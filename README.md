# ForeverPath

Eigenständiges Leveling- und Routen-Addon für **World of Warcraft: Forever**.

ForeverPath zeigt dir den nächsten sinnvollen Questschritt, setzt Wegpunkte, bewertet Alternativen und verfolgt deinen Fortschritt. Das Design und die Routenlogik sind eigenständig und enthalten keine RestedXP-Quelltexte, Grafiken, Texte oder geschützten Guide-Inhalte.

Die aktuelle Version enthält questgenaue Annahme-/Ziel-/Abgabeschritte, aktuelle-Zone-Filter, automatische Route-Recovery, Reisehinweise, Minimap- und Weltkarten-Navigation, einen **Gear & Rewards**-Tab, XP/h-Lernwerte, Trainer-/Berufsstopps, Gruppenlogik, Questketten-/Zonenfortschritt und Streamer-Layouts.

## Installation

1. Öffne auf GitHub die Repository-Seite und klicke auf **Code → Download ZIP**. Dadurch wird `LvL-Guide-main.zip` heruntergeladen.
2. Entpacke `LvL-Guide-main.zip` zunächst. Darin liegt die Datei `ForeverPath.zip`.
3. Öffne/entpacke jetzt auch `ForeverPath.zip`. Erst darin liegt der eigentliche Ordner `ForeverPath` mit der Datei `ForeverPath.toc`.
4. Kopiere den kompletten Ordner `ForeverPath` nach:

   ```text
   <WoW-Forever-Installationsordner>/Interface/AddOns/
   ```

   Danach muss die Datei `ForeverPath.toc` direkt hier liegen:

   ```text
   .../Interface/AddOns/ForeverPath/ForeverPath.toc
   ```

5. Starte WoW Forever und öffne die Addon-Auswahl am Charakterbildschirm.
6. Aktiviere **ForeverPath**. Falls der Client es anbietet, kannst du „Veraltete Addons laden“ aktivieren.
7. Im Spiel findest du das verschiebbare ForeverPath-Symbol an der Minimap. Linksklick öffnet das Menü, Ziehen verschiebt das Symbol.

**Wichtig:** Verwende den Installationsordner des Forever-Clients, nicht den Retail- oder Classic-Ordner. Der konkrete Ordnername kann je nach Battle.net-Version abweichen; entscheidend ist, dass darin der Forever-Client und anschließend `Interface\AddOns` liegen. Am Ende darf der Pfad nicht doppelt verschachtelt sein. Falsch wäre zum Beispiel `AddOns/ForeverPath.zip/ForeverPath` oder `AddOns/ForeverPath/ForeverPath/ForeverPath.toc`.

## Bedienung im Spiel

- **Minimap-Symbol:** Menü öffnen, verschieben oder per Rechtsklick Route analysieren
- **Tracker:** zeigt aktuellen Schritt, Questziel, Fortschritt, Score, XP/h und Tode
- **Navigations-HUD:** Richtung, Zielart, Entfernung und geschätzte Reisezeit
- **Weltkarte:** Linie zum aktuellen Ziel und kommende Routenpunkte
- **Route sync:** findet nach einem übersprungenen Schritt automatisch einen passenden Schritt in der aktuellen Zone
- **Jetzt analysieren:** startet den Quest- und Routen-Scan sofort
- Automatischer Scan beim Login und anschließend alle fünf Minuten
- Quest-ID-Verknüpfung mit NPC, Ziel, Abgabe, Folgequest und Live-Objektiven
- Tracker-Fortschrittsbalken, Restziele, Einklappen und Skalierung
- automatische Route-Recovery, erledigte-Schritte-Überspringen und Score-Alternativen
- Trainer-, Berufs-, Gasthof-, Flugpunkt-, Reparatur- und Hauptstadtstopp-Empfehlungen
- Gear-Profile für Auto, DPS, Tank und Heiler sowie Questbelohnungs-Vergleich
- gespeicherte Fensterpositionen, UI-Sperre, Transparenz, Schriftgröße und Minimalmodus
- Fehlerbericht-Export für Discord und Datenstatus mit ForeverDB-Build

Die Bedienung läuft vollständig über das verschiebbare Minimap-Symbol, den Tracker und die sichtbaren Buttons im Menü. Chatbefehle sind nicht erforderlich.

## Was das Addon bewertet

Die Empfehlung berücksichtigt unter anderem:

- XP pro Minute
- Reise-, Kampf- und Risikokosten
- Gruppenwartezeit und Rollenbonus
- Klassen- und Questkettenbonus
- Folgequestwert
- Ausrüstungszustand und mögliche Questbelohnungs-Upgrades
- Dungeon-Level, Gruppengröße, ForeverDB-Status und heuristischen Gear-/Loot-Bedarf
- aktuelle Zone und bereits erledigte Schritte

XP/h, Sessionzeit und Todesfälle werden lokal aus deiner tatsächlichen Spielsitzung erfasst. Fehlende Laufzeit- oder Lootwerte werden im Addon als Schätzung behandelt.

## Kompatibilität

Der aktuelle Build nutzt `Interface: 16001`, die derzeit dokumentierte Forever-Schnittstelle. Die Interface-Zeile und das Addon müssen nach jedem Client-Update im echten Spiel geprüft werden.

Ein echter Client-Test ist immer wichtiger als die Versionsnummer: Wenn das Addon nicht erscheint, zuerst den Installationspfad und die Ordnerstruktur prüfen.

## Datenquellen und API-Key

Das Addon enthält einen statischen, dokumentierten Datenstand. Es fragt ForeverDB im Spiel nicht live ab. Der ForeverDB-API-Key ist **nicht** in der ZIP und wird nicht benötigt, um das Addon zu installieren.

Enthaltene öffentliche Quellen:

- [ForeverDB API](https://foreverdb.net/developers) für Quest-, Dungeon-, Klassen-, Berufs-, Zonen- und bestätigte Änderungsdaten
- [QuestieDB-Forever / Forever Quest Pins](https://github.com/TylerAkins/forever-quest-markers)
- [Evergreen for WoW Forever](https://github.com/Dj2Swagittarius/evergreen-wow-forever)

Die vollständigen Attributionen, Lizenztexte und Import-Hinweise liegen im Addon unter `ExternalData/`. Die sichtbare Quellenangabe `Data from ForeverDB.net (https://foreverdb.net)` bleibt im Menü und Tracker erhalten.

## Daten aktualisieren

Für Entwickler liegt unter [`DATA-UPDATE.md`](./DATA-UPDATE.md) die Anleitung für neue lokale ForeverDB-Daten. Der Importer [`tools/import_foreverdb.py`](./tools/import_foreverdb.py) liest den persönlichen Schlüssel ausschließlich aus `FOREVERDB_API_KEY` und schreibt ihn nicht in Dateien.

Bitte niemals einen API-Key committen oder in die Addon-ZIP packen. Bei versehentlicher Offenlegung den Schlüssel auf der ForeverDB-Developer-Seite widerrufen und einen neuen erstellen.

## Changelog

Die Versionshistorie steht in [`CHANGELOG.md`](./CHANGELOG.md).

## Kontakt

Fragen, Fehlerberichte und Vorschläge gerne über Discord:

**Discord: `pacco1234`**

Bitte bei Fehlern möglichst Client-Version, Screenshot, reproduzierbare Schritte und den betroffenen Charakter-/Routenmodus mitschicken.

## Lizenzhinweis

ForeverPath wird als Community-Projekt bereitgestellt. Die jeweiligen offenen Datenquellen und deren Lizenzbedingungen bleiben unter `ExternalData/` dokumentiert. World of Warcraft und seine Inhalte gehören Blizzard Entertainment, Inc.
