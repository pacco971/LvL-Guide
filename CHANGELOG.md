# Changelog

## [0.9.3] – 2026-11-02

- Addon-Paket auf ForeverPath `0.9.3` angehoben.
- Release-Paket für den automatischen CurseForge-Upload vorbereitet.

Alle wichtigen Änderungen an ForeverPath werden hier dokumentiert.

## [0.9.3-beta] – 2026-11-03

- Navigation, Minimap-Linie und Weltkarten-Overlay gegen geschützte/ungültige Positionswerte abgesichert; nicht lesbare Werte werden als „nicht verfügbar“ behandelt.
- User-Waypoints werden vor dem Setzen geprüft und in geschützten Kartenbereichen sicher ignoriert, statt das Addon zu stoppen.
- SavedVariables-Profil verwendet Charaktername/Realm statt einer möglichen GUID als Tabellenschlüssel und exportiert den Ladezustand im Fehlerbericht.
- Rewardvergleich meldet den tatsächlich verfügbaren Forever-Client-API-Status, statt fehlende Item-Belohnungsfunktionen stillschweigend vorauszusetzen.
- ForeverDB-Importer um optionalen `--extended`-Lauf für Itemsets, Händler, Gifte, Disenchant, Battlegrounds und Dungeon-Details erweitert; der Schlüssel bleibt ausschließlich lokal.
- QuestPilot-Icon ergänzt und als Addon-Icon in der TOC hinterlegt.
- Neue Beta-ZIP enthält weiterhin den statischen ForeverDB-Stand `1.60.1.70707`; ein echter Login-/Ingame-Test bleibt vor Veröffentlichung als Release offen.

## [0.9.2] – 2026-11-01

- ForeverDB-Daten auf Build `1.60.1.70707` aktualisiert.
- Questdaten speichern jetzt zusätzlich Quest-Build und Clientkennung.
- Dungeons, Klassen, Berufe, Zonen sowie bestätigte ForeverDB-Änderungen (`changes-seen`, `verified=1`) importiert.
- Datenstatus im Addon zeigt Build, Importumfang und bestätigte Änderungen an.
- README-Installation auf den tatsächlichen Forever-Installationsordner angepasst; kein fest vorausgesetzter Ordnername `_forever_` mehr.
- Paket- und statische Prüfungen durchgeführt; echter Login-/Ingame-Smoke-Test bleibt bis zum verfügbaren Forever-Client offen.

## [0.9.1] – 2026-10-31

### Route 1.0 und Navigation

- Questplanung bevorzugt die aktuelle Zone und den aktuellen Kartenbereich; aktive Quests, Abgaben und Folgequests stehen vor entfernten Annahmen.
- Fraktions-, Klassen-, Vorquest- und Levelprüfung verschärft; fremde Gebiete werden nur noch als begründete Ausweichroute behalten.
- Reisehinweise unterscheiden Fußweg/Reittier, Flugpunkt, Hearthstone, Boot/Zeppelin und Klassenreise. Nicht messbare Flug-/Bootszeiten bleiben ausdrücklich Schätzungen.
- Navigations-HUD zeigt zusätzliche Zielarten für Gegner und Items; Wegpunktlisten und Weltkartenpunkte werden gecacht.

### Gear, UI und Performance

- Belohnungsvergleich berücksichtigt Zweihandwaffen, Main-/Offhand, Ringe und Schmuck getrennt und wartet auf vollständig geladene Itemdaten.
- Questketten, Folgequests, Quest-ID/Quelle, Zonenfortschritt und dynamische Routenalternativen sind im Route-Tab sichtbar.
- Kompakt- und Streamer-Layouts ergänzt; wiederkehrende Questplan-, Reward- und Wegpunktberechnungen werden zwischengespeichert.

## [0.9.0] – 2026-10-31

### Questplanung und Navigation

- QuestPlanner erstellt aus dem lokalen Datenstand eigene Annahme-, Ziel- und Abgabeschritte mit Quest-ID, Folgequest, Filtern und sichtbarer Quelle.
- Live-Questlog, Questobjektive, Folgequests und bereits abgegebene Quests werden automatisch in die aktive Reihenfolge einbezogen.
- Schritt überspringen, Route-Recovery und Rückkehr zur Hauptstrecke sind direkt über Tracker und Menü erreichbar.
- Navigations-HUD kennzeichnet NPC, Ziel und Abgabe; Minimap-Route und Weltkartenpunkte bleiben erhalten. Die Entfernung wird korrekt als relative Kartenstrecke ausgewiesen.

### Gear, UI und Komfort

- Neuer Tab **Gear & Rewards** mit Slotübersicht, Gear-Profilen und Questbelohnungs-Vergleich nach vollständig geladenen Itemdaten.
- Waffen-, Tank-, Heiler-, DPS- und Solo-Gewichtungen werden getrennt behandelt; fehlende oder noch ladende Items werden sichtbar markiert.
- Ersteinrichtung mit erkannter Klasse/Fraktion, Standardpositionen und Datenstand.
- Einstellungen, Datenquellen und Supportfunktionen bleiben ohne Chatbefehle über Minimap-Icon und Buttons erreichbar.

### Stabilität und Daten

- Legacy-Questlog-Fallback robuster gemacht und Questkettenfelder aus dem offenen Import erhalten.
- Session-, Gruppen-, Trainer-, Berufs- und Itemdaten werden weiter lokal gemessen; nicht verfügbare Werte bleiben als Schätzung gekennzeichnet.
- API-Key bleibt außerhalb von Addon und ZIP.

## [0.8.0] – 2026-10-30

### Quest- und Routenlogik

- Quest-ID-Datenbank mit NPC-, Ziel-, Abgabe- und Folgequest-Hinweisen aus dem lokalen ForeverDB-Import.
- Tracker zeigt echte Live-Questobjektive, Restziele und „Quest kann abgegeben werden“.
- Automatisches Weiterblättern über mehrere bereits erfüllte Schritte.
- Route-Recovery 2.0 bewertet Zonen-Treffer und Score-Alternativen für übersprungene Schritte.

### UI, Gear und Stopps

- Tracker einklappbar und skalierbar; Quest-Fortschrittsbalken ergänzt.
- Fensterpositionen werden gespeichert; Tracker, Pfeil und Hauptmenü lassen sich skalieren, sperren, dimmen und im Minimalmodus betreiben.
- Gear-Bewertung unterstützt Auto-, DPS-, Tank- und Heilerprofile.
- Trainer-, Berufs-, Gasthof-, Flugpunkt-, Reparatur- und Hauptstadtstopps werden als Empfehlungen eingeplant.
- Diagnosefenster exportiert einen kopierbaren Fehlerbericht für Discord.

### Datenstatus

- Datenstatus zeigt ForeverDB-Build, importierte Questanzahl und den Offline-Charakter des Addons.
- API-Key bleibt außerhalb des Addons; die Prüfung neuer Daten erfolgt weiterhin über den lokalen Importer.

## [0.7.2] – 2026-10-30

### Dokumentation

- GitHub-Installationsanleitung korrigiert: `LvL-Guide-main.zip` entpacken, darin `ForeverPath.zip` entpacken und erst danach den Ordner `ForeverPath` nach `_forever_/Interface/AddOns/` kopieren.
- Verschachtelte Fehlpfade wie `AddOns/ForeverPath/ForeverPath/` und das direkte Kopieren der ZIP werden ausdrücklich erklärt.

## [0.7.1] – 2026-10-30

### Verbesserungen

- Slashcommands vollständig entfernt.
- Bedienung ist jetzt ausschließlich über Minimap-Icon, Tracker und Menübuttons möglich.
- Installations- und Addon-README entsprechend aktualisiert.

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
