'use strict';
const $ = id => document.getElementById(id);
const valid = s => typeof s === 'string' && /^[A-Za-z0-9_-]{43}$/.test(s);
let invite, session, socket, retry, heartbeat, stopped = false;
// Fragment is never sent to the server or retained in browser history.
const fragment = location.hash.slice(1); history.replaceState(null,'',location.pathname);
try {
  if (fragment) { const p=new URLSearchParams(fragment); if(valid(p.get('room')) && valid(p.get('token'))) invite={room:p.get('room'),token:p.get('token')}; }
  const saved=JSON.parse(sessionStorage.getItem('pikaRemote')||'null');
  if (saved && valid(saved.room) && valid(saved.viewerToken) && saved.expiresAt>Date.now()) session=saved;
} catch { /* Storage disabled or stale data; QR can still pair this tab. */ }
function message(text) { $('connection').textContent=text; }
function stale(text) { $('dashboard').classList.add('stale'); $('refresh').disabled=true; message(text); }
function forget() { stopped=true; clearTimeout(retry); clearInterval(heartbeat); socket?.close(); session=null; try {sessionStorage.removeItem('pikaRemote');}catch{} $('dashboard').hidden=true; message('연결 정보가 지워졌습니다. 새 QR로 다시 연결하세요.'); }
function connect() {
  if(stopped || !session) return;
  if(session.expiresAt<=Date.now()) {forget();message('연결이 만료되었습니다. 새 QR을 요청하세요.');return;}
  socket=new WebSocket(`${location.protocol==='https:'?'wss:':'ws:'}//${location.host}/api/room/${session.room}/socket`);
  const ws=socket;
  ws.onopen=()=>ws.send(JSON.stringify({type:'auth',role:'viewer',token:session.viewerToken}));
  ws.onmessage=event=>{
    if(event.data==='pong') return;
    let m;try{m=JSON.parse(event.data);}catch{return;}
    if(m.type==='ready') { $('dashboard').hidden=false; message('연결됨 · Mac 상태를 기다리는 중'); ws.send(JSON.stringify({type:'refresh'})); clearInterval(heartbeat); heartbeat=setInterval(()=>{if(ws.readyState===1)ws.send('ping');},45000); }
    if(m.type==='presence' && !m.host) stale('Mac 연결이 끊겼습니다. 아래 값은 마지막 확인 상태입니다.');
    if(m.type==='status') {
      const s=m.status; $('dashboard').classList.remove('stale');$('refresh').disabled=false;
      message(s.ok===true?'Mac 연결됨':'Mac 상태 확인 실패'); if(s.ok!==true)$('dashboard').classList.add('stale');
      $('session').textContent=typeof s.sessionOn==='boolean'?(s.sessionOn?'ON':'OFF'):'확인 불가';$('monitor').textContent=typeof s.monitorOn==='boolean'?(s.monitorOn?'ON':'OFF'):'확인 불가';
      $('battery').textContent=typeof s.safety?.batteryPercent==='number'?`${s.safety.batteryPercent}%${s.safety.onAC?' · 충전 중':''}`:'확인 불가';
      $('lid').textContent=typeof s.safety?.lidClosed==='boolean'?(s.safety.lidClosed?'닫힘':'열림'):'확인 불가';
      $('health').textContent=s.recoveryRequired?'Mac에서 복구 필요':s.waitingForLid?'덮개 닫기 대기':s.busy?'처리 중':s.ok?'정상':'확인 불가';
      $('updated').textContent=`마지막 확인 ${new Date(m.at).toLocaleTimeString()}`;
    }
  };
  ws.onclose=e=>{clearInterval(heartbeat);stale('연결이 끊겼습니다. 다시 연결 중…');if([1008,4001,4003].includes(e.code)){forget();message('연결이 종료되었습니다. 새 QR로 연결해 주세요.');}else if(!stopped)retry=setTimeout(connect,5000);};
  ws.onerror=()=>ws.close();
}
$('connect').onclick=async()=>{
  $('connect').disabled=true;
  try {
    const r=await fetch(`/api/room/${invite.room}/claim`,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({token:invite.token}),cache:'no-store'});
    if(!r.ok) throw Error();
    const data=await r.json(); session={room:invite.room,...data}; invite=null;
    try{sessionStorage.setItem('pikaRemote',JSON.stringify(session));}catch{}
    $('connect').hidden=true; connect();
  }catch{message('QR이 만료되었거나 이미 사용되었습니다. Mac에서 새 QR을 요청하세요.');}
};
$('refresh').onclick=()=>{if(socket?.readyState===1){socket.send(JSON.stringify({type:'refresh'}));$('refresh').disabled=true;setTimeout(()=>{$('refresh').disabled=false;},3000);}};
$('disconnect').onclick=forget;
if(invite){$('connect').hidden=false;message('이 QR로 Mac 상태를 확인할 수 있습니다. 연결하시겠어요?');}else if(session)connect();
setInterval(()=>{if(session && session.expiresAt<=Date.now()){forget();message('24시간 연결이 만료되었습니다.');}},15000);
window.addEventListener('pagehide',()=>{stopped=true;clearTimeout(retry);clearInterval(heartbeat);socket?.close();});
window.addEventListener('pageshow',e=>{if(e.persisted){stopped=false;connect();}});
