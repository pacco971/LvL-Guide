# ForeverDB-Daten aktualisieren

Die ZIP enthält einen statischen, dokumentierten Datenstand. Das Addon fragt ForeverDB nicht live ab und enthält niemals einen API-Schlüssel.

1. Einen persönlichen Schlüssel auf [ForeverDB Developers](https://foreverdb.net/developers) erzeugen.
2. Den Schlüssel nur lokal als Umgebungsvariable setzen: `FOREVERDB_API_KEY`.
3. Im Repository ausführen: `python tools/import_foreverdb.py`.
4. Die erzeugten Dateien aus `build/ForeverPath/ExternalData/` in den lokalen Addon-Quellstand übernehmen, ZIP neu bauen und `CHANGELOG.md` ergänzen.
5. Vor dem Commit prüfen, dass weder der Schlüssel noch private API-Antworten außerhalb der vorgesehenen lokalen Datenimportdateien liegen.

Importiert werden Questdaten sowie die öffentlichen Zusatzendpunkte für Dungeons, Klassen, Berufe, Zonen und `changes-seen` mit `verified=1`. Damit kommen bestätigte Beobachtungen zu Quest-XP, Belohnungen, Itemwerten und NPC-Daten in den lokalen Datenstand. Die sichtbare Attribution `Data from ForeverDB.net (https://foreverdb.net)` bleibt im Addon erhalten.

Der Importer behandelt den Schlüssel ausschließlich im Speicher und schreibt ihn nicht in Dateien. Bei Verdacht auf Offenlegung den Schlüssel auf der Developer-Seite sofort widerrufen und einen neuen erzeugen.

## Automatischer Refresh

Der Workflow [`.github/workflows/refresh-foreverdb.yml`](./.github/workflows/refresh-foreverdb.yml) prüft ForeverDB täglich und kann zusätzlich manuell gestartet werden. Er baut die ZIP nur bei einem tatsächlich geänderten Datenstand neu, lädt sie anschließend zu CurseForge hoch und speichert die aktualisierte `ForeverPath.zip` wieder im Repository.

Dafür müssen unter den GitHub-Repository-Secrets vorhanden sein:

- `FOREVERDB_API_KEY`: persönlicher ForeverDB-Schlüssel
- `CF_API_TOKEN`: CurseForge-Upload-Token

Keiner dieser Schlüssel wird in die ZIP oder in Git-Dateien geschrieben.
