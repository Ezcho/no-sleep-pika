Source: https://no-sleep-pika.online/guide/de/control-mac-from-phone-qr/
Language: de

MAC GUIDE · 2026-11-23

# Mac per QR steuern: Sitzungen, Timer und Ausschalten vom Smartphone

Mit pika 1.3.0 steuern Sie Session und Energieoptionen vom Smartphone, nachdem Sie die Verbindung am Mac freigegeben haben.

## Mehr als den Status ansehen

Ein Build oder Download läuft auf dem Mac, während Sie in einem anderen Raum sind. Mit pika 1.3.0 ändern Sie Session, setzen Timer oder fordern Ausschalten und Neustart vom Smartphone an.

Neue Aufträge an einen KI-Agenten, KI-Chats, Terminalausgaben, Arbeitsfortschritt oder ein Remote-Desktop sind nicht enthalten.

## Zuerst die Mac-App aktualisieren

Lassen Sie pika 1.3.0 oder neuer auf dem Mac laufen. Für den Betrieb bei geschlossenem Deckel muss der Hilfsdienst funktionieren. Beide Geräte benötigen Internet.

Kann macOS den Entwickler nicht prüfen, kontrollieren Sie zuerst die offizielle Herkunft der Datei. Nach einem Öffnungsversuch wählen Sie für diese Datei in Systemeinstellungen → Datenschutz & Sicherheit „Dennoch öffnen“ und folgen der Systembestätigung. Namen können abweichen; die Installationshilfe erklärt den Weg. Deaktivieren Sie nicht den gesamten Schutz.

Warnungen vor Schadsoftware oder beschädigten Dateien sind ein anderer Fall; verwenden Sie dafür nicht diese Öffnungsausnahme.

[pika herunterladen](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.3.0/pika-1.3.0.pkg) · [Installationshilfe](https://no-sleep-pika.online/install/)

## Scannen und am Mac bestätigen

Bitten Sie einen mit pika MCP verbundenen KI-Chat um einen pika-QR. Scannen Sie ihn innerhalb von fünf Minuten mit der Handykamera. Er ist einmalig verwendbar. Zunächst erhalten Sie nur Lesezugriff; Session wird dadurch nicht eingeschaltet.

Fordern Sie am Smartphone die Steuerung an und bestätigen Sie am Mac. Erledigen Sie dies vor dem Weggehen mit beiden Geräten vor sich. Ohne Mac-Freigabe ist keine Steuerung möglich.

Die Handy-Schaltflächen sind derzeit koreanisch: „이 Mac에 연결“ verbindet, „Mac에 제어 허용 요청“ fordert die Steuerung an, danach bestätigen Sie am Mac. „예약·카운트다운 취소“ bricht Timer und Countdown ab. Für die erste MCP-Verbindung nutzen Sie die Anleitung unten.

[MCP-Verbindungsanleitung →](https://no-sleep-pika.online/de/#mcp)

## Diese Funktionen sind steuerbar

Session schaltet die Ruhezustandsverhinderung ein oder gibt sie frei. Monitor ist nur bei Session ON veränderbar; die Bildschirmregel für geschlossenen Deckel greift nach dem Zuklappen. Der Wert zeigt die angeforderte Einstellung, nicht den überprüften Bildschirmzustand.

Sie können Netzbetrieb verlangen, Session beim Abziehen des Ladegeräts oder bei 30, 40 oder 50% Akku beenden. Vorhandener Akku- und Hitzeschutz bleibt aktiv. Wärme wird als macOS-Stufe angezeigt, nicht in °C.

## Timer und 60 Sekunden zum Abbrechen

Wählen Sie 15, 30, 60, 180 oder 360 Minuten und danach Session freigeben, Ruhezustand, Ausschalten oder Neustart. Die Session-Freigabe beendet keine App zwangsweise.

Sofortiges Ausschalten oder Neustarten verlangt eine Bestätigung und startet einen abbrechbaren 60-Sekunden-Countdown. pika stellt zuvor seine Energieeinstellungen wieder her. Ungespeicherte Dokumente können die Aktion verzögern oder abbrechen. Gesendet bedeutet nicht abgeschlossen.

## Berechtigung gilt nur für die Verbindung

Die Freigabe gilt nur für die aktuelle Verbindung. Trennung oder Widerruf verwirft entfernte Timer und Countdowns; beim Neuverbinden ist erneut Zustimmung nötig. Der Zugang gilt höchstens 24 Stunden ab QR-Ausgabe. Timer laufen nach Beenden von pika oder Ruhezustand des Mac nicht weiter.

Eine Trennung wird unter Umständen erst nach einigen zehn Sekunden erkannt. Zum Verhindern des Ausschaltens drücken Sie „예약·카운트다운 취소“ und prüfen den Abbruchstatus, statt nur zu trennen. Entfernte Timer benötigen fortlaufende Verbindungssignale des Browsers; im Hintergrund kann die Verbindung abbrechen und der Timer verfallen.

Teilen Sie den QR nicht. Testen Sie Session und Timerabbruch zunächst mit unwichtigen Aufgaben. Alte Werte nach Verbindungsabbruch belegen kein Ausschalten. Netzwerk und Abschluss einer KI-Aufgabe werden nicht garantiert.

Quellen und Geltungsbereich

Anleitung des no-sleep-pika-Herstellers zur eigenen App 1.3.0, erstellt am 23. November 2026. Beachten Sie auch Apples offizielle Hinweise zu Installationswarnungen.

- [pika 1.3.0 · Release notes](https://github.com/Ezcho/no-sleep-pika/releases/tag/v1.3.0)

- [pika · Remote connection and permissions](https://github.com/Ezcho/no-sleep-pika/blob/v1.3.0/Remote/README.md)

- [Apple · Safely open apps on your Mac](https://support.apple.com/en-us/102445)

Vom no-sleep-pika-Entwickler verfasst; enthält unsere eigene App.

[pika herunterladen](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.3.0/pika-1.3.0.pkg)[Mac wach halten: Clamshell-Modus, caffeinate und pika im Vergleich →](https://no-sleep-pika.online/guide/de/keep-mac-awake/)[Markdown](https://no-sleep-pika.online/guide/de/control-mac-from-phone-qr/index.md)
