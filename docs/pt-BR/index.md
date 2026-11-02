Source: https://no-sleep-pika.online/pt-BR/
Language: pt-BR

# Feche o Mac e mantenha suas tarefas rodando.

[Baixar para Mac](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.1.0/pika-1.1.0.pkg)

58 Downloads

Versão pública 1.1.0 · macOS 13+ · Apple Silicon e Intel

## Conectar MCP

STDIO

Instale e abra o pika, depois conecte com o comando abaixo. Novo: leia o QR para ver o estado do Mac no celular. [Ver código-fonte ↗](https://github.com/Ezcho/no-sleep-pika#mcp)

`/Applications/pika.app/Contents/MacOS/pika-mcp`

## Connect your agent to pika

Set up once on the same Mac. Your agent can then read status and control Session / Monitor.

### 1Prepare pika

Install the pika PKG, which includes the app and helper. Open pika from Applications and keep it running in the menu bar. [Installation help ↗](https://no-sleep-pika.online/install/)

### 2Add the MCP server

If Codex CLI is installed, paste this into Terminal once. The MCP client starts the server when it connects.

`codex mcp add pika -- /Applications/pika.app/Contents/MacOS/pika-mcp`

No Codex CLI? Use a configuration file

For Codex, add this section to ~/.codex/config.toml. If pika already exists, update it instead of adding a duplicate. Keep your other settings.

```
[mcp_servers.pika]
command = "/Applications/pika.app/Contents/MacOS/pika-mcp"
```

Other local MCP clients

Add a server named pika using STDIO. Set Command to the path below. Leave arguments and environment variables empty. No server URL or API key is required.

`/Applications/pika.app/Contents/MacOS/pika-mcp`

This is a local STDIO connection. The website address is not an MCP endpoint, and a cloud-only URL connector cannot run this Mac executable.

[Codex official documentation ↗](https://learn.chatgpt.com/docs/extend/mcp?surface=cli)

### 3Check the connection

Save, restart your MCP client, and open a new chat. Ask your agent:

`Call pika_status and show the current state. Do not change Session or Monitor.`

A successful pika_status tool result confirms the connection to the app. Session OFF is normal; helper registration alone does not confirm helper connectivity.

### What you can ask next

`pika_set_session` — Session ON / OFF
`pika_set_monitor` — Monitor ON / OFF · requires Session ON

Session ON prepares pika. Display policy applies only after the lid closes. With the lid open, Monitor changes only save your preference.

Closing the agent does not end a pika session. Turn Session OFF in pika or ask your agent to do so.

Phone monitoring · pika 1.1.0+

After updating, restart your MCP connection and ask: Create a pika QR. pika_remote_pair returns a text QR plus a PNG and HTML fallback. Scan with your phone camera and tap Connect. The QR is single-use and expires in 5 minutes; read-only access lasts up to 24 hours. It does not start Session. Revoke with pika_remote_revoke or the Mac menu. Never share the QR.

Connection not working?

No tools: confirm the command path and restart the client. App connection error: open pika on the same Mac and user account. Helper error: quit pika, reinstall the latest full PKG, and reopen pika. If Terminal says codex was not found, use the configuration-file option above.
