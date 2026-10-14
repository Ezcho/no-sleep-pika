Source: https://no-sleep-pika.online/guide/mac-locked-ai-running/
Language: en

MAC GUIDE · 2026-10-05

# Mac locked: will Claude Code and Codex keep working?

Locking the screen, turning off the display and sleeping the Mac are different. Check local AI progress, approvals and network access before leaving a closed MacBook running.

## Locking is not the same as stopping

A password screen does not prove that an AI task stopped. Ordinary background commands can continue while the Mac remains awake, the app stays open and required services remain available. Screen-driven automation or authentication steps can still need an unlocked session. Keep the screen lock enabled.

Display sleep only describes the screen; system sleep affects execution. A Mac can lock first and sleep later. Apple provides a setting on supported configurations to prevent automatic sleep on power while the display is off. Do not treat that as a universal closed-lid override.

## Local session or cloud task?

Codex CLI reads files and runs commands locally. A task explicitly delegated to Codex Cloud runs in a separate cloud environment. Server-side model inference does not move local tools into the cloud.

Claude Code Remote Control connects to a session on your computer. Its documented reconnection behavior does not mean local commands ran during sleep. Independently hosted cloud tasks may not need your Mac awake; steps depending on local files or MCP servers do. pika does not migrate AI work to the cloud.

[Codex CLI](https://learn.chatgpt.com/docs/codex/cli) · [Codex Cloud](https://learn.chatgpt.com/docs/cloud) · [Claude Code Remote Control](https://code.claude.com/docs/en/remote-control)

## Check these causes first

Read the last agent message for approval requests, questions, completion or errors. Then check that the app or terminal is still running and that Wi-Fi, VPN and authentication remain available. Preventing sleep does not fix API failures or usage limits.

The read-only commands below show current power assertions and recent power events. An assertion is a request to prevent a kind of sleep, not proof that an AI task finished. Compare timestamps with the actual task log. Low CPU use alone is not evidence of failure.

```
pmset -g assertions
```

```
pmset -g log | tail -n 60
```

## A three-minute check

With the lid open, run the loop below in a terminal you leave open. Lock the screen for about three minutes, unlock and compare the timestamps. Stop the loop with Ctrl+C. Investigate large gaps alongside power logs.

This only checks a simple local process, not AI requests or approvals. Also inspect task output and file modification times. Test lid closure separately under the same power and network conditions; an open-lid result does not establish closed-lid behavior. This is a procedure for your own device, not a claimed hardware benchmark.

```
while true; do date "+%Y-%m-%d %H:%M:%S"; sleep 10; done
```

## Using pika with the lid closed

Install pika and its helper, prepare Session ON, leave Monitor OFF if display retention is unnecessary, then close the lid. In the current design, open-lid toggles do not immediately blank the display; the display policy is applied after lid closure. Monitor OFF is not an instruction to end your AI task and does not disable macOS locking.

Session OFF releases sleep prevention and shows Monitor OFF without immediately blanking the screen. Battery or thermal protection and helper failures can stop a session. Start with power connected on a ventilated desk, never rely on operation inside a closed bag, and turn Session OFF when finished. pika cannot guarantee connectivity or task completion.

[Download pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg) · [Installation help](https://no-sleep-pika.online/install/)

## Common questions

Does a locked screen mean failure? No: check real progress, and distinguish ordinary commands from GUI or authentication steps. Does tmux or caffeinate solve everything? No: terminal persistence and power assertions do not solve system sleep in every lid state, approvals or network failures.

Does an MCP connection prove the agent is working? No. pika status describes pika, not the complete progress of every Claude Code or Codex task, and it does not automatically approve actions.

Sources and scope

Checked against official documentation and current pika source on October 5, 2026. Behavior varies by app and macOS version. This guide is written by the pika maker; use the sources and the linked sleep-prevention comparison for additional context.

- [Apple · Sleep and wake settings](https://support.apple.com/guide/mac-help/set-sleep-and-wake-settings-mchle41a6ccd/mac)

- [OpenAI · Codex CLI](https://learn.chatgpt.com/docs/codex/cli)

- [OpenAI · Codex Cloud](https://learn.chatgpt.com/docs/cloud)

- [Anthropic · Claude Code Remote Control](https://code.claude.com/docs/en/remote-control)

[Who pays the electricity bill when AI works overnight? →](https://no-sleep-pika.online/guide/ai-overnight-electricity-cost/)

[MacBook downloads stop: screen off, sleep or a closed lid? →](https://no-sleep-pika.online/guide/macbook-downloads-stop/)

Written by the maker of no-sleep-pika; this comparison includes our own app.

[Download pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg)[How to keep your Mac awake: clamshell mode, caffeinate and pika →](https://no-sleep-pika.online/guide/keep-mac-awake/)[Markdown](https://no-sleep-pika.online/guide/mac-locked-ai-running/index.md)
