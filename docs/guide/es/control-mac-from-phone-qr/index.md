Source: https://no-sleep-pika.online/guide/es/control-mac-from-phone-qr/
Language: es

MAC GUIDE · 2026-11-23

# Controla tu Mac con un QR: sesiones, temporizadores y apagado desde el móvil

pika 1.3.0 permite controlar Session y las opciones de energía desde el móvil, después de aprobar la conexión en el Mac.

## Más que consultar el estado

Deja una compilación o descarga en el Mac y cambia Session, programa un temporizador o solicita apagar y reiniciar desde el móvil. pika 1.3.0 añade controles a la página de estado QR.

No envía nuevas instrucciones a un agente de IA ni muestra conversaciones, salida del terminal, porcentaje de avance o escritorio remoto.

## Actualiza primero la app del Mac

Abre pika 1.3.0 o posterior en el Mac. Evitar el reposo con la tapa cerrada requiere un servicio auxiliar operativo. Ambos dispositivos necesitan internet.

Si macOS no verifica al desarrollador, comprueba que el archivo procede del sitio oficial. Tras intentar abrirlo, entra en Ajustes del Sistema → Privacidad y seguridad → Abrir igualmente para ese archivo y sigue la confirmación del sistema. Los nombres varían; consulta la guía de instalación. No desactives la seguridad global.

Los avisos de malware o archivo dañado son distintos; no uses esta excepción para ellos.

[Descargar pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.3.0/pika-1.3.0.pkg) · [Ayuda de instalación](https://no-sleep-pika.online/install/)

## Escanea y autoriza en el Mac

Pide un QR de pika en un chat de IA conectado a pika MCP. Escanéalo con la cámara del móvil en cinco minutos: es de un solo uso. La conexión comienza en modo lectura y no activa Session.

Solicita control en el móvil y acepta el aviso del Mac. Hazlo antes de salir, con ambos dispositivos delante. Sin aprobación en el Mac, no hay control.

Los botones del móvil están actualmente en coreano: “이 Mac에 연결” conecta, “Mac에 제어 허용 요청” solicita control y después autorizas en el Mac. “예약·카운트다운 취소” cancela el temporizador. Para conectar MCP por primera vez, usa la guía siguiente.

[Guía de conexión MCP →](https://no-sleep-pika.online/es/#mcp)

## Qué puedes controlar

Session activa o libera la prevención del reposo. Monitor solo se cambia con Session ON; la política de pantalla del modo de tapa cerrada se aplica al cerrar la tapa. Su valor expresa la opción solicitada, no el estado físico comprobado de la pantalla.

Puedes exigir alimentación externa, liberar Session al desconectar el cargador o al llegar al 30, 40 o 50% de batería. Las protecciones existentes siguen vigentes. El calor se muestra como nivel de macOS, no en °C.

## Temporizadores y 60 segundos para cancelar

Programa 15, 30, 60, 180 o 360 minutos y elige liberar Session, reposo, apagado o reinicio. Liberar Session no fuerza el cierre de las aplicaciones.

El apagado o reinicio inmediato pide confirmación e inicia una cuenta atrás cancelable de 60 segundos. pika restaura primero sus ajustes de reposo. Un documento sin guardar puede retrasar o cancelar la acción: solicitud enviada no significa acción completada.

## El permiso termina con la conexión

El permiso corresponde a la conexión aprobada actual. Desconectar o revocar cancela los temporizadores remotos y la cuenta atrás; una conexión nueva necesita otra aprobación. El acceso dura hasta 24 horas desde la emisión del QR. Los temporizadores no continúan al salir de pika o entrar el Mac en reposo.

Detectar una desconexión puede tardar decenas de segundos. Para evitar el apagado, pulsa “예약·카운트다운 취소” y confirma el estado cancelado, en lugar de desconectar. Los temporizadores remotos necesitan señales continuas del navegador; pasar este a segundo plano puede cortar la conexión y cancelar el temporizador.

No compartas el QR. Prueba primero un cambio de Session y la cancelación con tareas sin importancia. Una página desconectada puede mostrar datos antiguos, no demostrar que el Mac se apagó. No se garantiza la red ni la finalización de tareas de IA.

Fuentes y alcance

Guía del creador de no-sleep-pika sobre su aplicación 1.3.0, escrita el 23 de noviembre de 2026. Consulta también la documentación oficial de Apple sobre avisos de instalación.

- [pika 1.3.0 · Release notes](https://github.com/Ezcho/no-sleep-pika/releases/tag/v1.3.0)

- [pika · Remote connection and permissions](https://github.com/Ezcho/no-sleep-pika/blob/v1.3.0/Remote/README.md)

- [Apple · Safely open apps on your Mac](https://support.apple.com/en-us/102445)

[¿Dos agentes de IA editando los mismos archivos? Separa sus carpetas. →](https://no-sleep-pika.online/guide/es/parallel-ai-agents-git-worktree/)

Escrito por el creador de no-sleep-pika; incluye nuestra app.

[Descargar pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.3.0/pika-1.3.0.pkg)[Cómo evitar que tu Mac se duerma: modo cerrado, caffeinate y pika →](https://no-sleep-pika.online/guide/es/keep-mac-awake/)[Markdown](https://no-sleep-pika.online/guide/es/control-mac-from-phone-qr/index.md)
