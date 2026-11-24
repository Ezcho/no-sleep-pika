Source: https://no-sleep-pika.online/guide/pt-BR/parallel-ai-agents-git-worktree/
Language: pt-BR

MAC GUIDE · 2026-11-24

# Dois agentes de IA editando os mesmos arquivos? Separe as pastas.

Com Git worktree, cada agente ganha sua própria pasta. Divida tarefas, revise alterações e integre os resultados sem misturar trabalho inacabado.

## O risco de dividir a mesma pasta

Um agente ajusta a interface, outro escreve testes. Na mesma pasta, ambos leem e alteram os mesmos arquivos. Criar dois nomes de branch não cria duas cópias independentes ali. Trocar a branch também muda os arquivos usados pelo outro agente.

Git worktree adiciona outra pasta de trabalho ao mesmo repositório. Cada pasta pode ter sua branch e seus arquivos, compartilhando o histórico. Isso separa o trabalho em andamento, mas não elimina possíveis conflitos na integração.

- 1 Separar pastas

- 2 Distribuir tarefas

- 3 Revisar alterações

- 4 Integrar por etapas

## Prepare um ponto de partida revisado

Execute o comando abaixo no projeto Git existente. É necessário pelo menos um commit: HEAD indica esse ponto de partida. Saída vazia significa que não foram relatadas alterações ou arquivos não rastreados; arquivos ignorados ainda podem existir.

Se aparecer uma lista, revise-a e faça commit apenas das mudanças desejadas, ou escolha um commit existente. Não adicione a pasta inteira sem conferir: segredos e trabalho sem relação devem ficar de fora. As novas pastas partem de HEAD, não das edições sem commit.

```
git status --short
```

## Crie duas pastas de trabalho

Execute os dois comandos no projeto original. Eles criam ai-ui e ai-tests e pastas ao lado do projeto. Os nomes de branch e os caminhos precisam estar livres. Se já existirem, escolha outros, sem forçar substituições.

Dependências instaladas, arquivos .env ignorados e ajustes locais não são todos copiados. Prepare o necessário conforme o projeto, forneça apenas as credenciais exigidas e use portas diferentes para servidores simultâneos. Worktree não é uma barreira de segurança: ferramentas com permissão podem acessar outras pastas.

```
git worktree add -b ai-ui ../project-ai-ui HEAD
git worktree add -b ai-tests ../project-ai-tests HEAD
```

## Defina pasta e responsabilidade

Abra um agente em project-ai-ui e outro em project-ai-tests. Informe o caminho absoluto e uma tarefa limitada: “alterar apenas o componente visual” e “adicionar testes do comportamento atual, sem mudar o código da aplicação”.

Defina quem cuida de arquivos compartilhados, como listas de dependências e arquivos de lock. Se ambos precisarem mudar o mesmo arquivo, trabalhe em sequência. Peça um resumo dos arquivos alterados, verificações realizadas e pendências.

## Revise e integre uma branch por vez

Execute os três comandos em cada pasta. Status lista mudanças e arquivos não rastreados. Diff mostra alterações ainda não preparadas em arquivos rastreados; diff --cached mostra as preparadas. Arquivos novos não rastreados não aparecem nesses diffs: abra-os separadamente.

Execute as verificações do projeto e faça commit das mudanças revisadas na respectiva branch. Volte ao projeto original e revise e integre uma branch por vez na branch de destino. Worktree não combina resultados automaticamente. Resolva conflitos e verifique o resultado conjunto antes de integrar a próxima.

```
git status --short
git diff
git diff --cached
```

## Onde o pika ajuda

O pika pode manter o Mac acordado durante o trabalho local, conforme as configurações de sessão e as proteções. Ele não distribui tarefas, faz merges ou resolve conflitos. O QR do pika 1.3 mostra o estado do Mac e controles de energia autorizados, não a saída da IA ou uma porcentagem confiável de conclusão. Confira os resultados do agente e os testes do projeto.

[Baixar pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.3.0/pika-1.3.0.pkg) · [Ajuda de instalação](https://no-sleep-pika.online/install/)

Fontes e escopo

Guia do criador do no-sleep-pika baseado na documentação oficial do Git. Trata de agentes genéricos, sem presumir recursos ou permissões de um produto. Siga também as regras do projeto e de proteção de segredos.

- [Git · git-worktree](https://git-scm.com/docs/git-worktree)

- [Git · git-status](https://git-scm.com/docs/git-status)

- [Git · git-diff](https://git-scm.com/docs/git-diff)

Escrito pelo criador de no-sleep-pika; inclui nosso app.

[Como manter o Mac acordado: modo clamshell, caffeinate e pika →](https://no-sleep-pika.online/guide/pt-BR/keep-mac-awake/)[Markdown](https://no-sleep-pika.online/guide/pt-BR/parallel-ai-agents-git-worktree/index.md)
