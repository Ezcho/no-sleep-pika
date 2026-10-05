Source: https://no-sleep-pika.online/guide/de/mac-locked-ai-running/
Language: de

MAC GUIDE · 2026-10-05

# Mac gesperrt: Arbeiten Claude Code und Codex weiter?

Unterscheide Bildschirmsperre, ausgeschaltetes Display und Ruhezustand bei lokalen KI-Aufgaben.

## Sperre oder Ruhezustand

Ein Passwortbildschirm beweist keinen Aufgabenabbruch. Hintergrundbefehle können weiterlaufen, wenn Mac, App und benötigte Verbindungen aktiv bleiben. Grafische Bedienung oder Authentifizierung kann Entsperren erfordern. Nach der Sperre kann später der Ruhezustand folgen. Lass den Passwortschutz eingeschaltet.

## Lokal oder Cloud

Codex CLI verarbeitet Dateien und Befehle lokal; an Codex Cloud übergebene Aufgaben laufen in einer anderen Umgebung. Claude Code Remote Control verbindet weiterhin eine lokale Sitzung. Wiederverbinden beweist keine Ausführung während des Schlafens. pika verschiebt Aufgaben nicht in die Cloud.

[Codex CLI](https://learn.chatgpt.com/docs/codex/cli) · [Codex Cloud](https://learn.chatgpt.com/docs/cloud) · [Claude Code Remote Control](https://code.claude.com/docs/en/remote-control)

## Ursachen prüfen

Prüfe die letzte Nachricht auf Freigaben, Fragen, Abschluss oder Fehler. Prüfe dann App, WLAN, VPN und Anmeldung. Die folgenden Lesebefehle zeigen Energieanforderungen und Ereignisse, nicht den KI-Fortschritt. Auch geringe CPU-Last beweist keinen Stillstand.

```
pmset -g assertions
```

```
pmset -g log | tail -n 60
```

## Drei Minuten testen

Starte die Schleife bei offenem Deckel, lass das Terminal offen und sperre etwa drei Minuten. Vergleiche die Zeitstempel und beende mit Ctrl+C. Vergleiche Lücken mit Energieprotokollen und KI-Ergebnissen. Dies testet nur einen einfachen Prozess; geschlossenen Deckel separat testen.

```
while true; do date "+%Y-%m-%d %H:%M:%S"; sleep 10; done
```

## pika einrichten

Installiere pika samt Hilfsdienst, aktiviere Session und lasse Monitor OFF, falls kein Display nötig ist. Schließe dann den Deckel; erst dann greift die Display-Richtlinie. Session OFF gibt den Ruhezustand wieder frei, ohne das Display sofort auszuschalten. Nutze Stromversorgung und einen belüfteten Tisch, keine geschlossene Tasche. Schutzfunktionen oder Dienstfehler können die Sitzung stoppen.

[pika herunterladen](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg) · [Installationshilfe](https://no-sleep-pika.online/install/)

## Häufige Fragen

Monitor OFF beendet nicht die KI. tmux verhindert keinen Systemschlaf; caffeinate löst weder Netzwerkprobleme noch Freigaben. Der pika-MCP-Status ist kein Fortschrittsbericht sämtlicher KI-Aufgaben.

Quellen und Geltungsbereich

Offizielle Quellen und pika-Code geprüft am 5. Oktober 2026. Vom pika-Entwickler verfasst; keine Garantie für unterbrechungsfreien Betrieb auf jedem Gerät.

- [Apple · Sleep and wake settings](https://support.apple.com/guide/mac-help/set-sleep-and-wake-settings-mchle41a6ccd/mac)

- [OpenAI · Codex CLI](https://learn.chatgpt.com/docs/codex/cli)

- [OpenAI · Codex Cloud](https://learn.chatgpt.com/docs/cloud)

- [Anthropic · Claude Code Remote Control](https://code.claude.com/docs/en/remote-control)

Vom no-sleep-pika-Entwickler verfasst; enthält unsere eigene App.

[pika herunterladen](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg)[Mac wach halten: Clamshell-Modus, caffeinate und pika im Vergleich →](https://no-sleep-pika.online/guide/de/keep-mac-awake/)[Markdown](https://no-sleep-pika.online/guide/de/mac-locked-ai-running/index.md)
