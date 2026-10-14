Source: https://no-sleep-pika.online/guide/de/ai-overnight-electricity-cost/
Language: de

MAC GUIDE · 2026-10-15

# Wenn die KI nachts arbeitet: Wer zahlt den Strom?

Acht Stunden Mac-Betrieb als Rechenbeispiel – getrennt von Abonnement- und API-Kosten.

## Zwei getrennte Kosten

Bei Cloud-KI übernimmt der Anbieter die eigentliche Modellberechnung. Lokale Builds und Tests verbrauchen trotzdem Strom auf deinem Mac. Ein lokales Modell wird ebenfalls dort berechnet. Haushaltsstrom und KI-Gebühren sind getrennte Kosten; eine Steckdosenmessung erfasst nicht das Rechenzentrum.

## Was kosten acht Stunden?

Mittlere Watt × Stunden ÷ 1.000 ergibt kWh. Multipliziere mit deinem Tarif. Fiktives Beispiel: acht Stunden täglich, dreißig Tage, 0,20 USD/kWh. Bei 10W: 0,08kWh und 0,016 USD pro Nacht; 2,4kWh und 0,48 USD für dreißig Nächte. Bei 30W: 0,24kWh und 0,048 USD; 7,2kWh und 1,44 USD. Bei 60W: 0,48kWh und 0,096 USD; 14,4kWh und 2,88 USD.

Das sind keine MacBook-Messwerte oder örtlichen Tarife. Steuern und Tarifstaffeln verändern die Rechnung. Für Mehrkosten gegenüber dem Ruhezustand dessen Verbrauch über dieselbe Zeit messen und abziehen.

## Netzteilleistung ist nicht Verbrauch

Ein 70W-Netzteil bedeutet keinen dauerhaften Verbrauch von 70W. Akkuladung, Displays und lokale Aufgaben verändern die Last. Ein ausgeschaltetes Display kann Strom sparen, aber nicht bei jedem Gerät denselben Betrag.

## Die eigene Arbeit messen

Ein Steckdosenmessgerät mit kumulierten kWh nach Anleitung verwenden. 0,06kWh in zwei Stunden entsprechen durchschnittlich 30W. Acht Stunden ergeben nur bei ähnlicher Last 0,24kWh. Möglichst die ganze Aufgabe messen, Akkustände notieren und separat versorgte Displays berücksichtigen: Sie fehlen in der Netzteilmessung.

## Spart pika Strom?

pika hält Aufgaben am Laufen, die der Ruhezustand unterbrechen könnte. Es misst keinen Strom und senkt keine KI-Gebühren. Wachhalten kann mehr Strom verbrauchen. Hilfsdienst prüfen, Session einschalten, Monitor bei unnötiger Anzeige ausschalten und kurz mit geschlossenem Deckel testen. Danach Session ausschalten. Freigaben, Netzwerkfehler und die Erkennung des Aufgabenendes bleiben separate Themen.

[pika herunterladen](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg) · [Installationshilfe](https://no-sleep-pika.online/install/)

## Vor dem Weggehen

Ergebnis und Abbruchbedingung festlegen. Falls angeboten, Nutzungsgrenzen oder Warnungen einstellen; ein bestehendes Abo nicht doppelt als Zusatzkosten zählen. Netzstrom und eine feste, gut belüftete Tischfläche nutzen, keine Tasche oder Bettdecke.

Annahmen und Quellen

Vom pika-Entwickler verfasst. Formel: Virginia Cooperative Extension. Belüftung: Apple. Wattwerte und USD-Tarif sind Annahmen.

- [Virginia Cooperative Extension · Estimating appliance energy use](https://ext.vt.edu/content/pubs_ext_vt_edu/en/2901/2901-9014/2901-9014.html)

- [Apple · Mac operating temperatures](https://support.apple.com/en-us/102336)

Vom no-sleep-pika-Entwickler verfasst; enthält unsere eigene App.

[pika herunterladen](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg)[Mac wach halten: Clamshell-Modus, caffeinate und pika im Vergleich →](https://no-sleep-pika.online/guide/de/keep-mac-awake/)[Markdown](https://no-sleep-pika.online/guide/de/ai-overnight-electricity-cost/index.md)
