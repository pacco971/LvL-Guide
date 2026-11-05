# Changelog

## [0.9.32-beta] – 2026-11-05

- Eigenes Addon-Icon als 64x64-TGA ergänzt und im TOC korrekt verknüpft.
- Navigationspfeil durch eine eigene, scharf gerenderte Pfeilgrafik ersetzt.
- Generisches Blizzard-Seitensymbol, Doppel-Glow und dunkler Rahmen aus dem separaten Pfeil-HUD entfernt.
- Pfeil-HUD bleibt frei verschiebbar und zeigt Schritt, Entfernung/ETA und das gekürzte Ziel kompakt unter dem Pfeil.

## [0.9.31-beta] – 2026-11-05

- Eigene Guide-Engine für Forever-Routen ergänzt: Questannahme, Ziele, Abgabe und Folgequest werden als getrennte Schritte geplant.
- Eigene Reise-/Versorgungsstopps sowie Klassenlehrer-Meilensteine erscheinen im selben scrollbaren Tracker; Fähigkeiten werden erst aus dem geöffneten Trainerfenster übernommen.
- Aktive Questlog-Schritte bleiben die höchste Priorität, während Zonen-, Ketten- und Routenfilter die nächsten unabhängigen Guide-Schritte ergänzen.
- Tracker-Aktion für Trainer- und Reisestopps repariert; diese Schritte können nach der Durchführung sauber abgehakt werden.
- Navigation erkennt jetzt auch eigene Schritte mit Zielpunkt, ohne die Questlog-Route zu überschreiben.
- Englische UI-Bezeichnungen für die neuen Trainer-/Reisestopp-Schritte ergänzt.

## [0.9.30-beta] – 2026-11-05

- XP-HUD auf ein klares, dreizeiliges Layout umgebaut: Levelzeit und Sitzungszeit oben, aktuelle XP
  mit Prozentwert in der Mitte und ETA/XP pro Stunde/Questlog-XP unten.
- Questlog-Projektion bleibt als goldene Vorschau sichtbar; die tatsächlich vorhandene XP wird als
  eigener farbiger Balken darüber dargestellt.
- Abgeschlossene Quest-XP, Erholungsbonus und `LEVEL UP READY!` werden direkt im HUD angezeigt.
- XP-Anzeige standardmäßig größer und weiterhin über das Menü verschiebbar, skalierbar, in der Größe
  änderbar, ein-/ausblendbar und sperrbar.
- Englische Sprachschlüssel für die neuen XP-HUD-Texte ergänzt.

## [0.9.29-beta] – 2026-11-05

- Ingame-Tracker auf einen echten Scrollbereich umgestellt.
- Weitere Folgequests und bis zu acht kommende Guide-Schritte werden unter den aktuellen Handlungen angezeigt.
- Mausrad scrollt den Tracker; kommende Schritte können angeklickt und als aktueller Fokus geladen werden.
- Neue Scroll-/Schritttexte für Deutsch und English ergänzt.

## [0.9.28-beta] – 2026-11-05

- Tracker-Schritte um konkrete Handlungen erweitert: Quest annehmen, Questgeber/NPC, Zielgebiet mit Koordinaten, Questabgabe, Abgabe-NPC und Folgequest.
- Klassen-/Trainerhinweis in die Route aufgenommen: nächster Meilenstein mit Stufe und Ort; nach einem geöffneten Trainerfenster werden tatsächlich verfügbare Fähigkeiten und der beobachtete Ort angezeigt.
- Klassen-Tab zeigt jeden Meilenstein jetzt mit einem Standort-Hinweis.
- Trainerdaten bleiben clientbasiert: Ohne besuchtes Trainerfenster werden keine erfundenen Zaubernamen behauptet.
- Neue Trackertexte vollständig für Deutsch und English ergänzt.

## [0.9.27-beta] – 2026-11-05

- Kompaktes, eigenständiges Navigations-HUD: kleiner einzelner Dreieckspfeil, kein zweiter Glow und kein übergroßes oberes Navigationsfeld.
- Der Pfeil folgt weiterhin dynamisch der Blickrichtung und aktualisiert Schritt, Entfernung/ETA sowie das gekürzte Ziel live.
- XP-Vorschau als eigenes verschiebbares HUD: Ein/Aus, Breite, Höhe, Skalierung und Sperre im Menü.
- Detaillierte Tracker-Schritte für Questannahme, NPC-Gespräch, Ziele, Abgabe, Abgabe-NPC und Folgequest ergänzt.
- Englische Bezeichnungen für die neuen XP- und Tracker-Einstellungen ergänzt.

## [0.9.26-beta] – 2026-11-05

- eigener **Questlog**-Tab: alle aktiven Quests statt eines festen Fünfer-Limits
- Statuspunkte und Unterziele im Tracker mit Questlog-Fortschritt
- Linksklick öffnet den eigenen Questlog, Rechtsklick setzt den Questfokus für Route und Pfeil
- kleiner eigener Journey Log für angenommene/entfernte Quests
- Klassen-Meilensteine für Trainer, Reittier, Reise, Waffen und Rollenfenster
- Schnellroute bewertet Live-Questlog, Zone, Level, Questkette, Koordinaten, Fraktion und Klassenfilter
- keine Laufzeit-Abhängigkeit von Questie; nur eigener Questlog-Scanner und mitgelieferte Daten

## [0.9.25-beta] – 2026-11-05

- Navigation optisch bereinigt: dünne blaue Kernlinie mit dezentem Glow, ein goldener Zielring und ein einzelnes Zielnamen-Label; kommende blaue Punkte bleiben aus.
- Karten- und Minimap-Ziel zeigen jetzt den aktiven Questnamen statt eines anonymen Folgepunkts.
- Questlog bleibt die autoritative Quelle für aktive Quest, Ziele und Abgabephase; die lokalen Forever-/Questdaten ergänzen NPC-, Ziel- und Folgequest-Informationen ohne externe Questie-Abhängigkeit.
- Neuer Reiseplan-Tab für Fuß/Reittier, Flugpunkt, Schiff/Zeppelin, Hearthstone, Klassenreise und Zonenwechsel mit klarer Kennzeichnung bestätigter und unbestätigter Optionen.
- Gear-&-Rewards-Tab erweitert: Auto/DPS/Tank/Heiler/Solo-Profile, Prozentvergleich von Belohnungen und deutlichere Slot-/Itemdaten.
- Sichere Auto-Quest-Aktion: passende Questannahme und Öffnen der Abgabe können automatisch erfolgen; die Auswahl und Bestätigung der Questbelohnung bleibt manuell.
- Neue Funktionen und Statusmeldungen sind für Deutsch und English vorbereitet.
- `GetWorldPosFromMapPos` robuster gegen Forever-Rückgaben mit Statuswert plus Vektor abgesichert.

## [0.9.24-beta] – 2026-11-05

- Neue Sprachumschaltung im Menü: Deutsch ↔ English, gespeichert pro Charakter.
- Tabs, Einstellungen, Navigation, Questtracker, Onboarding und Statusanzeigen wechseln sofort mit.
- Questtitel und Questziele bleiben bewusst in der Sprache des Forever-Clients/Questlogs, damit keine falschen Übersetzungen angezeigt werden.

## [0.9.23-beta] – 2026-11-05

- Minimap-Button neu gestaltet: kompaktes Karten-Icon mit sauberem ForeverPath-Ring statt übergroßem, unscharfem Rahmen.
- Minimap-Icon bleibt frei verschiebbar; ein Drag löst nicht mehr versehentlich zusätzlich das Öffnen des Addons aus.
- Minimap-Größe ist im Menü über `Minimap −` und `Minimap +` von 0,7x bis 1,45x einstellbar und wird gespeichert.

## [0.9.22-beta] – 2026-11-05

- Das redundante obere Navigations-HUD wird nicht mehr angezeigt; sichtbar bleibt der frei verschiebbare Pfeil mit Ziel, Entfernung und ETA.
- Oversized-Glow hinter dem Pfeil entfernt, der auf Forever doppelt und unscharf gerendert wurde.
- Den eigentlichen Navigationspfeil kompakter skaliert und die Live-Aktualisierung direkt an das sichtbare Pfeilfenster gebunden.

## [0.9.21-beta] – 2026-11-05

- Kritischer Navigationsfehler behoben: Forever liefert bei `GetWorldPosFromMapPos` teilweise Status `0` und den Vektor als zweiten Rückgabewert.
- Der numerische Statuswert wird nicht mehr als Vektor behandelt; dadurch bricht der Tracker-Refresh nicht mehr ab.
- Gear & Rewards zeigt Itemlevel als Fallback, wenn der Forever-Client keine Stat-Tabelle liefert, statt leer zu bleiben.
- Klassenansicht erhält immer ein erkennbares Profil mit Klasse, Stufe, Rolle und Datenstatus.
- Einstellungsseite auf die tatsächlich relevanten Route-, HUD- und Support-Schalter reduziert.
- Questtitel bevorzugen jetzt den lokalisierten Titel aus dem Questlog gegenüber englischen ForeverDB-Quelltiteln.

## [0.9.20-beta] – 2026-11-05

- Karten-Weltkoordinaten-Rückgabe abgesichert: Forever kann Status `0` plus Vektorobjekt zurückgeben.
- `Navigation.lua` behandelt numerische Statuswerte nicht mehr fälschlich als Vektor und verhindert dadurch den Tracker-Fehler an Zeile 107.
- Release auf `0.9.20-beta` angehoben.

## [0.9.19-beta] – 2026-11-05

- Navigationsauflösung korrigiert: aktuelle Zonenkarte wird vor der Kontinentkarte berücksichtigt.
- Forever-Classic-Builds setzen den Kartenkontext bei gleicher Questzone erneut, bevor „Gebietswechsel“ angezeigt wird.
- Zielpunkte wie NPC, Item, Gegner und Abgabe bleiben dadurch innerhalb derselben Zone richtbar.
- Release auf `0.9.19-beta` angehoben.

## [0.9.18-beta] – 2026-11-05

- Neuer Tab „Schnell leveln“ mit einer vorausberechneten Solo-Questroute aus Questlog, ForeverDB und Live-Questdaten.
- Bewertung berücksichtigt Levelpassung, aktuelle Zone, Kartenposition, Reiseaufwand, Folgequests, Koordinatenqualität und eigene XP-Messwerte.
- Aktive Questlog-Schritte werden immer vor theoretischen Questangeboten eingeordnet.
- Schnellmodus kann direkt im Tab aktiviert werden und verstärkt die Priorisierung der schnellen Solo-Route im Haupttracker.
- Unbekannte Quest-XP wird sichtbar als Schätzung markiert; gemessene XP ersetzen die Schätzung automatisch.
- Release auf `0.9.18-beta` angehoben.

## [0.9.17-beta] – 2026-11-05

- Ingame-Dashboard auf sechs Karten ausgebaut: Navigation-HUD, Questtracker, Routen-Score, XP/TTG, Minimap-Route und Datenstatus.
- Separater, frei verschiebbarer Navigationspfeil mit eigenem Zieltext, Entfernung, ETA und kurzem Status unter dem Pfeil.
- Pfeil aktualisiert sich weiter dynamisch mit Spielerposition und Blickrichtung; Farbe, Größe, Transparenz und Position bleiben über das Menü einstellbar.
- Kartenpositionen funktionieren zusätzlich über Forever-/Classic-Map-APIs, damit Ziele in derselben Zone nicht grundlos als Gebietswechsel erscheinen.
- Pfeil- und Dashboard-Texte werden gekürzt bzw. getrennt dargestellt, damit keine Zeilen und Buttons mehr ineinander laufen.
- Release auf `0.9.17-beta` angehoben.

## [0.9.16-beta] – 2026-11-05

- Navigation nutzt jetzt zusätzlich die klassische `GetPlayerMapPosition`-API des Forever-Clients.
- Dadurch werden Ziele in derselben Zone nicht mehr fälschlich als `Gebietswechsel erforderlich` angezeigt.
- Der Pfeil erhält wieder eine echte Richtung zu NPCs, Gegnern, Items und Abgaben und folgt der Spielerbewegung.
- Release auf `0.9.16-beta` angehoben.

## [0.9.15-beta] – 2026-11-05

- Legacy-Unicode-Pfeil vollständig deaktiviert; das alte lila Kästchen kann nicht mehr im großen HUD erscheinen.
- Pfeil aktualisiert jetzt etwa achtmal pro Sekunde und folgt Spielerposition sowie Blickrichtung geglättet.
- Weltkoordinaten-Richtung für Gebietswechsel ergänzt, wenn der Forever-Client diese Kartenwerte liefert.
- Quest-Vorschau zeigt den gesamten bekannten Questlog-Wert vorne an, zum Beispiel `6320 XP (9 Quests)`.
- Fertige, noch abzugebende Quests werden separat als `Abgabe bereit` ausgewiesen und bestimmen weiterhin `LEVEL UP READY`.
- Goldener Vorschau-Balken nutzt den Gesamtwert des Questlogs; die Bereitschaft bleibt korrekt auf fertige Quests begrenzt.
- Release auf `0.9.15-beta` angehoben.

## [0.9.14-beta] – 2026-11-05

- Navigationspfeil auf eine echte WoW-Minimap-Texture umgestellt; kein kaputtes Unicode-Kästchen mehr.
- Pfeil als eigenes, frei verschiebbares HUD mit Questziel, Entfernung und ETA darunter ergänzt.
- Detail-Navigation und kleiner Pfeil lassen sich unabhängig positionieren; UI-Sperre gilt für beide.
- Zieltext im großen Navigationsfeld gekürzt und entzerrt, damit Entfernung und Hinweise nicht mehr ineinander rutschen.
- Questlog-XP zählt bekannte Belohnungs-XP aller geloggten Quests; fertige Quest-XP bleibt separat für die Level-Up-Projektion.
- Questlog-Scan fällt auch dann auf die ältere WoW-API zurück, wenn die moderne API keine Einträge liefert.
- Release auf `0.9.14-beta` angehoben.

## [0.9.13-beta] – 2026-11-05

- Tracker-Feld vergrößert und neu ausgerichtet: Questtext, Zielbalken, Fortschritt und XP/TTG überlappen nicht mehr.
- Der Tracker zeigt klar `QUEST ANNEHMEN` bzw. `QUEST ABGEBEN` und blendet eine direkte Questaktion ein.
- Questaktionen arbeiten nur auf ausdrücklichen Button-Klick im geöffneten Blizzard-Questfenster; stille Hintergrund-Aktionen erlaubt der WoW-Client nicht.
- Release auf `0.9.13-beta` angehoben.

## [0.9.12-beta] – 2026-11-05

- Alte Navigation-SavedVariables werden beim Update vollständig entfernt; der HUD startet garantiert oben mittig.
- Legacy-Positionen überschreiben den sichtbaren Standardstart nicht mehr.
- Das Einstellungsmenü zeigt jetzt klar `Navigation: AN` oder `Navigation: AUS`.
- Release auf `0.9.12-beta` angehoben.

## [0.9.11-beta] – 2026-11-05

- Navigations-HUD wird beim ersten Start dieses Builds sichtbar zurückgesetzt, falls eine alte SavedVariables-Position ihn versteckt oder außerhalb des Bildschirms abgelegt hat.
- HUD liegt auf einer höheren UI-Ebene und der Richtungs-Pfeil wird deutlich größer gerendert.
- Release auf `0.9.11-beta` angehoben.

## [0.9.10-beta] – 2026-11-05

- Navigationspfeil erkennt jetzt Zonenkarten auch dann, wenn der Forever-Client für den Spieler nur die Kontinentkarte meldet.
- Fertige Quests erhalten ohne separaten Marker den bekannten QuestieDB-NPC-Punkt als Abgabe-Wegpunkt.
- Evergreen-Questgeber werden bei fehlendem Abgabe-Punkt als sicherer Fallback verwendet.
- Release auf `0.9.10-beta` angehoben.

## [0.9.9-beta] – 2026-11-05

- Quest-XP-Projektion wählt den Questlog-Eintrag vor der XP-Abfrage aus und unterstützt dadurch Forever-API-Varianten zuverlässiger.
- Fertige Quest-XP zeigt jetzt Anzahl der Quests, Gesamt-XP und Vorschau-Prozent an.
- Die Anzeige ergänzt „Level-Up in …“ auf Basis der gemessenen XP/h; ohne Messwerte steht sichtbar „wird gemessen“.
- XP-Projektionsbalken liegt sichtbar über der Blizzard-XP-Leiste.
- Release auf `0.9.9-beta` angehoben.

## [0.9.8-beta] – 2026-11-05

- Offene Questziele im Questlog werden vor fertigen, noch nicht abgegebenen Quests priorisiert.
- Der Navigationspfeil führt nach dem Erledigen direkt zur nächsten offenen Quest; die fertige Quest bleibt anschließend als Abgabe-Schritt verfügbar.
- Release auf `0.9.8-beta` angehoben.

## [0.9.7-beta] – 2026-11-05

- Navigations-HUD liegt jetzt über dem Hauptfenster und startet sichtbar am oberen Bildschirmrand; der Pfeil bleibt verschiebbar.
- Tooltip-Scanning gegen Forever-Clientvarianten abgesichert; ein inkompatibler `HookScript` kann den Addon-Start nicht mehr abbrechen.
- Release auf `0.9.7-beta` angehoben.

## [0.9.6-beta] – 2026-11-05

- Aktive Questtitel werden im Tracker aus dem echten Questlog übernommen; lokalisierte Titel wie „Die Verdammten“ bleiben sichtbar.
- Evergreen-Zielpunkte werden bei bekannten Questtiteln auch ohne Quest-ID-Verknüpfung als Wegpunkt-Fallback verwendet.
- UI-Fehler beim Einfärben der Routenbuttons behoben (`FontString:SetTextColor` statt Button-Methode).
- ForeverPath ruft keine ForeverGuild-Funktionen mehr aus dem Layer-Refresh auf, damit geschützte/Secret-Werte nicht zwischen den Addons getaintet werden.
- XP-, Session- und Aura-Auswertung defensiver gegen geschützte Clientwerte gemacht.

## [0.9.5-beta] – 2026-11-05

- Der aktive Questlog ist jetzt die primäre Quelle für die Route: laufende Quests werden vor allgemeinen Datenbank-Angeboten eingeplant.
- Questphasen werden aus dem echten Clientstatus abgeleitet: Ziele zuerst erledigen, fertige Quests zur Abgabe priorisieren und danach neu planen.
- Questlog-Einträge werden auch bei älteren Client-APIs sicher erkannt; Titelabgleich und unbekannte Quest-IDs bleiben als Live-Schritt sichtbar.
- Der Navigationspfeil nutzt den aktuellen Blizzard-Questmarker als Fallback und kennzeichnet Ziel-, Gegner- und Item-Schritte genauer.
- Nahe Annahmequests und Folgequests werden erst nach den aktiven Questlog-Schritten in die Route aufgenommen.
- Release auf `0.9.5-beta` angehoben.

## [0.9.4-beta] – 2026-11-04

- Quest-XP-Projektion über der Blizzard-XP-Leiste ergänzt: fertige Quest-XP, Vorschauwert und „LEVEL UP READY!“.
- Questbelohnungs-XP nutzt sichere Client-APIs und einen versteckten Tooltip-Fallback; unbekannte Werte bleiben sichtbar als geschätzt markiert.
- XP-Session in Kill-, Quest-, sonstige XP sowie Reise-/Kampfzeit aufgeteilt; TTG nutzt einen gewichteten gleitenden Mittelwert über bis zu zehn Minuten.
- Navigations-HUD um einen mehrschichtigen 3D-Style-Pfeil und einen optionalen effizienten EP-Mob-Wegpunkt erweitert.
- Pfeilgröße, Pfeilfarbe, Pfeilstil, EP-Mob-Priorität und Layer-Hinweise sind über das Ingame-Menü einstellbar; der HUD bleibt verschiebbar.
- Mouseover-/Target-Tooltips zeigen geschätzte Mob-XP, Level-Prozent und Kills bis zum Level-Up; beobachtete XP-Gewinne verbessern die Schätzung lokal.
- Layer-Routing ergänzt: lokale Überfarm-Indikatoren, ForeverGuild-Adapter, sichtbarer Wechselvorschlag; kein automatisches Layer-Hopping ohne öffentliche API.
- ForeverDB-Importer speichert API-Metadaten und kann im erweiterten Lauf Items und Spells kompakt importieren; der GitHub-Refresh nutzt den erweiterten Lauf.
- API-Key bleibt außerhalb von Repository, Addon und ZIP.
- Extended-Refresh fängt vorübergehende ForeverDB-5xx-Fehler bei optionalen Item-/Spell-Endpunkten mit Retries ab; der Questimport kann dadurch trotzdem sauber abgeschlossen werden.

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
