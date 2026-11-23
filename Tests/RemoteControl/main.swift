import Foundation
var checks = 0
func check(_ condition: Bool, _ label: String) { precondition(condition,label); checks += 1; print("PASS \(label)") }
check(RemoteCommand.parse("set_session",["enabled":true]) != nil,"boolean accepted")
check(RemoteCommand.parse("set_session",["enabled":1]) == nil,"numeric boolean rejected")
check(RemoteCommand.parse("shutdown",["force":true]) == nil,"force flag rejected")
check(RemoteCommand.parse("shell",["command":"shutdown"]) == nil,"arbitrary commands rejected")
check(RemoteCommand.parse("schedule",["minutes":0,"action":"shutdown"]) == nil,"zero duration rejected")
check(RemoteCommand.parse("schedule",["minutes":15.5,"action":"shutdown"]) == nil,"fractional duration rejected")
check(RemoteCommand.parse("schedule",["minutes":15,"action":"restart"]) != nil,"allowed schedule accepted")
check(RemoteCommand.parse("set_conditions",["acOnly":true,"stopOnDisconnect":false,"batteryFloor":1]) == nil,"weak battery threshold rejected")
check(RemoteCommand.parse("set_conditions",["acOnly":true,"stopOnDisconnect":false,"batteryFloor":30]) != nil,"conditions accepted")
var auth = RemoteAuthorization()
let viewer="viewer-A", now=1000.0
let first=UUID().uuidString
check(!auth.accept(id:first,viewer:viewer,expires:now+1000,cancel:false,now:now,grantID:auth.grant ?? "none"),"no implicit approval")
auth.connect(viewer)
check(!auth.approve("viewer-B"),"wrong viewer cannot be approved")
check(auth.approve(viewer),"current viewer approved")
check(auth.accept(id:first,viewer:viewer,expires:now+1000,cancel:false,now:now,grantID:auth.grant ?? "none"),"approved fresh command accepted")
check(!auth.accept(id:first.lowercased(),viewer:viewer,expires:now+1000,cancel:false,now:now,grantID:auth.grant ?? "none"),"case-insensitive replay rejected")
check(!auth.accept(id:UUID().uuidString,viewer:viewer,expires:now,cancel:false,now:now,grantID:auth.grant ?? "none"),"expired command rejected")
check(!auth.accept(id:UUID().uuidString,viewer:viewer,expires:now+21000,cancel:false,now:now,grantID:auth.grant ?? "none"),"far-future deadline rejected")
auth.connect("viewer-B")
check(!auth.accept(id:UUID().uuidString,viewer:"viewer-B",expires:now+1000,cancel:false,now:now,grantID:auth.grant ?? "none"),"reconnect loses permission")
auth.connect(viewer);_ = auth.approve(viewer)
for _ in 0..<256 { check(auth.accept(id:UUID().uuidString,viewer:viewer,expires:now+1000,cancel:false,now:now,grantID:auth.grant ?? "none"),"bounded command accepted") }
check(!auth.accept(id:UUID().uuidString,viewer:viewer,expires:now+1000,cancel:false,now:now,grantID:auth.grant ?? "none"),"cache exhaustion cannot allow replay")
check(auth.accept(id:UUID().uuidString,viewer:viewer,expires:now+1000,cancel:true,now:now,grantID:auth.grant ?? "none"),"cancellation survives budget exhaustion")
let oldGrant=auth.grant!
auth.revoke(); _ = auth.approve(viewer)
check(!auth.accept(id:UUID().uuidString,viewer:viewer,expires:now+1000,cancel:false,now:now,grantID:oldGrant),"old grant cannot cross reapproval")
auth.revoke()
check(!auth.accept(id:UUID().uuidString,viewer:viewer,expires:now+1000,cancel:true,now:now,grantID:auth.grant ?? "none"),"revocation also denies cancellation")
print("\(checks) remote command/authorization checks passed")
