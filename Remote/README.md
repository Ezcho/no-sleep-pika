# pika remote gateway

Read-only QR pairing for the native pika app. Cloudflare Workers + SQLite Durable
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
are tab-scoped sessionStorage. A lost claim response requires a new QR. No commands,
keyboard/mouse control, screen video, arbitrary IPC, AI outputs, or file access are
exposed. Those require a separate explicit authorization design.

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
xcrun swiftc -swift-version 5 -parse-as-library -module-cache-path .build/module-cache \
 Sources/Control/LocalControl.swift Sources/App/RemotePairing.swift \
 Tests/RemoteQR/main.swift -o .build/RemoteQRTests
.build/RemoteQRTests
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
- 4 sockets/room, pending auth 10 seconds, frames <=8 KiB, 30 JSON frames/min/socket.
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
- QR is a bearer invitation: whoever scans it first can read state. No identity proof
  is claimed. Remote writes are rejected at the server, not merely hidden in the UI.

## Release status

PROD gateway deployed and HTTPS/WSS smoke-tested with disposable synthetic status.
Local workerd integration: 12 checks, including opened-socket expiry. Native QR
round-trip and two create/revoke races tested. Security reviewer findings addressed.
Universal pika 1.1.0 (build 17) PKG prepared locally with existing ad-hoc signing.
Physical-phone acceptance remains pending. Public app release and update feed are
maintained by the repository release pipeline; see the main README for the current release.
