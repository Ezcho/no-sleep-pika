Source: https://no-sleep-pika.online/guide/control-mac-from-phone-qr/
Language: en

MAC GUIDE · 2026-11-23

# Control your Mac with a QR code: sessions, timers and shutdown from your phone

Choose when your Mac keeps working and when it rests. Learn how pika 1.3.0 pairs your phone, asks for Mac approval and limits remote control.

## Go beyond checking status

You left a build or download running on your Mac and moved to another room. With pika 1.3.0, the QR dashboard can do more than show status: you can change Session, set a timer, or request shutdown and restart.

This controls pika and Mac power actions. It does not send instructions to an AI agent or show its conversation, terminal output, progress percentage or screen.

## Update the Mac app first

Update pika on the Mac to 1.3.0 or later and leave it running. Closed-lid sleep prevention needs a working helper service. Both devices need an internet connection.

If macOS cannot verify the developer, first check that the file came from the official site. After trying to open it, use System Settings → Privacy & Security → Open Anyway for that file, then follow macOS confirmation and authentication. Labels vary by OS. Use the installation guide below; do not disable system-wide security.

Warnings about malware or a damaged file are different; do not use this opening exception for those alerts.

[Download pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.3.0/pika-1.3.0.pkg) · [Installation help](https://no-sleep-pika.online/install/)

## Scan, then approve on your Mac

In an AI chat with pika MCP connected, ask for a pika QR. Scan it with your phone camera and connect within five minutes. It is single-use. Pairing initially gives read-only access and does not turn Session on.

Request remote control on the phone, then approve the prompt on the Mac. Do this before leaving, while you can see both devices. Without Mac approval, the phone cannot control it.

The phone buttons currently read “이 Mac에 연결” (connect), then “Mac에 제어 허용 요청” (request control). Approve on the Mac. “예약·카운트다운 취소” cancels a timer or countdown. New to pika MCP? Follow the connection guide linked below first.

[MCP connection guide →](https://no-sleep-pika.online/#mcp)

## What the phone can control

Session enables or releases sleep prevention. Monitor is available only while Session is on; in closed-lid mode its prepared display policy applies after lid closure. The Monitor value is a requested setting, not a camera view of the physical display.

Power conditions can require external power, release Session when the charger disconnects, or stop at 30, 40 or 50% battery. Existing battery and thermal protections still apply. Heat is a macOS level, not a Celsius reading.

## Timers and a 60-second cancellation window

Choose a 15-, 30-, 60-, 180- or 360-minute timer, then choose Session release, sleep, shutdown or restart. Releasing Session ends sleep prevention; it does not force-close your apps.

An immediate shutdown or restart request asks for confirmation and starts a 60-second countdown on the Mac. Cancel the timer if you change your mind. pika first restores its sleep settings, then asks macOS to act. Unsaved-document prompts may delay or cancel shutdown. A request sent is not proof that it completed.

## Access ends with the connection

Control belongs to the currently approved connection. Disconnecting or revoking permission cancels remote timers and countdowns; a new connection needs approval again. Access lasts at most 24 hours from QR issuance. Timers do not continue through pika exit or Mac sleep.

Detecting a lost connection can take tens of seconds. To prevent shutdown, use “예약·카운트다운 취소” and check the canceled state instead of disconnecting. Remote timers need continuing browser connection signals; moving the browser into the background may disconnect it and cancel the timer.

Keep the QR private. Before leaving, try a harmless Session change and timer cancellation. A disconnected page may show its last known values, not proof of shutdown. Sleep prevention cannot guarantee network connectivity or an AI job’s completion.

Sources and scope

Written by the no-sleep-pika maker on November 23, 2026, for pika 1.3.0. This is a guide to our own app. See Apple’s guidance for installation alerts and current settings names.

- [pika 1.3.0 · Release notes](https://github.com/Ezcho/no-sleep-pika/releases/tag/v1.3.0)

- [pika · Remote connection and permissions](https://github.com/Ezcho/no-sleep-pika/blob/v1.3.0/Remote/README.md)

- [Apple · Safely open apps on your Mac](https://support.apple.com/en-us/102445)

[Two AI agents editing the same files? Give them separate folders. →](https://no-sleep-pika.online/guide/parallel-ai-agents-git-worktree/)

Written by the maker of no-sleep-pika; this comparison includes our own app.

[Download pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.3.0/pika-1.3.0.pkg)[How to keep your Mac awake: clamshell mode, caffeinate and pika →](https://no-sleep-pika.online/guide/keep-mac-awake/)[Markdown](https://no-sleep-pika.online/guide/control-mac-from-phone-qr/index.md)
