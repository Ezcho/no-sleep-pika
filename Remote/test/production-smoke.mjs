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
 // Both sockets below belong to this synthetic test, never to a user's Mac.
 const message=(ws,type)=>wait(ws,'message',e=>JSON.parse(e.data).type===type).then(e=>JSON.parse(e.data));
 const denied=message(viewer,'command_result');viewer.send(JSON.stringify({type:'command',id:crypto.randomUUID(),action:'shutdown',args:{}}));assert.equal((await denied).code,'denied');
 const capable=message(viewer,'capabilities');host.send(JSON.stringify({type:'capabilities',control:true}));assert.equal((await capable).control,true);
 const approval=message(host,'control_request');viewer.send(JSON.stringify({type:'control_request',id:crypto.randomUUID()}));const request=await approval,grantID=crypto.randomUUID();
 const granted=message(viewer,'control_permission');host.send(JSON.stringify({type:'control_permission',viewerID:request.viewerID,enabled:true,grantID}));assert.equal((await granted).enabled,true);
 const command=message(host,'command'),id=crypto.randomUUID();viewer.send(JSON.stringify({type:'command',id,grantID,action:'set_session',args:{enabled:false}}));const delivery=await command;assert.equal(delivery.id,id);assert.equal(delivery.viewerID,request.viewerID);assert(delivery.expiresAt>Date.now());
 const ack=message(viewer,'command_result');host.send(JSON.stringify({type:'command_result',id,ok:true,code:'accepted'}));assert.equal((await ack).ok,true);
 const replay=message(viewer,'command_result');viewer.send(JSON.stringify({type:'command',id,grantID,action:'set_session',args:{enabled:false}}));assert.equal((await replay).code,'denied');
 const hostClosed=wait(host,'close'),viewerClosed=wait(viewer,'close');
 assert.equal((await post(`/api/room/${room.id}/revoke`,null,{Authorization:`Bearer ${room.hostToken}`})).status,200);
 await Promise.all([hostClosed,viewerClosed]);
 assert.equal((await post(`/api/room/${room.id}/claim`,{token:room.pairToken})).status,403);
 console.log('PASS PROD HTTPS/CSP, one-use QR, authenticated WSS state relay, approval-bound synthetic commands, replay rejection, revocation and reuse rejection');
}finally{if(room)await post(`/api/room/${room.id}/revoke`,null,{Authorization:`Bearer ${room.hostToken}`});}
