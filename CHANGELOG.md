# Changelog

Alle wichtigen Änderungen an ForeverPath werden hier dokumentiert.

## [0.4.0] – 2026-10-30

### Neu

- Questdaten aus ForeverDB als lokaler Build-Import integriert.
- Questlevel, Fraktion, Zone, Forever-Status, Questgeber und Abgabeorte verfügbar.
- Questketten mit Vorgänger- und Folgequests ergänzt.
- Automatische Ziel- und Abgabe-Wegpunkte im Questtracker.
- Sichtbare Quellenangabe `Data from ForeverDB.net (https://foreverdb.net)` im Addon.
- QuestieDB-Forever-Marker und Evergreen-Routen-/Klassenhinweise integriert.
- 2.029 normalisierte Evergreen-Routenschritte mit Klassen- und Rasseninformationen.
- Beweglicher Minimap-Button und beweglicher Fortschritts-Tracker.
- Automatischer Questscan beim Login und anschließend alle fünf Minuten.
- Routenbewertung mit Reisezeit, Kampf, Risiko, Gruppenwartezeit, Klassen-, Dungeon-, Ausrüstungs-, Ketten- und Folgequest-Bonus.

### Verbesserungen

- Der Tracker zeigt aktuelle Questziele, Fortschritt, beste Empfehlung und Entfernung an.
- Das Menü nutzt für Wegpunkte die aktuelle Questphase: Annahme, Ziel oder Abgabe.
- Questschritte können bei erfüllten Questzielen automatisch weitergeschaltet werden.
- Datenquellen, Lizenzhinweise und Attribution befinden sich im Addon unter `ExternalData/`.

### Sicherheit und Lizenzen

- Der ForeverDB-API-Key ist nicht Bestandteil des Addons oder der ZIP-Datei.
- Der Client fragt ForeverDB nicht live ab; die Questdaten sind ein dokumentierter Build-Import.
- GPL-3.0- und GPL-2.0-or-later-Hinweise sowie die Attribution der offenen Daten bleiben erhalten.
- Es werden keine RestedXP-Quelltexte, Grafiken, Texte oder geschützten Routen übernommen.

## [0.3.0]

- Grundlegendes ForeverPath-Menü und gespeicherter Routenfortschritt.
- Speedrun-, Dungeon-, Discovery- und Legacy-Modus.
- Klassenprofile für Solo-, Dungeon- und Hybridspielweisen.
- Minimap-Button, Fortschritts-Tracker und optionale Wegpunkte.
- Questlog-Scan und erste Score-Empfehlungen.
