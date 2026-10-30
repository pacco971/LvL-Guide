# ForeverPath

Eigenständiges Leveling- und Routen-Addon für **World of Warcraft: Forever**.

ForeverPath zeigt dir den nächsten sinnvollen Questschritt, setzt Wegpunkte, bewertet Alternativen und verfolgt deinen Fortschritt. Das Design und die Routenlogik sind eigenständig und enthalten keine RestedXP-Quelltexte, Grafiken, Texte oder geschützten Guide-Inhalte.

## Installation

1. Lade die Datei [`ForeverPath.zip`](./ForeverPath.zip) herunter.
2. Öffne den ZIP-Ordner und entpacke den enthaltenen Ordner `ForeverPath`.
3. Kopiere den kompletten Ordner nach:

   ```text
   <WoW-Forever-Ordner>/_classic_beta_/Interface/AddOns/
   ```

   Danach muss die Datei `ForeverPath.toc` direkt hier liegen:

   ```text
   .../_classic_beta_/Interface/AddOns/ForeverPath/ForeverPath.toc
   ```

4. Starte WoW Forever und öffne die Addon-Auswahl am Charakterbildschirm.
5. Aktiviere **ForeverPath**. Falls der Client es anbietet, kannst du „Veraltete Addons laden“ aktivieren.
6. Im Spiel findest du das verschiebbare ForeverPath-Symbol an der Minimap. Linksklick öffnet das Menü, Ziehen verschiebt das Symbol.

## Bedienung im Spiel

- **Minimap-Symbol:** Menü öffnen, verschieben oder per Rechtsklick Route analysieren
- **Tracker:** zeigt aktuellen Schritt, Questziel, Fortschritt, Score, XP/h und Tode
- **Navigations-HUD:** Richtung, Zielart, Entfernung und geschätzte Reisezeit
- **Weltkarte:** Linie zum aktuellen Ziel und kommende Routenpunkte
- **Route sync:** findet nach einem übersprungenen Schritt automatisch einen passenden Schritt in der aktuellen Zone
- **Jetzt analysieren:** startet den Quest- und Routen-Scan sofort
- Automatischer Scan beim Login und anschließend alle fünf Minuten

Die Chatbefehle bleiben optional:

```text
/fp
/fp next
/fp prev
/fp scan
/fp data
/fp reset
```

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

Der aktuelle Build ist für `Interface: 16001` und den dokumentierten WoW-Forever-Beta-Stand gepackt. Wenn der Client später eine andere Interface-Version verlangt, muss die Interface-Zeile in `ForeverPath.toc` angepasst und im Spiel getestet werden.

Ein echter Client-Test ist immer wichtiger als die Versionsnummer: Wenn das Addon nicht erscheint, zuerst den Installationspfad und die Ordnerstruktur prüfen.

## Datenquellen und API-Key

Das Addon enthält einen statischen, dokumentierten Datenstand. Es fragt ForeverDB im Spiel nicht live ab. Der ForeverDB-API-Key ist **nicht** in der ZIP und wird nicht benötigt, um das Addon zu installieren.

Enthaltene öffentliche Quellen:

- [ForeverDB API](https://foreverdb.net/developers) für Quest-, Dungeon-, Klassen-, Berufs- und Zonendaten
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
