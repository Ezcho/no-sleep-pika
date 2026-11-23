# pika remote gateway

QR pairing for the native pika app. Connections start read-only; pika 1.3.0 can grant explicit local approval for bounded remote controls. Cloudflare Workers + SQLite Durable
Objects host both the mobile page and WSS relay. Existing GitHub Pages is unchanged.
Production gateway: https://pika-remote.always-wakeup.workers.dev (deployed 2026-11-03 KST).

## Product boundary

1. Local AI calls `pika_set_session(enabled: true)` if the user requested sleep
   prevention. Its real outcome must be checked; pairing itself never starts Session.
2. `pika_remote_pair` asks the running app for a new 5-minute, single-use QR.
   Display `qrText` in a monospace code block. For camera scanning, the tool also
   returns a PNG and a private local HTML `qrPreviewPath` (white background, quiet zone).
3. The phone scans and explicitly taps Connect. It can read Session, Monitor,
   battery, lid, and recovery state for at most 24 hours from issuance.
4. `pika_remote_revoke` or the Mac menu's **휴대폰 연결 해제** revokes access.
   This does not switch the local Session off. Closing the app stops its bridge.

The app owns the connection: closing the MCP client does not terminate it. Host
credentials live in app memory; app restart requires new pairing. Browser credentials
are tab-scoped sessionStorage. A lost claim response requires a new QR. The Mac must explicitly approve each live viewer connection before remote controls are accepted. Approval clears when either socket reconnects or disconnects. The fixed commands are Session/Monitor ON/OFF, power conditions, timer scheduling/cancellation, and shutdown/restart with a native cancellable countdown. No keyboard/mouse control, screen video, arbitrary IPC, shell commands, AI outputs, or file access are exposed.

## Develop and validate

Node 22+; macOS/Xcode required for native checks.

```sh
cd Remote
npm ci
npm run check
npm test
npm run test:integration
npm run dev
```

`npm run build` is **dry-run only**. Integration tests use ephemeral local workerd,
never the installed app or cloud resources. On this checkout a project-local Node
22 binary is under `.local/remote-runtime/node_modules/node/bin/node` (not committed).

From the repository root:

```sh
bash Scripts/test.sh

```

## Production rollout

1. Connect the intended Cloudflare account and confirm Workers **Free**. Keep
   billing disabled unless explicitly approved. No paid service or TURN needed.
2. In Remote, authenticate Wrangler and review `wrangler.jsonc`. The migration
   creates two SQLite DO classes; rate limiter namespaces are reserved for pika.
3. Explicit release step: `npx wrangler deploy`. Record the resulting HTTPS
   `workers.dev` origin. The free daily limits can reject operations: this is not
   an unlimited or SLA-backed endpoint.
4. Build the native app with the pinned origin:
   `PIKA_REMOTE_GATEWAY=https://YOUR-WORKER.YOUR-ACCOUNT.workers.dev bash Scripts/build.sh`.
   The committed Info.plist pins the production origin; the build setting overrides it for another trusted deployment. Removing both configurations makes QR creation fail closed with `remote_not_configured`.
   Never accept a gateway supplied by an MCP tool argument.
5. On a staging app/device, verify QR via iPhone and Android camera, read-only state,
   lid closure/reopen, airplane-mode reconnect, Mac app restart, local revoke,
   expired QR and 24-hour expiry. Confirm expired UI never looks live.
6. Package/sign/notarize using the existing release process and release only after
   device acceptance. No automatic main push, app version bump, or release workflow
   is included here. Replacing app binaries remotely is not part of QR pairing.

Rollback: disable remote routing or delete the Worker deployment, and ship an app
without PikaRemoteGateway. Native Session operation is independent of gateway health.
Durable Object migrations are forward-only; do not delete production namespaces as
part of routine code rollback. A compatible earlier Worker version is preferred.

## Security and operating limits

- 256-bit random host, invitation, and viewer tokens; server persists SHA-256 hashes.
- Fragment-only QR secret, removed from page history on load. Auth is an initial
  WebSocket frame, never a query parameter; host revocation uses Authorization.
- Atomic claim; every auth/message checks expiry. Alarms close expired sockets.
- 4 sockets/room, pending auth 10 seconds, frames <=8 KiB, 45 viewer JSON frames/minute and 60 host frames/minute (status plus command replies).
- Native status sampling every 5 seconds while observed; changed values only, minimum
  3 seconds between sends. Auto-response keepalive uses WebSocket hibernation.
- Pairing capped at 3/min/IP, 20/day/IP, 1,000/day across the deployment. Other HTTP
  requests capped at 30/min/IP. Shared NATs may hit limits. Distributed abuse can
  still exhaust free capacity; add challenge/device enrollment before broad promotion.
- IP counters are hashed and reset by the next UTC day request; no raw IPs retained
  by application storage. Cloudflare infrastructure may have its own access metadata.
- No application telemetry, request bodies, secrets, or status history are logged.
  A stale mobile dashboard indicates disconnection. It is not evidence of Mac shutdown.
- Transport is TLS to the relay, **not end-to-end encryption**. The relay sees the
  limited allowlisted state. Do not extend it to terminal output without revisiting this.
- If revoke cannot reach the gateway, local bridge stops and reports unconfirmed
  revocation; retain credentials for retry. Server credentials expire within 24 hours.
- QR is a bearer invitation: whoever scans it first can read state. No identity proof is claimed. Remote writes are denied by both server and native app until the Mac explicitly approves the current viewer ID. Each approval creates a fresh grant UUID included in every command, so delayed frames from a previous grant cannot cross a revoke/reapprove boundary. Reconnection requires approval again.
- Commands use exact typed allowlists, UUID IDs and 15-second delivery expiry. IDs are retained for the host socket lifetime, up to 256 commands; exhaustion requires a new connection and approval, not replay-cache eviction. The server allows at most 12 mutating commands per viewer per minute. Idempotent cancellation remains available at that limit and at the replay-cache capacity; overall frame limits still apply. No commands are queued for disconnected Macs. The phone sends an application heartbeat every 10 seconds; a 25-second viewer lease closes silent/dead sockets, clears approval, and notifies the Mac to cancel remote timers. Background browser suspension can therefore require reapproval.
- The browser disables controls on stale status and connection loss, never reports an optimistic state change, and allows cancellation while a prior command result is pending. Native shutdown/restart countdowns are canceled when remote permission or connectivity is lost.

## Release status

PROD gateway deployed and HTTPS/WSS smoke-tested with disposable synthetic status.
Local workerd integration: 12 checks, including opened-socket expiry. Native QR
round-trip and two create/revoke races tested. Security reviewer findings addressed.
Universal pika 1.1.0 (build 17) PKG prepared locally with existing ad-hoc signing.
Physical-phone acceptance remains pending. Public app release and update feed are
maintained by the repository release pipeline; see the main README for the current release.
