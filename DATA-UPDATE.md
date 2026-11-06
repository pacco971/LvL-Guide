# ForeverDB-Daten aktualisieren

Die ZIP enthält einen statischen, dokumentierten Datenstand. Das Addon fragt ForeverDB nicht live ab und enthält niemals einen API-Schlüssel.

1. Einen persönlichen Schlüssel auf [ForeverDB Developers](https://foreverdb.net/developers) erzeugen.
2. Den Schlüssel nur lokal als Umgebungsvariable setzen: `FOREVERDB_API_KEY`.
3. Im Repository ausführen: `python tools/import_foreverdb.py`.
   Für den vollständigen Zusatzimport (Itemsets, Händler, Gifte, Disenchant,
   Battlegrounds, Items, Spells und Details der bekannten Dungeons) optional
   `python tools/import_foreverdb.py --extended` verwenden. Dieser Lauf macht
   mehr API-Anfragen und sollte deshalb nur gezielt ausgeführt werden. Der
   Extended-Lauf prüft zusätzlich die kleinen öffentlichen Endpunkte
   `/builds`, `/builds/latest`, `/buffs-nerfs` und `/merchants-favor`; fallen
   diese temporär aus, bleibt der Questimport trotzdem verwendbar.
4. Die erzeugten Dateien aus `build/ForeverPath/ExternalData/` in den lokalen Addon-Quellstand übernehmen, ZIP neu bauen und `CHANGELOG.md` ergänzen.
5. Vor dem Commit prüfen, dass weder der Schlüssel noch private API-Antworten außerhalb der vorgesehenen lokalen Datenimportdateien liegen.

Importiert werden Questdaten sowie die öffentlichen Zusatzendpunkte für Dungeons, Klassen, Berufe, Zonen und `changes-seen` mit `verified=1`. Der optionale Extended-Lauf ergänzt Itemsets, Händler, Gifte, Disenchant, Battlegrounds, kompakte Item-/Spell-Felder, API-Metadaten und Dungeon-Details. Damit kommen bestätigte Beobachtungen zu Quest-XP, Belohnungen, Itemwerten und NPC-Daten in den lokalen Datenstand. Die sichtbare Attribution `Data from ForeverDB.net (https://foreverdb.net)` bleibt im Addon erhalten.

Der Importer behandelt den Schlüssel ausschließlich im Speicher und schreibt ihn nicht in Dateien. Bei Verdacht auf Offenlegung den Schlüssel auf der Developer-Seite sofort widerrufen und einen neuen erzeugen. Ein gleicher ForeverDB-Build bedeutet nicht automatisch, dass keine verifizierten Hotfixdaten hinzugekommen sind; deshalb gehört der Hotfix-Snapshot zum sichtbaren Datenstatus.

## Automatischer Refresh

Der Workflow läuft regulär täglich und kann über **Actions → Refresh ForeverPath from ForeverDB → Run workflow** gestartet werden. Als Login-unabhängiger Fallback startet ein Push auf `.github/refresh-foreverdb.trigger` ausschließlich diesen Datenrefresh.

Der Workflow [`.github/workflows/refresh-foreverdb.yml`](./.github/workflows/refresh-foreverdb.yml) prüft ForeverDB täglich und kann zusätzlich manuell gestartet werden. Er verwendet den Extended-Lauf, baut die ZIP nur bei einem tatsächlich geänderten Datenstand neu, lädt sie anschließend zu CurseForge hoch und speichert die aktualisierte `ForeverPath.zip` wieder im Repository.

Dafür müssen unter den GitHub-Repository-Secrets vorhanden sein:

- `FOREVERDB_API_KEY`: persönlicher ForeverDB-Schlüssel
- `CF_API_TOKEN`: CurseForge-Upload-Token

Keiner dieser Schlüssel wird in die ZIP oder in Git-Dateien geschrieben.
