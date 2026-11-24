Source: https://no-sleep-pika.online/guide/de/parallel-ai-agents-git-worktree/
Language: de

MAC GUIDE · 2026-11-24

# Zwei KI-Agenten ändern dieselben Dateien? Erst die Ordner trennen.

Mit Git worktree bekommt jeder Agent einen eigenen Arbeitsordner. So verteilst du Aufgaben, prüfst Änderungen und führst Ergebnisse Schritt für Schritt zusammen.

## Warum ein gemeinsamer Ordner problematisch ist

Ein Agent ändert die Oberfläche, ein anderer schreibt Tests. Im selben Ordner lesen und bearbeiten beide dieselben Dateien. Zwei Branch-Namen erzeugen dort keine zwei unabhängigen Dateisätze. Ein Branch-Wechsel verändert auch die Dateien, mit denen der andere Agent arbeitet.

Git worktree fügt demselben Repository einen Arbeitsordner hinzu. Jeder Ordner kann seinen eigenen Branch und ausgecheckte Dateien haben; die Historie bleibt gemeinsam. Laufende Änderungen sind getrennt, spätere Konflikte beim Zusammenführen bleiben trotzdem möglich.

- 1 Ordner trennen

- 2 Aufgaben zuweisen

- 3 Änderungen prüfen

- 4 Einzeln integrieren

## Einen geprüften Ausgangspunkt wählen

Führe den folgenden Befehl im bestehenden Git-Projekt aus. Mindestens ein Commit muss vorhanden sein; HEAD bezeichnet den gespeicherten Ausgangspunkt. Keine Ausgabe bedeutet keine gemeldeten Änderungen oder unversionierten Dateien. Ignorierte Dateien können dennoch vorhanden sein.

Prüfe aufgelistete Dateien zuerst. Committe nur gewünschte, geprüfte Änderungen oder wähle einen vorhandenen Commit. Nimm nicht blind den ganzen Ordner auf: Geheimnisse und fremde Änderungen gehören nicht hinein. Neue Ordner beginnen bei HEAD, nicht bei uncommitteten Änderungen.

```
git status --short
```

## Zwei Arbeitsordner anlegen

Beide Befehle werden im ursprünglichen Projekt ausgeführt. Sie erstellen ai-ui und ai-tests sowie benachbarte Arbeitsordner. Branch-Namen und Zielpfade müssen unbenutzt sein. Wähle sonst andere Namen, statt etwas zu überschreiben.

Installierte Abhängigkeiten, ignorierte .env-Dateien und lokale Einstellungen werden nicht vollständig übernommen. Bereite sie nach Projektanleitung vor, gib nur nötige Zugangsdaten weiter und nutze unterschiedliche Ports für gleichzeitige Server. Worktrees sind keine Sicherheits-Sandbox: Werkzeuge können mit passenden Rechten andere Ordner erreichen.

```
git worktree add -b ai-ui ../project-ai-ui HEAD
git worktree add -b ai-tests ../project-ai-tests HEAD
```

## Ordner und Aufgabe klar zuweisen

Starte einen Agenten in project-ai-ui, den anderen in project-ai-tests. Nenne den absoluten Pfad und eine enge Aufgabe: etwa „nur die Oberflächenkomponente ändern“ und „Tests für bestehendes Verhalten ergänzen, keinen Anwendungscode ändern“.

Lege Zuständigkeiten für gemeinsame Dateien wie Abhängigkeitslisten und Lockfiles fest. Müssen beide dieselbe Datei ändern, arbeite nacheinander. Lass geänderte Dateien, ausgeführte Prüfungen und offene Punkte melden.

## Prüfen und einzeln zusammenführen

Führe die drei Befehle in jedem Ordner aus. Status zeigt Änderungen und unversionierte Dateien. Diff zeigt nicht vorgemerkte Änderungen an versionierten Dateien, diff --cached die vorgemerkten. Neue unversionierte Dateien fehlen in diesen Diffs; öffne sie zusätzlich.

Führe passende Projektprüfungen aus und committe die geprüften Änderungen im jeweiligen Branch. Kehre dann zum ursprünglichen Projekt zurück und prüfe und integriere einen Branch nach dem anderen in den Zielbranch. Worktree führt Ergebnisse nicht automatisch zusammen. Löse Konflikte und prüfe das Gesamtergebnis vor dem nächsten Branch.

```
git status --short
git diff
git diff --cached
```

## Was pika dabei leistet

pika kann den Mac während lokaler KI-Arbeit wach halten, abhängig von Sitzungseinstellungen und Schutzfunktionen. Es verteilt keine Aufgaben und löst weder Merges noch Konflikte. Der QR-Zugang von pika 1.3 zeigt Mac-Status und erlaubte Stromsteuerung, keine KI-Ausgabe oder verlässliche Fertigstellungsquote. Prüfe dafür die Agentenergebnisse und Projekttests.

[pika herunterladen](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.3.0/pika-1.3.0.pkg) · [Installationshilfe](https://no-sleep-pika.online/install/)

Quellen und Geltungsbereich

Dieser Leitfaden vom Hersteller von no-sleep-pika folgt der offiziellen Git-Dokumentation. Er gilt für allgemeine KI-Agenten und setzt keine bestimmten Produktfunktionen oder Rechte voraus. Beachte zusätzlich die Projektregeln und den Umgang mit Geheimnissen.

- [Git · git-worktree](https://git-scm.com/docs/git-worktree)

- [Git · git-status](https://git-scm.com/docs/git-status)

- [Git · git-diff](https://git-scm.com/docs/git-diff)

Vom no-sleep-pika-Entwickler verfasst; enthält unsere eigene App.

[Mac wach halten: Clamshell-Modus, caffeinate und pika im Vergleich →](https://no-sleep-pika.online/guide/de/keep-mac-awake/)[Markdown](https://no-sleep-pika.online/guide/de/parallel-ai-agents-git-worktree/index.md)
