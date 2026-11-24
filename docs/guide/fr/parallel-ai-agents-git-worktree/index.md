Source: https://no-sleep-pika.online/guide/fr/parallel-ai-agents-git-worktree/
Language: fr

MAC GUIDE · 2026-11-24

# Deux agents IA modifient les mêmes fichiers ? Séparez leurs dossiers.

Git worktree donne à chaque agent son propre dossier. Répartissez les tâches, vérifiez les changements puis intégrez-les sans mélanger les travaux en cours.

## Pourquoi un dossier partagé pose problème

Un agent modifie l’interface, l’autre écrit des tests. Dans un même dossier, ils lisent et modifient les mêmes fichiers. Deux noms de branche ne créent pas deux copies indépendantes. Changer de branche dans ce dossier change aussi les fichiers utilisés par l’autre agent.

Git worktree ajoute un dossier de travail au même dépôt. Chaque dossier peut avoir sa branche et ses fichiers, tout en partageant l’historique. Cela sépare les travaux en cours, sans garantir une intégration sans conflit.

- 1 Séparer les dossiers

- 2 Répartir les tâches

- 3 Vérifier les changements

- 4 Intégrer à tour de rôle

## Préparer un point de départ vérifié

Lancez la commande suivante dans un projet Git existant. Il faut au moins un commit : HEAD désigne le point de départ enregistré. Une sortie vide signifie qu’aucune modification ni fichier non suivi n’est signalé. Des fichiers ignorés peuvent toutefois être présents.

Si une liste apparaît, examinez-la puis enregistrez uniquement les modifications voulues, ou choisissez un commit existant. N’ajoutez pas tout le dossier sans vérification : secrets et travaux sans rapport doivent rester à l’écart. Les nouveaux dossiers partent de HEAD, pas des modifications non commitées.

```
git status --short
```

## Créer deux dossiers de travail

Depuis le projet d’origine, ces commandes créent les branches ai-ui et ai-tests et deux dossiers voisins. Choisissez des noms de branche et des chemins encore inutilisés. S’ils existent déjà, changez de nom plutôt que de forcer un écrasement.

Les dépendances installées, les fichiers .env ignorés et les réglages locaux ne sont pas tous copiés. Suivez les instructions du projet, ne fournissez que les identifiants nécessaires et utilisez des ports différents pour les serveurs simultanés. Un worktree n’est pas une isolation de sécurité : les permissions peuvent permettre l’accès à d’autres dossiers.

```
git worktree add -b ai-ui ../project-ai-ui HEAD
git worktree add -b ai-tests ../project-ai-tests HEAD
```

## Attribuer un dossier et une tâche

Ouvrez un agent dans project-ai-ui et l’autre dans project-ai-tests. Donnez le chemin absolu et une mission précise : « modifier seulement le composant d’interface » et « ajouter des tests du comportement actuel sans changer le code de l’application ».

Attribuez les fichiers communs, notamment les listes de dépendances et les fichiers de verrouillage. Si les deux tâches touchent le même fichier, avancez dans l’ordre. Demandez les fichiers modifiés, les vérifications effectuées et le travail restant.

## Vérifier puis intégrer une branche à la fois

Lancez les trois commandes dans chaque dossier. Status liste les modifications et fichiers non suivis. Diff montre les modifications non indexées des fichiers suivis ; diff --cached montre celles déjà indexées. Les nouveaux fichiers non suivis n’apparaissent pas dans ces diff : ouvrez-les séparément.

Effectuez les vérifications du projet et créez un commit des modifications validées sur chaque branche. Revenez ensuite au projet initial pour examiner et intégrer une branche à la fois dans la branche cible. Worktree ne fusionne rien automatiquement. Résolvez les conflits et vérifiez le résultat combiné avant la branche suivante.

```
git status --short
git diff
git diff --cached
```

## Le rôle de pika

pika peut garder le Mac éveillé pendant le travail local, selon les réglages de session et les protections. Il ne répartit pas les tâches et ne gère ni fusion ni conflit. Le QR de pika 1.3 présente l’état du Mac et les commandes d’alimentation autorisées, pas la sortie de l’IA ni un pourcentage fiable d’avancement. Vérifiez les résultats de l’agent et les tests du projet.

[Télécharger pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.3.0/pika-1.3.0.pkg) · [Aide à l’installation](https://no-sleep-pika.online/install/)

Sources et périmètre

Ce guide du créateur de no-sleep-pika suit les documents officiels de Git. Il concerne des agents génériques, sans supposer les fonctions ou permissions d’un produit. Respectez aussi les règles du projet et de gestion des secrets.

- [Git · git-worktree](https://git-scm.com/docs/git-worktree)

- [Git · git-status](https://git-scm.com/docs/git-status)

- [Git · git-diff](https://git-scm.com/docs/git-diff)

Rédigé par le créateur de no-sleep-pika ; présente notre app.

[Empêcher un Mac de se mettre en veille : écran fermé, caffeinate et pika →](https://no-sleep-pika.online/guide/fr/keep-mac-awake/)[Markdown](https://no-sleep-pika.online/guide/fr/parallel-ai-agents-git-worktree/index.md)
