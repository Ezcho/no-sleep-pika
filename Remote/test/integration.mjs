import { Miniflare, convertV4MiniflareOptions } from 'miniflare';
import { readFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import assert from 'node:assert/strict';
const makeOptions = source => convertV4MiniflareOptions({workers:[{name:"pika",modules:true,script:source,compatibilityDate:'2025-10-01',
 durableObjects:{ROOMS:{className:'Room',useSQLite:true},ADMISSION:{className:'Admission',useSQLite:true}},
 ratelimits:{LIMITER:{namespace_id:'1001',simple:{limit:30,period:60}},PAIR_LIMITER:{namespace_id:'1002',simple:{limit:3,period:60}}},
 serviceBindings:{ASSETS:()=>new Response('test')}}]});
const source=await readFile(new URL('../.build/worker.js',import.meta.url),'utf8');
let mf=new Miniflare(makeOptions(source));
const base='https://pika.test'; let n=0;
async function req(path,options={}) {return mf.dispatchFetch(base+path,options);}
function next(ws,type) {
 return new Promise((resolve,reject)=>{
  const timer=setTimeout(()=>{ws.removeEventListener('message',on);reject(Error(`timeout ${type}`));},5000);
  function on(e){let m;try{m=JSON.parse(e.data);}catch{return;}if(m.type===type){clearTimeout(timer);ws.removeEventListener('message',on);resolve(m);}}
  ws.addEventListener('message',on);
 });
}
async function sock(room,role,token){const r=await req(`/api/room/${room}/socket`,{headers:{Upgrade:'websocket'}});assert.equal(r.status,101);const ws=r.webSocket;ws.accept();const ready=next(ws,'ready');ws.send(JSON.stringify({type:'auth',role,token}));await ready;return ws;}
function closed(ws){return new Promise((resolve,reject)=>{const timer=setTimeout(()=>reject(Error('close timeout')),5000);ws.addEventListener('close',e=>{clearTimeout(timer);resolve(e.code);},{once:true});});}
function pass(label){console.log('PASS',++n,label);}
try {
 let r=await req('/api/pair',{method:'POST',headers:{Origin:'https://evil.test'}});assert.equal(r.status,403);pass('cross-origin pairing denied');
 const p=await (await req('/api/pair',{method:'POST'})).json();assert.match(p.id,/^[\w-]{43}$/);pass('room created with opaque ID');
 const host=await sock(p.id,'host',p.hostToken);
 const claims=await Promise.all([1,2].map(()=>req(`/api/room/${p.id}/claim`,{method:'POST',body:JSON.stringify({token:p.pairToken})})));
 assert.deepEqual(claims.map(x=>x.status).sort(),[200,403]);const v=await claims.find(x=>x.status===200).json();pass('concurrent QR claim succeeds exactly once');
 const viewer=await sock(p.id,'viewer',v.viewerToken);
 const received=next(viewer,'status');host.send(JSON.stringify({type:'status',status:{ok:true,sessionOn:true,lastError:'private path',safety:{batteryPercent:80,onAC:true}}}));
 const status=await received;assert.equal(status.status.sessionOn,true);assert.equal(status.status.lastError,undefined);pass('real relay filters private diagnostics');
 const invalid=await req(`/api/room/${p.id}/socket`,{headers:{Upgrade:'websocket'}});invalid.webSocket.accept();const invalidClose=closed(invalid.webSocket);invalid.webSocket.send('null');assert.equal(await invalidClose,1008);pass('null frame rejected without crashing room');
 const refresh=next(host,'refresh');viewer.send(JSON.stringify({type:'refresh'}));await refresh;pass('legitimate connection survives malformed peer');
 const writeClose=closed(viewer);viewer.send(JSON.stringify({type:'set_session',enabled:true}));assert.equal(await writeClose,1008);pass('remote mutations denied');
 const viewer2=await sock(p.id,'viewer',v.viewerToken);
 r=await req(`/api/room/${p.id}/revoke`,{method:'POST',headers:{Authorization:`Bearer ${v.viewerToken}`}});assert.equal(r.status,403);pass('viewer cannot revoke as host');
 const hostClose=closed(host), viewerClose=closed(viewer2);
 r=await req(`/api/room/${p.id}/revoke`,{method:'POST',headers:{Authorization:`Bearer ${p.hostToken}`}});assert.equal(r.status,200);await Promise.all([hostClose,viewerClose]);
 r=await req(`/api/room/${p.id}/socket`,{headers:{Upgrade:'websocket'}});assert.equal(r.status,403);pass('revoke closes peers and rejects reconnect');
 r=await req(`/api/room/${p.id}/claim?token=secret`,{method:'POST'});assert.equal(r.status,403);pass('URL query credentials rejected');
 // No mutation of real app or power settings occurs in this test.
 console.log(`${n} live Durable Object integration checks passed`);
} finally {await mf.dispose();}

// Exercise the same production expiry paths with shortened constants only in memory.
assert(source.includes('var PAIR_TTL = 5 * 60 * 1e3;'));
assert(source.includes('var SESSION_TTL = 24 * 60 * 60 * 1e3;'));
mf=new Miniflare(makeOptions(source.replace('var PAIR_TTL = 5 * 60 * 1e3;','var PAIR_TTL = 1000;').replace('var SESSION_TTL = 24 * 60 * 60 * 1e3;','var SESSION_TTL = 2500;')));
try {
 const p=await (await req('/api/pair',{method:'POST'})).json();
 const v=await (await req(`/api/room/${p.id}/claim`,{method:'POST',body:JSON.stringify({token:p.pairToken})})).json();
 const host=await sock(p.id,'host',p.hostToken), viewer=await sock(p.id,'viewer',v.viewerToken);
 await Promise.all([closed(host),closed(viewer)]);
 assert.equal((await req(`/api/room/${p.id}/socket`,{headers:{Upgrade:'websocket'}})).status,403);
 pass('session expiry closes existing sockets and denies reconnect');
 const q=await (await req('/api/pair',{method:'POST'})).json();
 await new Promise(r=>setTimeout(r,1300));
 assert.equal((await req(`/api/room/${q.id}/claim`,{method:'POST',body:JSON.stringify({token:q.pairToken})})).status,403);
 pass('unclaimed QR expires without relying on client clock');
} finally {await mf.dispose();}
