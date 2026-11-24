Source: https://no-sleep-pika.online/guide/pt-BR/control-mac-from-phone-qr/
Language: pt-BR

MAC GUIDE · 2026-11-23

# Controle o Mac por QR: sessões, temporizadores e desligamento pelo celular

O pika 1.3.0 permite controlar Session e energia pelo celular depois de autorizar a conexão no Mac.

## Além de consultar o estado

Deixe uma compilação ou download no Mac e use o celular para mudar Session, programar um temporizador ou solicitar desligamento e reinício. O pika 1.3.0 acrescenta controles à página do QR.

Ele não envia novas instruções a agentes de IA nem mostra conversas, saída do terminal, porcentagem de progresso ou área de trabalho remota.

## Atualize primeiro o aplicativo do Mac

Mantenha o pika 1.3.0 ou mais recente aberto no Mac. Evitar repouso com a tampa fechada exige um serviço auxiliar funcionando. Os dois aparelhos precisam de internet.

Se o macOS não verificar o desenvolvedor, confira a origem oficial do arquivo. Depois de tentar abri-lo, use Ajustes do Sistema → Privacidade e Segurança → Abrir Mesmo Assim para esse arquivo e siga a confirmação do sistema. Os nomes variam; veja o guia de instalação. Não desative a segurança geral nem use esse procedimento para avisos de malware ou arquivo danificado.

[Baixar pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.3.0/pika-1.3.0.pkg) · [Ajuda de instalação](https://no-sleep-pika.online/install/)

## Escaneie e autorize no Mac

Peça um QR do pika no chat de IA conectado às ferramentas pika por MCP. Escaneie com a câmera em até cinco minutos e toque para conectar ao Mac. O QR só funciona uma vez; o acesso inicial é de leitura e não liga Session.

Peça permissão de controle no celular e aceite o aviso no Mac. Faça isso antes de sair, com os dois aparelhos à vista. Sem aprovação no Mac não há controle. A página inicial explica como conectar o MCP se for sua primeira vez.

Os botões do celular estão em coreano: “이 Mac에 연결” conecta, “Mac에 제어 허용 요청” pede controle e depois você autoriza no Mac. “예약·카운트다운 취소” cancela o temporizador. O guia abaixo explica a primeira conexão MCP.

[Guia de conexão MCP →](https://no-sleep-pika.online/pt-BR/#mcp)

## O que pode ser controlado

Session ativa ou libera a prevenção de repouso. Monitor só muda com Session ON; no modo de tampa fechada, a configuração de tela é aplicada ao fechar a tampa. O valor Monitor é a configuração solicitada, não uma verificação da tela física.

Escolha manter apenas na tomada, liberar ao desconectar o carregador ou com 30, 40 ou 50% de bateria. As proteções existentes continuam. O calor é um nível do macOS, não uma medida em °C.

## Temporizadores e 60 segundos para cancelar

Escolha 15, 30, 60, 180 ou 360 minutos para liberar Session, repousar, desligar ou reiniciar. Liberar Session não fecha os aplicativos à força.

Desligar ou reiniciar imediatamente exige confirmação e começa uma contagem regressiva cancelável de 60 segundos. Use o botão de cancelar agendamento/contagem. O pika restaura as configurações de repouso antes da solicitação. Documentos não salvos podem atrasar ou cancelar a ação: enviado não significa concluído.

## A permissão acompanha a conexão

A permissão vale para a conexão aprovada atual. Desconectar ou revogar cancela temporizadores remotos e contagens; uma nova conexão exige nova aprovação. O acesso dura no máximo 24 horas a partir da emissão do QR. Os temporizadores não continuam se o pika sair ou o Mac entrar em repouso.

Detectar uma desconexão pode levar dezenas de segundos. Para impedir o desligamento, pressione “예약·카운트다운 취소” e confira o cancelamento, em vez de apenas desconectar. Temporizadores remotos precisam de sinais contínuos do navegador; colocá-lo em segundo plano pode desconectar e cancelar o temporizador.

Não compartilhe o QR. Teste primeiro uma alteração simples de Session e o cancelamento. Dados antigos em uma página desconectada não provam que o Mac desligou. Não há garantia de rede ou conclusão de tarefas de IA.

Fontes e escopo

Guia do criador do no-sleep-pika sobre o próprio aplicativo 1.3.0, escrito em 23 de novembro de 2026. Consulte também a orientação oficial da Apple sobre avisos de instalação.

- [pika 1.3.0 · Release notes](https://github.com/Ezcho/no-sleep-pika/releases/tag/v1.3.0)

- [pika · Remote connection and permissions](https://github.com/Ezcho/no-sleep-pika/blob/v1.3.0/Remote/README.md)

- [Apple · Safely open apps on your Mac](https://support.apple.com/en-us/102445)

[Dois agentes de IA editando os mesmos arquivos? Separe as pastas. →](https://no-sleep-pika.online/guide/pt-BR/parallel-ai-agents-git-worktree/)

Escrito pelo criador de no-sleep-pika; inclui nosso app.

[Baixar pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.3.0/pika-1.3.0.pkg)[Como manter o Mac acordado: modo clamshell, caffeinate e pika →](https://no-sleep-pika.online/guide/pt-BR/keep-mac-awake/)[Markdown](https://no-sleep-pika.online/guide/pt-BR/control-mac-from-phone-qr/index.md)
