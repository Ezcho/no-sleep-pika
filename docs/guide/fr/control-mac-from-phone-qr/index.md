Source: https://no-sleep-pika.online/guide/fr/control-mac-from-phone-qr/
Language: fr

MAC GUIDE · 2026-11-23

# Contrôlez votre Mac avec un QR : sessions, minuteurs et extinction depuis le téléphone

pika 1.3.0 permet de gérer Session et l’alimentation depuis votre téléphone après une autorisation sur le Mac.

## Au-delà de la consultation

Laissez une compilation ou un téléchargement sur le Mac et utilisez votre téléphone pour changer Session, régler un minuteur ou demander l’extinction et le redémarrage. pika 1.3.0 ajoute des commandes à la page QR.

Il ne transmet pas de consignes à un agent IA et n’affiche ni conversations, ni sortie du terminal, ni progression du travail, ni bureau distant.

## Mettez d’abord le Mac à jour

Gardez pika 1.3.0 ou une version ultérieure ouvert sur le Mac. Le maintien éveillé avec le capot fermé nécessite un service auxiliaire fonctionnel. Les deux appareils ont besoin d’internet.

Si macOS ne peut pas vérifier le développeur, vérifiez la provenance officielle du fichier. Après avoir essayé de l’ouvrir, allez dans Réglages Système → Confidentialité et sécurité → Ouvrir quand même pour ce fichier, puis confirmez dans macOS. Les intitulés varient : consultez le guide d’installation sans désactiver la protection générale.

Les alertes de logiciel malveillant ou de fichier endommagé sont différentes : n’utilisez pas cette exception pour les contourner.

[Télécharger pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.3.0/pika-1.3.0.pkg) · [Aide à l’installation](https://no-sleep-pika.online/install/)

## Scannez puis autorisez sur le Mac

Demandez un QR pika dans un chat IA relié à pika MCP. Scannez-le avec l’appareil photo du téléphone dans les cinq minutes. Il est à usage unique. La connexion débute en lecture seule et n’active pas Session.

Demandez le contrôle sur le téléphone, puis acceptez sur le Mac. Faites-le avant de partir, avec les deux appareils devant vous. Sans accord sur le Mac, aucune commande n’est autorisée.

Les boutons du téléphone sont actuellement en coréen : “이 Mac에 연결” pour connecter, puis “Mac에 제어 허용 요청” pour demander le contrôle, avant d’accepter sur le Mac. “예약·카운트다운 취소” annule le minuteur. Le guide ci-dessous explique la première connexion MCP.

[Guide de connexion MCP →](https://no-sleep-pika.online/fr/#mcp)

## Les commandes disponibles

Session active ou libère le maintien éveillé. Monitor n’est modifiable que lorsque Session est ON ; sa politique d’affichage en mode capot fermé s’applique à la fermeture. Sa valeur représente le réglage demandé, pas une vérification physique de l’écran.

Vous pouvez exiger le secteur, libérer Session au débranchement ou à 30, 40 ou 50% de batterie. Les protections existantes restent actives. La chaleur est un niveau macOS, pas une température en °C.

## Minuteurs et 60 secondes pour annuler

Réglez 15, 30, 60, 180 ou 360 minutes, puis choisissez libération de Session, veille, extinction ou redémarrage. Libérer Session ne ferme pas les applications de force.

Une demande immédiate d’extinction ou de redémarrage exige une confirmation, puis lance un décompte annulable de 60 secondes. pika restaure d’abord ses réglages de veille. Un document non enregistré peut retarder ou annuler l’opération : envoyé ne veut pas dire terminé.

## La permission suit la connexion

L’autorisation concerne la connexion actuelle. Une déconnexion ou une révocation annule les minuteurs distants et le décompte ; il faut approuver une nouvelle connexion. L’accès dure au maximum 24 heures depuis la création du QR. Les minuteurs ne persistent pas après fermeture de pika ou mise en veille du Mac.

La détection d’une coupure peut prendre plusieurs dizaines de secondes. Pour empêcher l’extinction, utilisez “예약·카운트다운 취소” et vérifiez l’annulation plutôt que de vous déconnecter. Les minuteurs distants exigent des signaux réguliers du navigateur ; le passage en arrière-plan peut couper la connexion et annuler le minuteur.

Ne partagez pas le QR. Testez d’abord Session et l’annulation sur une tâche sans importance. Des données anciennes après déconnexion ne prouvent pas que le Mac est éteint. Le réseau et la fin d’un travail IA ne sont pas garantis.

Sources et portée

Guide de l’auteur de no-sleep-pika sur sa propre application 1.3.0, rédigé le 23 novembre 2026. Consultez aussi Apple pour les avertissements d’installation.

- [pika 1.3.0 · Release notes](https://github.com/Ezcho/no-sleep-pika/releases/tag/v1.3.0)

- [pika · Remote connection and permissions](https://github.com/Ezcho/no-sleep-pika/blob/v1.3.0/Remote/README.md)

- [Apple · Safely open apps on your Mac](https://support.apple.com/en-us/102445)

[Deux agents IA modifient les mêmes fichiers ? Séparez leurs dossiers. →](https://no-sleep-pika.online/guide/fr/parallel-ai-agents-git-worktree/)

Rédigé par le créateur de no-sleep-pika ; présente notre app.

[Télécharger pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.3.0/pika-1.3.0.pkg)[Empêcher un Mac de se mettre en veille : écran fermé, caffeinate et pika →](https://no-sleep-pika.online/guide/fr/keep-mac-awake/)[Markdown](https://no-sleep-pika.online/guide/fr/control-mac-from-phone-qr/index.md)
