import { test } from 'node:test';
import assert from 'node:assert/strict';
import { live, claimable, safeStatus, validToken } from '../src/policy.mjs';
test('expiry and single use are enforced independently of cleanup',()=>{
 const r={expiresAt:100,pairUntil:50,pairHash:'secret'};
 assert.equal(claimable(r,'secret',49),true);assert.equal(claimable(r,'secret',50),false);
 assert.equal(claimable({...r,viewerHash:'claimed'},'secret',1),false);
 assert.equal(live(r,100),false);assert.equal(live({...r,revoked:true},1),false);
});
test('strict token and status allowlists',()=>{
 assert.equal(validToken('a'.repeat(43)),true);for(const bad of [null,{},'a'.repeat(42),'../'+ 'a'.repeat(43)])assert.equal(validToken(bad),false);
 const s=safeStatus({ok:false,lastError:'/Users/private',command:'rm',safety:{batteryPercent:101,thermalState:'<script>',onAC:true,issue:'secret'}});
 assert.deepEqual(s,{ok:false,safety:{onAC:true}});
});
