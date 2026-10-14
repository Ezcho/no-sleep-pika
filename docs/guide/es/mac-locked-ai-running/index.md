Source: https://no-sleep-pika.online/guide/es/mac-locked-ai-running/
Language: es

MAC GUIDE · 2026-10-05

# Mac bloqueado: ¿siguen trabajando Claude Code y Codex?

Distingue bloqueo, pantalla apagada y reposo antes de dejar una tarea de IA local con la tapa cerrada.

## Bloqueo y reposo

La pantalla de contraseña no demuestra que la tarea haya terminado. Los comandos en segundo plano pueden continuar si el Mac está despierto y la aplicación y sus conexiones siguen disponibles. La automatización visual o la autenticación pueden necesitar desbloqueo. El sistema puede entrar en reposo después de bloquearse; conserva la protección por contraseña.

## Local o nube

Codex CLI trabaja con archivos y comandos locales; una tarea delegada a Codex Cloud se ejecuta en otro entorno. Claude Code Remote Control sigue conectado a una sesión local. Reconectar no significa haber trabajado durante el reposo. pika no traslada tareas a la nube.

[Codex CLI](https://learn.chatgpt.com/docs/codex/cli) · [Codex Cloud](https://learn.chatgpt.com/docs/cloud) · [Claude Code Remote Control](https://code.claude.com/docs/en/remote-control)

## Qué revisar primero

Revisa el último mensaje: aprobación, pregunta, finalización o error. Comprueba después aplicación, Wi-Fi, VPN y sesión iniciada. Los comandos de consulta siguientes muestran solicitudes de energía y eventos; no prueban el progreso de la IA ni lo demuestra un uso bajo de CPU.

```
pmset -g assertions
```

```
pmset -g log | tail -n 60
```

## Prueba de tres minutos

Con la tapa abierta, ejecuta el bucle, deja la terminal abierta y bloquea unos tres minutos. Compara las horas y termina con Ctrl+C. Contrasta huecos con registros de energía y comprueba también los resultados de la IA. Solo verifica un proceso simple; prueba la tapa cerrada por separado.

```
while true; do date "+%Y-%m-%d %H:%M:%S"; sleep 10; done
```

## Configurar pika

Instala pika y su servicio auxiliar. Activa Session, deja Monitor OFF si no necesitas la pantalla y cierra la tapa. La política de pantalla se aplica al cerrarla. Session OFF libera la prevención del reposo sin apagar inmediatamente la pantalla. Usa alimentación y una mesa ventilada, nunca una bolsa cerrada. La protección o fallos del servicio pueden detener la sesión.

[Descargar pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg) · [Ayuda de instalación](https://no-sleep-pika.online/install/)

## Preguntas frecuentes

Monitor OFF no ordena terminar la IA. tmux no impide el reposo y caffeinate no soluciona aprobaciones ni fallos de red. El estado de pika MCP no refleja todos los trabajos de Claude Code o Codex.

Fuentes y alcance

Documentación oficial e implementación de pika revisadas el 5 de octubre de 2026. Guía del creador de pika, sin garantía de ejecución continua en todos los equipos.

- [Apple · Sleep and wake settings](https://support.apple.com/guide/mac-help/set-sleep-and-wake-settings-mchle41a6ccd/mac)

- [OpenAI · Codex CLI](https://learn.chatgpt.com/docs/codex/cli)

- [OpenAI · Codex Cloud](https://learn.chatgpt.com/docs/cloud)

- [Anthropic · Claude Code Remote Control](https://code.claude.com/docs/en/remote-control)

[Si la IA trabaja de noche, ¿quién paga la electricidad? →](https://no-sleep-pika.online/guide/es/ai-overnight-electricity-cost/)

[Descargas detenidas en MacBook: pantalla, reposo y tapa →](https://no-sleep-pika.online/guide/es/macbook-downloads-stop/)

Escrito por el creador de no-sleep-pika; incluye nuestra app.

[Descargar pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg)[Cómo evitar que tu Mac se duerma: modo cerrado, caffeinate y pika →](https://no-sleep-pika.online/guide/es/keep-mac-awake/)[Markdown](https://no-sleep-pika.online/guide/es/mac-locked-ai-running/index.md)
