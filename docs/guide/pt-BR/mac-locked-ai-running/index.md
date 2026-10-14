Source: https://no-sleep-pika.online/guide/pt-BR/mac-locked-ai-running/
Language: pt-BR

MAC GUIDE · 2026-10-05

# Mac bloqueado: Claude Code e Codex continuam trabalhando?

Entenda bloqueio, tela apagada e repouso ao acompanhar tarefas locais de IA.

## Bloqueio não é repouso

A tela de senha não comprova que o trabalho parou. Comandos em segundo plano podem continuar com o Mac acordado, aplicativo aberto e conexões disponíveis. Automação visual e autenticação podem exigir desbloqueio. O repouso pode ocorrer depois do bloqueio. Mantenha a proteção por senha.

## Local ou nuvem

Codex CLI usa arquivos e comandos locais; tarefas delegadas ao Codex Cloud executam em outro ambiente. Claude Code Remote Control ainda conecta uma sessão local. Reconectar não significa executar durante o repouso. pika não transfere tarefas à nuvem.

[Codex CLI](https://learn.chatgpt.com/docs/codex/cli) · [Codex Cloud](https://learn.chatgpt.com/docs/cloud) · [Claude Code Remote Control](https://code.claude.com/docs/en/remote-control)

## O que verificar

Leia a última mensagem: aprovação, pergunta, conclusão ou erro. Depois confira aplicativo, Wi-Fi, VPN e login. Os comandos de leitura abaixo mostram solicitações de energia e eventos, não o progresso da IA. CPU baixa também não prova falha.

```
pmset -g assertions
```

```
pmset -g log | tail -n 60
```

## Teste de três minutos

Com a tampa aberta, execute o loop, mantenha o terminal e bloqueie por cerca de três minutos. Compare horários e encerre com Ctrl+C. Confira lacunas nos registros de energia e os resultados da IA. Isso testa apenas um processo simples; teste a tampa fechada separadamente.

```
while true; do date "+%Y-%m-%d %H:%M:%S"; sleep 10; done
```

## Configurar pika

Instale pika e o serviço auxiliar, ligue Session, mantenha Monitor OFF se não precisar da tela e feche a tampa. A política de tela é aplicada ao fechar. Session OFF libera o repouso sem apagar imediatamente a tela. Use energia e mesa ventilada, nunca bolsa fechada. Proteções ou falhas do serviço podem parar a sessão.

[Baixar pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg) · [Ajuda de instalação](https://no-sleep-pika.online/install/)

## Perguntas comuns

Monitor OFF não encerra a IA. tmux não impede o repouso; caffeinate não resolve rede nem aprovações. O estado de pika MCP não representa todos os trabalhos de IA.

Fontes e escopo

Fontes oficiais e implementação verificadas em 5 de outubro de 2026. Guia do criador de pika, sem garantia de execução contínua em todos os dispositivos.

- [Apple · Sleep and wake settings](https://support.apple.com/guide/mac-help/set-sleep-and-wake-settings-mchle41a6ccd/mac)

- [OpenAI · Codex CLI](https://learn.chatgpt.com/docs/codex/cli)

- [OpenAI · Codex Cloud](https://learn.chatgpt.com/docs/cloud)

- [Anthropic · Claude Code Remote Control](https://code.claude.com/docs/en/remote-control)

[Se a IA trabalha à noite, quem paga a eletricidade? →](https://no-sleep-pika.online/guide/pt-BR/ai-overnight-electricity-cost/)

[Download parado no MacBook: tela, repouso ou tampa? →](https://no-sleep-pika.online/guide/pt-BR/macbook-downloads-stop/)

Escrito pelo criador de no-sleep-pika; inclui nosso app.

[Baixar pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg)[Como manter o Mac acordado: modo clamshell, caffeinate e pika →](https://no-sleep-pika.online/guide/pt-BR/keep-mac-awake/)[Markdown](https://no-sleep-pika.online/guide/pt-BR/mac-locked-ai-running/index.md)
