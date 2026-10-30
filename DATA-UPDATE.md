# ForeverDB-Daten aktualisieren

Die ZIP enthält einen statischen, dokumentierten Datenstand. Das Addon fragt ForeverDB nicht live ab und enthält niemals einen API-Schlüssel.

1. Einen persönlichen Schlüssel auf [ForeverDB Developers](https://foreverdb.net/developers) erzeugen.
2. Den Schlüssel nur lokal als Umgebungsvariable setzen: `FOREVERDB_API_KEY`.
3. Im Repository ausführen: `python tools/import_foreverdb.py`.
4. Die erzeugten Dateien aus `build/ForeverPath/ExternalData/` in den lokalen Addon-Quellstand übernehmen, ZIP neu bauen und `CHANGELOG.md` ergänzen.
5. Vor dem Commit prüfen, dass weder der Schlüssel noch private API-Antworten außerhalb der vorgesehenen lokalen Datenimportdateien liegen.

Importiert werden Questdaten sowie die öffentlichen Zusatzendpunkte für Dungeons, Klassen, Berufe und Zonen. Die sichtbare Attribution `Data from ForeverDB.net (https://foreverdb.net)` bleibt im Addon erhalten.

Der Importer behandelt den Schlüssel ausschließlich im Speicher und schreibt ihn nicht in Dateien. Bei Verdacht auf Offenlegung den Schlüssel auf der Developer-Seite sofort widerrufen und einen neuen erzeugen.
