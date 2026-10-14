Source: https://no-sleep-pika.online/guide/de/macbook-downloads-stop/
Language: de

MAC GUIDE · 2026-10-15

# MacBook-Download stoppt: Display, Ruhezustand oder Deckel?

Prüfe Netzwerk und Speicher, bevor du caffeinate oder pika einsetzt.

## Zeitpunkt prüfen

Prüfe Pause, Netzwerkfehler, Speicherplatz und Anmeldung in der Download-App. Scheitert der Transfer auch während der Nutzung, prüfe WLAN, VPN und Server. Schlafverhinderung repariert keine abgelaufenen Links.

## Display und Ruhezustand

Ein dunkles Display bedeutet nicht automatisch Systemschlaf. Der Transfer kann weiterlaufen, später kann aber automatischer Schlaf folgen. Prüfe bei unterstützten Macs die Option zum Wachbleiben am Netzteil. Behalte den Passwortschutz.

## caffeinate bei offenem Deckel

Der folgende Befehl fordert eine Stunde Schutz vor Leerlaufschlaf an. Lass das Terminal offen und nutze deine Download-App. Ctrl+C beendet früher; -t zählt Sekunden, -i betrifft das System, -d das Display. Netzwerk und alle Schlafzustände sind damit nicht abgesichert.

```
caffeinate -i -t 3600
```

```
man caffeinate
```

## Bedingungen beim Schließen

Für externe Displays prüfe Netzteil, Tastatur, Maus und Modellunterstützung. Ein Ladegerät allein ist keine vollständige Konfiguration. Ohne externes Display teste einen kurzen Transfer und vergleiche empfangene Bytes vor und nach dem Schließen.

## Mit pika herunterladen

Bereite pika und Hilfsdienst vor, starte den Download, aktiviere Session und lasse Monitor OFF, falls kein Display nötig ist. Die Display-Richtlinie greift nach dem Schließen. Danach Session OFF. Nutze Strom und einen belüfteten Tisch, keine geschlossene Tasche. Schutzfunktionen oder Fehler können die Sitzung stoppen.

[pika herunterladen](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg) · [Installationshilfe](https://no-sleep-pika.online/install/)

## Ergebnis prüfen

Prüfe Abschluss, Dateigröße und angebotene Prüfsumme. Nutze die Fortsetzungsfunktion der App. pika repariert keine Verbindung und erkennt keinen Downloadabschluss. Ein ausgeschaltetes Display garantiert keinen Geschwindigkeitsgewinn.

Quellen

Geprüft am 11. Oktober 2026 anhand von Apple, caffeinate(8) und pika-Code. Anleitung des pika-Entwicklers.

- [Apple · Sleep and wake settings](https://support.apple.com/guide/mac-help/set-sleep-and-wake-settings-mchle41a6ccd/mac)

- [Apple · External displays](https://support.apple.com/en-us/102501)

- `man caffeinate` · macOS System Manager’s Manual

[Wenn die KI nachts arbeitet: Wer zahlt den Strom? →](https://no-sleep-pika.online/guide/de/ai-overnight-electricity-cost/)

Vom no-sleep-pika-Entwickler verfasst; enthält unsere eigene App.

[pika herunterladen](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg)[Mac wach halten: Clamshell-Modus, caffeinate und pika im Vergleich →](https://no-sleep-pika.online/guide/de/keep-mac-awake/)[Markdown](https://no-sleep-pika.online/guide/de/macbook-downloads-stop/index.md)
