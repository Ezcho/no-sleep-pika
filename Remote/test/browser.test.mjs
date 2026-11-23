import {test} from 'node:test';
import assert from 'node:assert/strict';
import vm from 'node:vm';
import {readFileSync} from 'node:fs';
import {randomUUID} from 'node:crypto';

function page() {
 const elements=new Map();
 const element=id=>{if(!elements.has(id))elements.set(id,{disabled:id==='controls',checked:false,value:'0',textContent:'',hidden:false,classList:{add(){},remove(){}}});return elements.get(id);};
 const sockets=[];
 class WebSocket {constructor(){this.readyState=1;this.sent=[];sockets.push(this);}send(s){this.sent.push(JSON.parse(s));}close(){this.readyState=3;}}
 const ctx=vm.createContext({document:{getElementById:element,activeElement:null,hidden:false,addEventListener(){}},window:{addEventListener(){}},location:{hash:'',pathname:'/',host:'pika.test',protocol:'https:'},history:{replaceState(){}},sessionStorage:{getItem(){return JSON.stringify({room:'a'.repeat(43),viewerToken:'b'.repeat(43),expiresAt:Date.now()+60000});},removeItem(){},setItem(){}},WebSocket,URLSearchParams,crypto:{randomUUID},Date,JSON,Number,Math,confirm:()=>true,setTimeout:()=>1,clearTimeout(){},setInterval(){},clearInterval(){}});
 vm.runInContext(readFileSync(new URL('../public/app.js',import.meta.url),'utf8'),ctx);
 const ws=sockets[0];ws.onopen();
 const receive=m=>ws.onmessage({data:JSON.stringify(m)});
 return {element,ws,receive,ctx};
}
test('web controls require capability, live status and explicit approval; no optimistic state',()=>{
 const {element:e,ws,receive}=page();
 e('shutdown').onclick();assert.equal(ws.sent.filter(m=>m.type==='command').length,0);
 receive({type:'ready'});receive({type:'presence',host:true});receive({type:'capabilities',control:true});
 receive({type:'status',at:Date.now(),status:{ok:true,sessionOn:false,monitorOn:false,safety:{batteryPercent:80,onAC:true},power:{acOnly:false,stopOnDisconnect:false,batteryFloor:0}}});
 assert.equal(e('controls').disabled,true);
 receive({type:'control_permission',enabled:true,grantID:randomUUID()});assert.equal(e('controls').disabled,false);
 e('session-on').onclick();const cmd=ws.sent.find(m=>m.type==='command');assert.equal(cmd.action,'set_session');assert.equal(e('session').textContent,'OFF');
 receive({type:'command_result',id:cmd.id,ok:true,code:'accepted'});assert.equal(e('session').textContent,'OFF');assert.match(e('command-message').textContent,/실제 상태/);
 receive({type:'presence',host:false});assert.equal(e('controls').disabled,true);e('shutdown').onclick();assert.equal(ws.sent.filter(m=>m.type==='command').length,1);
});
test('cancel remains available while a command is awaiting response',()=>{
 const {element:e,ws,receive}=page();receive({type:'presence',host:true});receive({type:'capabilities',control:true});receive({type:'status',at:Date.now(),status:{ok:true,sessionOn:true}});receive({type:'control_permission',enabled:true,grantID:randomUUID()});
 e('shutdown').onclick();assert.equal(e('controls').disabled,false);e('cancel-timer').onclick();
 assert.deepEqual(ws.sent.filter(m=>m.type==='command').map(m=>m.action),['shutdown','cancel_timer']);
});
test('old app capability and stale status cannot enable remote writes',()=>{
 const {element:e,receive,ctx}=page();receive({type:'presence',host:true});receive({type:'status',at:Date.now(),status:{ok:true}});receive({type:'control_permission',enabled:true,grantID:randomUUID()});assert.equal(e('controls').disabled,true);
 receive({type:'capabilities',control:true});assert.equal(e('controls').disabled,false);
 vm.runInContext('lastStatusAt=Date.now()-21000;controls()',ctx);assert.equal(e('controls').disabled,true);
});
