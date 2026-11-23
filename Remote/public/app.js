'use strict';
const $ = id => document.getElementById(id);
const valid = s => typeof s === 'string' && /^[A-Za-z0-9_-]{43}$/.test(s);
let invite, session, socket, retry, heartbeat, stopped = false;
let grantID=null;
let hostOnline=false, capable=false, approved=false, statusOK=false, lastStatusAt=0, pendingID=null, commandTimeout, approvalTimeout, latestStatus=null;
const actionNames={release:'세션 해제',sleep:'Mac 잠자기',shutdown:'Mac 종료',restart:'Mac 재시동'};
function controls() {
  const live=hostOnline && statusOK && Date.now()-lastStatusAt<20000 && socket?.readyState===1;
  $('controls').disabled=!(live && approved && capable);
  for(const id of ['session-on','session-off','monitor-on','monitor-off','save-conditions','schedule','shutdown','restart'])$(id).disabled=!!pendingID;
  $('request-control').disabled=!hostOnline || !capable || approved || !!approvalTimeout || socket?.readyState!==1;
  $('permission').textContent=approved && live?'제어 허용됨':'조회 전용';
  $('control-help').textContent=!capable?'원격 제어에는 Mac의 pika 1.3.0 이상이 필요합니다.':approved?'이 연결에서 제어가 허용됐습니다. 연결이 끊기면 Mac에서 다시 승인해야 합니다.':'아래 버튼을 누른 뒤 Mac 화면에서 원격 제어를 허용하세요.';
  if(approved && live && !pendingID){$('monitor-on').disabled=!latestStatus?.sessionOn || !!latestStatus?.busy;$('monitor-off').disabled=$('monitor-on').disabled;}
}
function clearApproval() {approved=false;grantID=null;clearTimeout(approvalTimeout);approvalTimeout=null;controls();}
function finishCommand(text) {pendingID=null;clearTimeout(commandTimeout);$('command-message').textContent=text;controls();}
function command(action,args={}) {
  if($('controls').disabled || (pendingID && action!=='cancel_timer'))return;
  clearTimeout(commandTimeout);pendingID=crypto.randomUUID();controls();$('command-message').textContent='Mac에 요청하는 중…';
  socket.send(JSON.stringify({type:'command',id:pendingID,grantID,action,args}));
  commandTimeout=setTimeout(()=>{finishCommand('응답을 확인하지 못했습니다. 자동 재시도하지 않습니다. 상태를 새로고침한 뒤 확인하세요.');},20000);
}
function renderTimers() {
  const p=latestStatus?.power;
  const describe=(action,deadline)=>actionNames[action]&&Number.isFinite(deadline)?`${actionNames[action]} · ${Math.max(0,Math.ceil((deadline-Date.now())/1000))}초 후`:null;
  $('timer-state').textContent=describe(p?.timerAction,p?.timerDeadline)||'예약 없음';
  $('pending-state').textContent=describe(p?.pendingAction,p?.pendingDeadline)||'';
}
// Fragment is never sent to the server or retained in browser history.
const fragment = location.hash.slice(1); history.replaceState(null,'',location.pathname);
try {
  if (fragment) { const p=new URLSearchParams(fragment); if(valid(p.get('room')) && valid(p.get('token'))) invite={room:p.get('room'),token:p.get('token')}; }
  const saved=JSON.parse(sessionStorage.getItem('pikaRemote')||'null');
  if (saved && valid(saved.room) && valid(saved.viewerToken) && saved.expiresAt>Date.now()) session=saved;
} catch { /* Storage disabled or stale data; QR can still pair this tab. */ }
function message(text) { $('connection').textContent=text; }
function stale(text) { statusOK=false;clearApproval();$('dashboard').classList.add('stale'); $('refresh').disabled=true; message(text); }
function forget() { hostOnline=false;capable=false;clearApproval();finishCommand('');stopped=true; clearTimeout(retry); clearInterval(heartbeat); socket?.close(); session=null; try {sessionStorage.removeItem('pikaRemote');}catch{} $('dashboard').hidden=true;$('control-panel').hidden=true; message('연결 정보가 지워졌습니다. 새 QR로 다시 연결하세요.'); }
function connect() {
  if(stopped || !session) return;
  if(session.expiresAt<=Date.now()) {forget();message('연결이 만료되었습니다. 새 QR을 요청하세요.');return;}
  hostOnline=false;capable=false;statusOK=false;clearApproval();
  socket=new WebSocket(`${location.protocol==='https:'?'wss:':'ws:'}//${location.host}/api/room/${session.room}/socket`);
  const ws=socket;
  ws.onopen=()=>ws.send(JSON.stringify({type:'auth',role:'viewer',token:session.viewerToken}));
  ws.onmessage=event=>{
    if(socket!==ws)return;
    if(event.data==='pong') return;
    let m;try{m=JSON.parse(event.data);}catch{return;}
    if(m.type==='ready') { $('dashboard').hidden=false;$('control-panel').hidden=false; message('연결됨 · Mac 상태를 기다리는 중'); ws.send(JSON.stringify({type:'refresh'})); clearInterval(heartbeat); heartbeat=setInterval(()=>{if(ws.readyState===1)ws.send('ping');},45000); }
    if(m.type==='presence') {hostOnline=m.host===true;if(!hostOnline){capable=false;stale('Mac 연결이 끊겼습니다. 아래 값은 마지막 확인 상태입니다.');if(pendingID)finishCommand('연결이 끊겨 실행 결과를 확인할 수 없습니다.');}controls();}
    if(m.type==='capabilities'){capable=m.control===true;if(!capable)clearApproval();controls();}
    if(m.type==='control_permission'){grantID=typeof m.grantID==='string'&&/^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i.test(m.grantID)?m.grantID.toLowerCase():null;approved=m.enabled===true&&grantID!==null;clearTimeout(approvalTimeout);approvalTimeout=null;$('command-message').textContent=approved?'Mac에서 원격 제어를 허용했습니다.':'제어가 허용되지 않았거나 해제되었습니다.';controls();}
    if(m.type==='command_result' && m.id===pendingID){const text=m.ok===true?'Mac이 요청을 받았습니다. 아래 실제 상태를 확인하세요.':({busy:'Mac이 다른 작업을 처리 중입니다.',denied:'제어 권한이 없습니다. Mac에서 다시 허용하세요.',invalid:'지원하지 않는 요청입니다.',failed:'요청을 처리하지 못했습니다. Mac에서 상태를 확인하세요.',cancelled:'요청이 취소되었습니다.'})[m.code]||'요청을 처리하지 못했습니다.';finishCommand(text);ws.send(JSON.stringify({type:'refresh'}));}
    if(m.type==='status') {
      const s=m.status;latestStatus=s;statusOK=s.ok===true;lastStatusAt=Date.now(); $('dashboard').classList.remove('stale');$('refresh').disabled=false;
      message(s.ok===true?'Mac 연결됨':'Mac 상태 확인 실패'); if(s.ok!==true)$('dashboard').classList.add('stale');
      $('session').textContent=typeof s.sessionOn==='boolean'?(s.sessionOn?'ON':'OFF'):'확인 불가';$('monitor').textContent=typeof s.monitorOn==='boolean'?(s.monitorOn?'ON':'OFF'):'확인 불가';
      $('battery').textContent=typeof s.safety?.batteryPercent==='number'?`${s.safety.batteryPercent}%${s.safety.onAC?' · 충전 중':''}`:'확인 불가';
      $('thermal').textContent=({normal:'정상',nominal:'정상',fair:'주의',serious:'높음',critical:'위험'})[s.safety?.thermalState]||'확인 불가';
      $('lid').textContent=typeof s.safety?.lidClosed==='boolean'?(s.safety.lidClosed?'닫힘':'열림'):'확인 불가';
      $('health').textContent=s.recoveryRequired?'Mac에서 복구 필요':s.waitingForLid?'덮개 닫기 대기':s.busy?'처리 중':s.ok?'정상':'확인 불가';
      const p=s.power;
      if(p && !pendingID && !document.activeElement?.closest('#controls')){$('ac-only').checked=p.acOnly===true;$('stop-disconnect').checked=p.stopOnDisconnect===true;$('battery-floor').value=String(p.batteryFloor??0);}
      renderTimers();controls();
      $('updated').textContent=`마지막 확인 ${new Date(m.at).toLocaleTimeString()}`;
    }
  };
  ws.onclose=e=>{if(socket!==ws)return;hostOnline=false;clearInterval(heartbeat);stale('연결이 끊겼습니다. 다시 연결 중…');if([1008,4001,4003].includes(e.code)){forget();message('연결이 종료되었습니다. 새 QR로 연결해 주세요.');}else if(!stopped)retry=setTimeout(connect,5000);};
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
$('refresh').onclick=()=>{if(socket?.readyState===1){socket.send(JSON.stringify({type:'refresh'}));$('refresh').disabled=true;setTimeout(()=>{$('refresh').disabled=!hostOnline||socket?.readyState!==1;},3000);}};
$('disconnect').onclick=forget;
$('request-control').onclick=()=>{if($('request-control').disabled)return;socket.send(JSON.stringify({type:'control_request',id:crypto.randomUUID()}));$('command-message').textContent='Mac 화면에서 원격 제어를 허용해 주세요.';approvalTimeout=setTimeout(()=>{approvalTimeout=null;$('command-message').textContent='승인 대기 시간이 지났습니다. Mac에서 승인하거나 다시 요청하세요.';controls();},60000);controls();};
$('session-on').onclick=()=>command('set_session',{enabled:true});$('session-off').onclick=()=>command('set_session',{enabled:false});
$('monitor-on').onclick=()=>command('set_monitor',{enabled:true});$('monitor-off').onclick=()=>command('set_monitor',{enabled:false});
$('save-conditions').onclick=()=>command('set_conditions',{acOnly:$('ac-only').checked,stopOnDisconnect:$('stop-disconnect').checked,batteryFloor:Number($('battery-floor').value)});
$('schedule').onclick=()=>{const minutes=Number($('timer-minutes').value),action=$('timer-action').value;if(confirm(`${minutes}분 후 ${actionNames[action]}을 예약할까요? 작업이 중단될 수 있습니다. pika 종료·Mac 잠자기 시 예약은 취소됩니다.`))command('schedule',{minutes,action});};
$('cancel-timer').onclick=()=>command('cancel_timer');
for(const action of ['shutdown','restart'])$(action).onclick=()=>{if(confirm(`${actionNames[action]}을 요청할까요? 60초 카운트다운 뒤 작업이 중단됩니다. 그 전에 취소할 수 있습니다.`))command(action);};
setInterval(()=>{controls();renderTimers();},1000);
setInterval(()=>{if(socket?.readyState===1)socket.send(JSON.stringify({type:'refresh'}));},10000);
document.addEventListener('visibilitychange',()=>{if(!document.hidden && socket?.readyState===1)socket.send(JSON.stringify({type:'refresh'}));});
if(invite){$('connect').hidden=false;message('이 QR로 Mac 상태를 확인할 수 있습니다. 연결하시겠어요?');}else if(session)connect();
setInterval(()=>{if(session && session.expiresAt<=Date.now()){forget();message('24시간 연결이 만료되었습니다.');}},15000);
window.addEventListener('pagehide',()=>{stopped=true;clearTimeout(retry);clearInterval(heartbeat);socket?.close();});
window.addEventListener('pageshow',e=>{if(e.persisted){stopped=false;connect();}});
