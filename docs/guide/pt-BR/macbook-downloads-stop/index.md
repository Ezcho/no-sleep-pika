Source: https://no-sleep-pika.online/guide/pt-BR/macbook-downloads-stop/
Language: pt-BR

MAC GUIDE · 2026-10-15

# Download parado no MacBook: tela, repouso ou tampa?

Confira rede e armazenamento antes de usar caffeinate ou pika.

## Quando parou

Veja pausa, erro de rede, espaço e login no aplicativo. Se falha durante o uso, confira Wi-Fi, VPN e servidor. Evitar repouso não recupera links expirados.

## Tela e repouso

Tela apagada não significa sistema dormindo. A transferência pode continuar, mas o repouso automático pode ocorrer depois do bloqueio. Confira a opção de manter acordado na tomada, se disponível. Mantenha a senha.

## caffeinate com tampa aberta

O comando abaixo solicita uma hora sem repouso por inatividade. Deixe o terminal aberto e baixe no aplicativo habitual. Ctrl+C encerra antes; -t usa segundos, -i é do sistema e -d da tela. Não garante rede nem impede todo tipo de repouso.

```
caffeinate -i -t 3600
```

```
man caffeinate
```

## Condições ao fechar

Com monitor externo, confira energia, teclado, mouse e suporte do modelo. Só o carregador não completa essa configuração. Sem monitor externo, teste uma transferência curta e compare bytes antes e depois de fechar.

## Baixar com pika

Prepare pika e o serviço auxiliar, inicie o download, ligue Session e deixe Monitor OFF se não precisar da tela. Feche a tampa para aplicar a política de tela. Termine com Session OFF. Use energia e mesa ventilada, nunca bolsa fechada. Proteção ou falhas podem parar a sessão.

[Baixar pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg) · [Ajuda de instalação](https://no-sleep-pika.online/install/)

## Verificar o resultado

Confira conclusão, tamanho e checksum fornecido. Retome pelas funções do aplicativo. pika não recupera a rede nem detecta o fim; apagar a tela não garante mais velocidade.

Fontes

Verificado em 11 de outubro de 2026 com Apple, caffeinate(8) e código pika. Guia do criador de pika.

- [Apple · Sleep and wake settings](https://support.apple.com/guide/mac-help/set-sleep-and-wake-settings-mchle41a6ccd/mac)

- [Apple · External displays](https://support.apple.com/en-us/102501)

- `man caffeinate` · macOS System Manager’s Manual

[Se a IA trabalha à noite, quem paga a eletricidade? →](https://no-sleep-pika.online/guide/pt-BR/ai-overnight-electricity-cost/)

Escrito pelo criador de no-sleep-pika; inclui nosso app.

[Baixar pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg)[Como manter o Mac acordado: modo clamshell, caffeinate e pika →](https://no-sleep-pika.online/guide/pt-BR/keep-mac-awake/)[Markdown](https://no-sleep-pika.online/guide/pt-BR/macbook-downloads-stop/index.md)
