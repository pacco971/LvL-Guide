# Changelog

Alle wichtigen Änderungen an ForeverPath werden hier dokumentiert.

## [0.7.0] – 2026-10-30

### Neu

- Zusätzlicher lokaler ForeverDB-Import für Dungeons, Klassen, Berufe und Zonen.
- Dynamische Route-Recovery bewertet mehrere passende spätere Schritte nach dem aktuellen Score.
- Weltkarten-Overlay mit Spieler-Ziel-Linie, aktuellem Zielpunkt und kommenden Routenpunkten.
- Geglättete, spielerorientierte Pfeilrotation und drei kommende Ziele auf der Minimap.
- Klassen-/Trainerstopp und Berufsdaten-Hinweise im Live-Ratschlag.
- Dungeon-Score berücksichtigt ForeverDB-Status, Dungeonart, Gruppengröße und heuristischen Gear-/Loot-Bedarf.
- Reproduzierbarer `tools/import_foreverdb.py`-Importer und `DATA-UPDATE.md` für lokale API-Updates.

### Transparenz

- Loot- und Laufzeitwerte ohne bestätigte API-Daten bleiben ausdrücklich heuristisch.
- ForeverDB-API-Key wird nur lokal verwendet und ist nicht in ZIP, Addon oder GitHub enthalten.
- Quellen und Attribution bleiben im Einstellungen-Tab und unter `ExternalData/` sichtbar.

## [0.6.0] – 2026-10-30

### Neu

- Route-Recovery erkennt passende spätere Schritte in der aktuellen Zone.
- Neuer „Route sync“-Button im Tracker.
- Session-Tracker mit XP/h, Laufzeit, Level-Fortschritt und Todesfällen.
- Ausrüstungszustand und mögliche Questbelohnungs-Upgrades im Live-Ratschlag.
- Dungeon-Empfehlung nach Level, Gruppenzustand und Rolle.
- Daten- und Performance-Cache für zonenbezogene Evergreen-Wegpunkte.

### Verbesserungen

- XP- und Level-Events aktualisieren Fortschritt und Empfehlungen live.
- Inventaränderungen lösen eine neue Analyse der Ausrüstung aus.
- Die Navigation bleibt auch bei übersprungenen Questschritten handlungsfähig.

## [0.5.0] – 2026-10-30

### Neu

- Eigener verschiebbarer Navigations-HUD mit Richtungsanzeige und dynamischem Ziel.
- Distanz- und ETA-Schätzung für den aktuellen Quest-Wegpunkt.
- Dynamische Ziel-Linie und Zielpunkt auf der Minimap.
- Navigation im Einstellungen-Tab ein- und ausschaltbar.
- Navigation nutzt Questgeber-, Ziel- und Abgabe-Wegpunkte abhängig vom aktuellen Queststatus.
- Evergreen-Routen liefern auch ohne aktiven Questlog-Eintrag einen zonenbezogenen Fallback-Wegpunkt.

### Design

- Eigene ForeverPath-Farben und Unicode-Richtungssymbole statt RestedXP-Grafiken.
- Blizzard-Standard-Textures und unabhängiges ForeverPath-Layout bleiben erhalten.
- Routenlisten zeigen erledigte, aktuelle und kommende Schritte mit eigenen Statussymbolen.

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
