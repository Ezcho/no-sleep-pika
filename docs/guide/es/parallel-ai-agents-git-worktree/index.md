Source: https://no-sleep-pika.online/guide/es/parallel-ai-agents-git-worktree/
Language: es

MAC GUIDE · 2026-11-24

# ¿Dos agentes de IA editando los mismos archivos? Separa sus carpetas.

Con Git worktree, cada agente trabaja en su propia carpeta. Aprende a repartir tareas, revisar los cambios e integrarlos sin mezclar trabajo pendiente.

## El problema de compartir una carpeta

Un agente modifica la interfaz y otro escribe pruebas. Si comparten carpeta, leen y cambian los mismos archivos. Crear dos nombres de rama no crea dos copias independientes en esa carpeta. Cambiar de rama allí también cambia los archivos que utiliza el otro agente.

Git worktree añade otra carpeta de trabajo al mismo repositorio. Cada una tiene sus archivos y puede usar su propia rama, compartiendo el historial. Separa el trabajo pendiente, pero no garantiza que las modificaciones sean compatibles al integrarlas.

- 1 Separar carpetas

- 2 Asignar tareas

- 3 Revisar cambios

- 4 Integrar por turnos

## Prepara un punto de partida revisado

Ejecuta el siguiente comando en un proyecto Git existente. Debe haber al menos un commit: HEAD será el punto de partida. Si no hay salida, Git no informa de cambios ni archivos sin seguimiento; aún puede haber archivos ignorados.

Si aparece una lista, revísala y confirma solo los cambios deseados, o elige un commit existente. No añadas toda la carpeta a ciegas: puede contener secretos o trabajo ajeno. Las nuevas carpetas parten de HEAD, no de las ediciones sin confirmar.

```
git status --short
```

## Crea dos carpetas de trabajo

Ejecuta ambos comandos desde el proyecto original. Crean las ramas ai-ui y ai-tests y sus carpetas junto al proyecto. Los nombres y las rutas deben estar libres. Si ya existen, elige otros en lugar de forzar una sobrescritura.

Las dependencias instaladas, los archivos .env ignorados y los ajustes locales no se copian automáticamente. Sigue las instrucciones del proyecto, facilita solo las credenciales necesarias y usa puertos distintos para servidores simultáneos. Un worktree no es un entorno de seguridad aislado: una herramienta con permisos puede acceder a otras carpetas.

```
git worktree add -b ai-ui ../project-ai-ui HEAD
git worktree add -b ai-tests ../project-ai-tests HEAD
```

## Asigna carpeta y tarea

Abre un agente en project-ai-ui y otro en project-ai-tests. Indica la ruta absoluta y una tarea acotada: «modifica solo el componente visual» y «añade pruebas del comportamiento actual sin cambiar el código de la aplicación».

Asigna un responsable para archivos compartidos, como manifiestos de dependencias y archivos de bloqueo. Si ambos necesitan modificar el mismo archivo, trabaja por turnos. Pide una lista de archivos cambiados, comprobaciones realizadas y trabajo pendiente.

## Revisa e integra una rama cada vez

Ejecuta los tres comandos en cada carpeta. Status muestra cambios y archivos sin seguimiento. Diff muestra cambios no preparados en archivos seguidos; diff --cached muestra los preparados. Los archivos nuevos sin seguimiento no aparecen en estos diff: ábrelos por separado.

Ejecuta las comprobaciones pertinentes y confirma los cambios revisados en la rama de cada carpeta. Después vuelve al proyecto original e integra una rama cada vez en la rama de destino. Worktree no combina resultados automáticamente. Resuelve cualquier conflicto y comprueba el resultado conjunto antes de incorporar la siguiente rama.

```
git status --short
git diff
git diff --cached
```

## El papel de pika

pika ayuda a mantener el Mac despierto durante el trabajo local, según la configuración de sesión y sus protecciones. No reparte tareas, fusiona ramas ni resuelve conflictos. La conexión QR de pika 1.3 muestra el estado del Mac y controles de energía autorizados, no la salida de la IA ni un porcentaje fiable de finalización. Verifica los resultados del agente y las pruebas del proyecto.

[Descargar pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.3.0/pika-1.3.0.pkg) · [Ayuda de instalación](https://no-sleep-pika.online/install/)

Fuentes y alcance

Guía del creador de no-sleep-pika basada en la documentación oficial de Git. Se aplica a agentes genéricos, sin presuponer funciones o permisos de un producto concreto. Respeta también las normas del proyecto y el manejo de secretos.

- [Git · git-worktree](https://git-scm.com/docs/git-worktree)

- [Git · git-status](https://git-scm.com/docs/git-status)

- [Git · git-diff](https://git-scm.com/docs/git-diff)

Escrito por el creador de no-sleep-pika; incluye nuestra app.

[Cómo evitar que tu Mac se duerma: modo cerrado, caffeinate y pika →](https://no-sleep-pika.online/guide/es/keep-mac-awake/)[Markdown](https://no-sleep-pika.online/guide/es/parallel-ai-agents-git-worktree/index.md)
