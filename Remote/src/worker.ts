import { DurableObject } from 'cloudflare:workers';
import { PAIR_TTL, SESSION_TTL, validToken, live, claimable, safeStatus } from './policy.mjs';
interface Env { ROOMS: DurableObjectNamespace<Room>; ADMISSION: DurableObjectNamespace<Admission>; LIMITER: RateLimit; PAIR_LIMITER: RateLimit; ASSETS: Fetcher }
interface RecordData { hostHash: string; pairHash: string; pairUntil: number; expiresAt: number; viewerHash?: string; revoked?: boolean }
const json = (value: unknown, status = 200) => Response.json(value, {status, headers: {'Cache-Control': 'no-store', 'Referrer-Policy': 'no-referrer'}});
const deny = () => json({error: 'Connection unavailable or expired'}, 403);
function token() { return btoa(String.fromCharCode(...crypto.getRandomValues(new Uint8Array(32)))).replaceAll('+','-').replaceAll('/','_').replaceAll('=',''); }
async function hash(s: string) { return Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(s))), n => n.toString(16).padStart(2,'0')).join(''); }
async function body(req: Request): Promise<any> {
  const reader = req.body?.getReader(); if (!reader) throw Error('body');
  const deadline = Date.now()+5000;
  let bytes = new Uint8Array(0);
  try {
    while (true) {
      let timer: ReturnType<typeof setTimeout> | undefined;
      const {done,value} = await Promise.race([reader.read(), new Promise<never>((_,reject)=>{
        timer=setTimeout(()=>reject(Error('timeout')),Math.max(0,deadline-Date.now()));
      })]).finally(()=>clearTimeout(timer ?? null));
      if (done) break;
      if (bytes.length + value.length > 4096 || Date.now()>deadline) throw Error('size or timeout');
      const next = new Uint8Array(bytes.length + value.length); next.set(bytes); next.set(value,bytes.length); bytes = next;
    }
    return JSON.parse(new TextDecoder().decode(bytes));
  } finally { void reader.cancel().catch(()=>{}); }
}

export default {
  async fetch(req: Request, env: Env): Promise<Response> {
    const url = new URL(req.url);
    if (url.protocol !== 'https:' && url.hostname !== '127.0.0.1' && url.hostname !== 'localhost') return deny();
    if (url.pathname.startsWith('/api/')) {
      if (url.search) return deny(); // No credentials in URLs/logs.
      const origin = req.headers.get('Origin');
      if (origin && origin !== url.origin) return deny();
      const key = req.headers.get('CF-Connecting-IP') || 'local';
      if (!(await env.LIMITER.limit({key})).success) return json({error:'Too many requests'},429);
      if (url.pathname === '/api/pair' && req.method === 'POST') {
        if (!(await env.PAIR_LIMITER.limit({key})).success) return json({error:'Pairing rate limit'},429);
        const permission = await env.ADMISSION.getByName('daily').fetch(new Request('https://internal/admit',{method:'POST',headers:{'X-Client':await hash(key)}}));
        if (!permission.ok) return permission;
        const id = token();
        return env.ROOMS.getByName(id).fetch(new Request('https://internal/create',{method:'POST'}));
      }
      const match = /^\/api\/room\/([A-Za-z0-9_-]{43})\/(claim|socket|revoke)$/.exec(url.pathname);
      if (!match) return json({error:'Not found'},404);
      if (match[2] === 'claim' && req.method === 'POST') {
        let parsed; try { parsed = await body(req); } catch { return deny(); }
        if (!parsed || typeof parsed !== 'object' || Array.isArray(parsed) || !validToken(parsed.token)) return deny();
        return env.ROOMS.getByName(match[1]).fetch(new Request(req.url,{method:'POST',body:JSON.stringify({token:parsed.token})}));
      }
      return env.ROOMS.getByName(match[1]).fetch(req);
    }
    if (req.method !== 'GET' && req.method !== 'HEAD') return json({error:'Method not allowed'},405);
    const result = await env.ASSETS.fetch(req);
    const response = new Response(result.body,result);
    response.headers.set('Content-Security-Policy', `default-src 'none'; script-src 'self'; style-src 'self'; connect-src 'self' wss://${url.host}; img-src 'self' data:; base-uri 'none'; frame-ancestors 'none'; form-action 'none'`);
    response.headers.set('Referrer-Policy','no-referrer');
    response.headers.set('X-Content-Type-Options','nosniff');
    response.headers.set('Cache-Control','no-store');
    response.headers.set('Permissions-Policy','camera=(), microphone=(), geolocation=()');
    return response;
  }
} satisfies ExportedHandler<Env>;
// Bound public provisioning independently of per-IP rate limiting and room IDs.
export class Admission extends DurableObject<Env> {
  async fetch(req: Request): Promise<Response> {
    return this.ctx.blockConcurrencyWhile(async () => {
      const day = Math.floor(Date.now()/86400000);
      const counter = await this.ctx.storage.get<{day:number,count:number}>('counter');
      const count = counter?.day === day ? counter.count : 0;
      if (counter?.day !== day) await this.ctx.storage.deleteAll();
      const client = req.headers.get('X-Client') || 'local';
      const used = await this.ctx.storage.get<number>(client) || 0;
      if (used >= 20) return json({error:'Daily device pairing limit'},429);
      if (count >= 1000) return json({error:'Daily pairing capacity reached'},429);
      await this.ctx.storage.put(client,used+1);
      await this.ctx.storage.put('counter',{day,count:count+1}); return json({ok:true});
    });
  }
}
export class Room extends DurableObject<Env> {
  constructor(ctx: DurableObjectState,env:Env) { super(ctx,env); ctx.setWebSocketAutoResponse(new WebSocketRequestResponsePair('ping','pong')); }
  async fetch(req: Request): Promise<Response> {
    let parsed: any;
    if (new URL(req.url).pathname.endsWith('/claim')) {
      try { parsed = await body(req); } catch { return deny(); }
      if (!parsed || typeof parsed !== 'object' || Array.isArray(parsed)) return deny();
    }
    return this.ctx.blockConcurrencyWhile(async () => {
      const path = new URL(req.url).pathname;
      let r = await this.ctx.storage.get<RecordData>('room');
      if (path === '/create' && req.method === 'POST' && !r) {
        const host = token(), pair = token();
        r = {hostHash:await hash(host),pairHash:await hash(pair),pairUntil:Date.now()+PAIR_TTL,expiresAt:Date.now()+SESSION_TTL};
        await this.ctx.storage.put('room',r); await this.ctx.storage.setAlarm(r.pairUntil);
        return json({id:this.ctx.id.name,hostToken:host,pairToken:pair,pairUntil:r.pairUntil,expiresAt:r.expiresAt});
      }
      if (!live(r)) return deny();
      r = r!;
      if (path.endsWith('/claim') && req.method === 'POST') {
        const b = parsed;
        if (!validToken(b.token) || !claimable(r,await hash(b.token))) return deny();
        const viewer = token(); r.viewerHash = await hash(viewer); r.pairHash = '';
        await this.ctx.storage.put('room',r); await this.schedule(r);
        return json({viewerToken:viewer,expiresAt:r.expiresAt});
      }
      if (path.endsWith('/revoke') && req.method === 'POST') {
        const credential = req.headers.get('Authorization')?.replace(/^Bearer /,'') || '';
        if (!validToken(credential) || await hash(credential) !== r.hostHash) return deny();
        await this.expire(); return json({ok:true});
      }
      if (path.endsWith('/socket') && req.method === 'GET' && req.headers.get('Upgrade')?.toLowerCase() === 'websocket') {
        if (this.ctx.getWebSockets().length >= 4) return json({error:'Connection limit'},429);
        const pair = new WebSocketPair();
        this.ctx.acceptWebSocket(pair[1]);
        pair[1].serializeAttachment({role:'pending',deadline:Date.now()+10000,window:Date.now(),count:0});
        await this.schedule(r);
        return new Response(null,{status:101,webSocket:pair[0]});
      }
      return deny();
    });
  }
  async schedule(r: RecordData) {
    const deadlines = this.ctx.getWebSockets().filter(ws=>ws.readyState===1).map(ws => ws.deserializeAttachment()).filter(a => a?.role === 'pending').map(a=>a.deadline);
    await this.ctx.storage.setAlarm(Math.min(r.viewerHash ? r.expiresAt : r.pairUntil,...deadlines));
  }
  async webSocketMessage(ws: WebSocket,message: string | ArrayBuffer) {
    // Serializes authentication/revocation with messages across async hash/storage awaits.
    await this.ctx.blockConcurrencyWhile(async () => {
      const r = await this.ctx.storage.get<RecordData>('room');
      const a = ws.deserializeAttachment();
      if (!live(r) || !a || typeof message !== 'string' || new TextEncoder().encode(message).length > 8192) { ws.close(1008,'Unavailable'); return; }
      if (Date.now()-a.window > 60000) { a.window=Date.now(); a.count=0; }
      if (++a.count > 30) { ws.close(1008,'Rate limit'); return; }
      ws.serializeAttachment(a);
      let m; try { m=JSON.parse(message); } catch { ws.close(1008,'Invalid message'); return; }
      if (!m || typeof m !== 'object' || Array.isArray(m)) { ws.close(1008,'Invalid message'); return; }
      if (a.role === 'pending') {
        if (Date.now() >= a.deadline || m.type !== 'auth' || !validToken(m.token) || !['host','viewer'].includes(m.role)) { ws.close(1008,'Unauthorized'); return; }
        const expected = m.role === 'host' ? r!.hostHash : r!.viewerHash;
        if (!expected || await hash(m.token) !== expected) { ws.close(1008,'Unauthorized'); return; }
        for (const old of this.ctx.getWebSockets()) if (old !== ws && old.deserializeAttachment()?.role === m.role) old.close(4001,'Replaced');
        a.role=m.role; ws.serializeAttachment(a);
        ws.send(JSON.stringify({type:'ready',role:a.role,expiresAt:r!.expiresAt,paired:!!r!.viewerHash}));
        this.presence(); await this.schedule(r!); return;
      }
      if (a.role === 'host' && m.type === 'status') {
        for (const peer of this.ctx.getWebSockets()) if (peer.deserializeAttachment()?.role === 'viewer') this.send(peer,{type:'status',status:safeStatus(m.status),at:Date.now()});
      } else if (a.role === 'viewer' && m.type === 'refresh') {
        for (const peer of this.ctx.getWebSockets()) if (peer.deserializeAttachment()?.role === 'host') this.send(peer,{type:'refresh'});
      } else { ws.close(1008,'Read-only connection'); }
    });
  }
  send(ws:WebSocket,data:unknown) { try { ws.send(JSON.stringify(data)); } catch { /* Closed peer; reconnect reauthenticates. */ } }
  presence() {
    const sockets=this.ctx.getWebSockets().filter(ws=>ws.readyState===1);
    for (const ws of sockets) if (ws.deserializeAttachment()?.role !== 'pending') this.send(ws,{type:'presence',host:sockets.some(s=>s.deserializeAttachment()?.role==='host'),viewer:sockets.some(s=>s.deserializeAttachment()?.role==='viewer')});
  }
  webSocketClose(ws:WebSocket,code:number,reason:string) { try { ws.close([1005,1006,1015].includes(code)?1000:code,reason); } finally { this.presence(); } }
  webSocketError(ws:WebSocket) { ws.close(1011,'Connection error'); this.presence(); }
  async expire() { for(const ws of this.ctx.getWebSockets()) ws.close(4003,'Expired or revoked'); await this.ctx.storage.deleteAll(); }
  async alarm() {
    await this.ctx.blockConcurrencyWhile(async () => {
    const r=await this.ctx.storage.get<RecordData>('room');
    if (!live(r) || (!r!.viewerHash && Date.now()>=r!.pairUntil)) { await this.expire(); return; }
    for (const ws of this.ctx.getWebSockets()) { const a=ws.deserializeAttachment(); if (a?.role==='pending' && Date.now()>=a.deadline) { ws.serializeAttachment({...a,role:'closed'}); ws.close(1008,'Authentication timeout'); } }
    await this.schedule(r!);
    });
  }
}
