Source: https://no-sleep-pika.online/guide/ru/mac-locked-ai-running/
Language: ru

MAC GUIDE · 2026-10-05

# Mac заблокирован: продолжат ли работу Claude Code и Codex?

Разберитесь в блокировке, выключении экрана и сне при работе с локальными ИИ-задачами.

## Блокировка и сон

Экран пароля не доказывает остановку задачи. Фоновые команды могут выполняться, пока Mac бодрствует, приложение открыто и нужные соединения доступны. Управлению интерфейсом и авторизации может потребоваться разблокировка. После блокировки система может позднее уснуть. Не отключайте пароль.

## Локально или в облаке

Codex CLI работает с локальными файлами и командами; задачи Codex Cloud выполняются в другой среде. Claude Code Remote Control также подключается к локальной сессии. Переподключение не означает работу во время сна. pika не переносит задачи в облако.

[Codex CLI](https://learn.chatgpt.com/docs/codex/cli) · [Codex Cloud](https://learn.chatgpt.com/docs/cloud) · [Claude Code Remote Control](https://code.claude.com/docs/en/remote-control)

## Что проверить

Проверьте последнее сообщение: ожидание разрешения, вопрос, завершение или ошибка. Затем приложение, Wi-Fi, VPN и вход в аккаунт. Команды ниже только читают запросы питания и события; они не доказывают прогресс ИИ. Низкая загрузка CPU тоже не означает сбой.

```
pmset -g assertions
```

```
pmset -g log | tail -n 60
```

## Проверка за три минуты

С открытой крышкой запустите цикл, оставьте терминал открытым и заблокируйте экран примерно на три минуты. Сравните время и завершите Ctrl+C. Сопоставьте пропуски с журналом питания и результатами ИИ. Проверяется лишь простой процесс; закрытую крышку тестируйте отдельно.

```
while true; do date "+%Y-%m-%d %H:%M:%S"; sleep 10; done
```

## Настройка pika

Установите pika и вспомогательную службу, включите Session, оставьте Monitor OFF, если экран не нужен, и закройте крышку. Политика экрана применяется после закрытия. Session OFF снимает запрет сна без немедленного выключения экрана. Используйте питание и проветриваемый стол, не закрытую сумку. Защита или сбой службы могут остановить сессию.

[Скачать pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg) · [Помощь с установкой](https://no-sleep-pika.online/install/)

## Частые вопросы

Monitor OFF не завершает ИИ-задачу. tmux не предотвращает сон; caffeinate не решает проблемы сети и разрешений. Статус pika MCP не показывает ход всех задач ИИ.

Источники и рамки

Официальные источники и код pika проверены 5 октября 2026 года. Материал автора pika, без гарантии непрерывной работы на любом устройстве.

- [Apple · Sleep and wake settings](https://support.apple.com/guide/mac-help/set-sleep-and-wake-settings-mchle41a6ccd/mac)

- [OpenAI · Codex CLI](https://learn.chatgpt.com/docs/codex/cli)

- [OpenAI · Codex Cloud](https://learn.chatgpt.com/docs/cloud)

- [Anthropic · Claude Code Remote Control](https://code.claude.com/docs/en/remote-control)

[Если ИИ работает ночью, кто платит за электричество? →](https://no-sleep-pika.online/guide/ru/ai-overnight-electricity-cost/)

[Загрузка на MacBook остановилась: экран, сон или крышка? →](https://no-sleep-pika.online/guide/ru/macbook-downloads-stop/)

Материал разработчика no-sleep-pika с описанием собственного приложения.

[Скачать pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg)[Как не дать Mac уснуть: закрытая крышка, caffeinate и pika →](https://no-sleep-pika.online/guide/ru/keep-mac-awake/)[Markdown](https://no-sleep-pika.online/guide/ru/mac-locked-ai-running/index.md)
