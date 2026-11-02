// Explicit opt-in: creates ONE ephemeral room on the supplied gateway, then revokes it.
import assert from 'node:assert/strict';
const base=process.env.PIKA_SMOKE_ORIGIN;
if(!base || new URL(base).protocol!=='https:') throw Error('Set PIKA_SMOKE_ORIGIN to the authorized HTTPS gateway');
let room;
const post=(path,body,headers={})=>fetch(base+path,{method:'POST',headers:{'Content-Type':'application/json',...headers},...(body?{body:JSON.stringify(body)}:{})});
function wait(ws,event,predicate=()=>true){return new Promise((resolve,reject)=>{const t=setTimeout(()=>{ws.removeEventListener(event,on);reject(Error('Timeout: '+event));},10000);function on(e){if(predicate(e)){clearTimeout(t);ws.removeEventListener(event,on);resolve(e);}}ws.addEventListener(event,on);});}
async function auth(role,token){const ws=new WebSocket(base.replace('https:','wss:')+`/api/room/${room.id}/socket`);await wait(ws,'open');const ready=wait(ws,'message',e=>JSON.parse(e.data).type==='ready');ws.send(JSON.stringify({type:'auth',role,token}));await ready;return ws;}
try{
 const page=await fetch(base);assert.equal(page.status,200);assert.match(page.headers.get('content-security-policy'),/frame-ancestors 'none'/);
 const r=await post('/api/pair');assert.equal(r.status,200);room=await r.json();
 const claim=await post(`/api/room/${room.id}/claim`,{token:room.pairToken});assert.equal(claim.status,200);const v=await claim.json();
 assert.equal((await post(`/api/room/${room.id}/claim`,{token:room.pairToken})).status,403);
 const host=await auth('host',room.hostToken),viewer=await auth('viewer',v.viewerToken);
 const status=wait(viewer,'message',e=>JSON.parse(e.data).type==='status');host.send(JSON.stringify({type:'status',status:{ok:true,sessionOn:false,monitorOn:false,safety:{batteryPercent:80,onAC:true}}}));
 assert.equal(JSON.parse((await status).data).status.sessionOn,false);
 const hostClosed=wait(host,'close'),viewerClosed=wait(viewer,'close');
 assert.equal((await post(`/api/room/${room.id}/revoke`,null,{Authorization:`Bearer ${room.hostToken}`})).status,200);
 await Promise.all([hostClosed,viewerClosed]);
 assert.equal((await post(`/api/room/${room.id}/claim`,{token:room.pairToken})).status,403);
 console.log('PASS PROD HTTPS/CSP, one-use QR, authenticated WSS state relay, revocation and reuse rejection');
}finally{if(room)await post(`/api/room/${room.id}/revoke`,null,{Authorization:`Bearer ${room.hostToken}`});}
