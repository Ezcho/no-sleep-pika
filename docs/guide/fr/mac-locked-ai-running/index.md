Source: https://no-sleep-pika.online/guide/fr/mac-locked-ai-running/
Language: fr

MAC GUIDE · 2026-10-05

# Mac verrouillé : Claude Code et Codex continuent-ils à travailler ?

Distinguez verrouillage, écran éteint et veille pour vérifier vos tâches IA locales avant de fermer le MacBook.

## Verrouillage et veille

L’écran de mot de passe ne prouve pas l’arrêt d’une tâche. Les commandes en arrière-plan peuvent continuer si le Mac reste éveillé, avec l’application et les connexions nécessaires. Les opérations graphiques ou d’authentification peuvent nécessiter un déverrouillage. Le Mac peut se mettre en veille après le verrouillage ; gardez la protection par mot de passe.

## Local ou cloud

Codex CLI utilise des fichiers et commandes locaux ; une tâche déléguée à Codex Cloud s’exécute dans un autre environnement. Claude Code Remote Control reste une connexion à une session locale. Une reconnexion ne prouve pas une activité pendant la veille. pika ne transfère pas les tâches vers le cloud.

[Codex CLI](https://learn.chatgpt.com/docs/codex/cli) · [Codex Cloud](https://learn.chatgpt.com/docs/cloud) · [Claude Code Remote Control](https://code.claude.com/docs/en/remote-control)

## Causes à vérifier

Lisez le dernier message : autorisation, question, fin ou erreur. Vérifiez ensuite application, Wi-Fi, VPN et connexion au compte. Les commandes en lecture seule ci-dessous montrent les demandes d’énergie et événements, pas la réussite de l’IA. Une faible activité CPU ne suffit pas non plus.

```
pmset -g assertions
```

```
pmset -g log | tail -n 60
```

## Un contrôle de trois minutes

Couvercle ouvert, lancez la boucle, laissez le terminal ouvert et verrouillez environ trois minutes. Comparez les heures puis arrêtez avec Ctrl+C. Confrontez les interruptions aux journaux d’énergie et aux résultats de l’IA. Ce test ne vérifie qu’un processus simple ; testez séparément le couvercle fermé.

```
while true; do date "+%Y-%m-%d %H:%M:%S"; sleep 10; done
```

## Configurer pika

Installez pika et son service auxiliaire. Activez Session, laissez Monitor OFF si l’écran est inutile et fermez le couvercle. La politique d’affichage s’applique alors. Session OFF libère la prévention de veille sans éteindre immédiatement l’écran. Utilisez une alimentation et un bureau ventilé, jamais un sac fermé. Protection ou panne du service peuvent arrêter la session.

[Télécharger pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg) · [Aide à l’installation](https://no-sleep-pika.online/install/)

## Questions courantes

Monitor OFF ne termine pas la tâche IA. tmux ne bloque pas la veille et caffeinate ne résout ni autorisations ni réseau. L’état de pika MCP ne représente pas la progression de toutes les tâches IA.

Sources et portée

Sources officielles et code pika consultés le 5 octobre 2026. Guide rédigé par le créateur de pika, sans garantie de fonctionnement continu sur tous les appareils.

- [Apple · Sleep and wake settings](https://support.apple.com/guide/mac-help/set-sleep-and-wake-settings-mchle41a6ccd/mac)

- [OpenAI · Codex CLI](https://learn.chatgpt.com/docs/codex/cli)

- [OpenAI · Codex Cloud](https://learn.chatgpt.com/docs/cloud)

- [Anthropic · Claude Code Remote Control](https://code.claude.com/docs/en/remote-control)

[Quand l’IA travaille la nuit, qui paie l’électricité ? →](https://no-sleep-pika.online/guide/fr/ai-overnight-electricity-cost/)

[Téléchargement arrêté sur MacBook : écran, veille et couvercle →](https://no-sleep-pika.online/guide/fr/macbook-downloads-stop/)

Rédigé par le créateur de no-sleep-pika ; présente notre app.

[Télécharger pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg)[Empêcher un Mac de se mettre en veille : écran fermé, caffeinate et pika →](https://no-sleep-pika.online/guide/fr/keep-mac-awake/)[Markdown](https://no-sleep-pika.online/guide/fr/mac-locked-ai-running/index.md)
