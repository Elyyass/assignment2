# CoffeeTime Standortanalyse

- **Course:** KI mit Python (Sommersemester 2026)
- **Deadline:** May 28, 2026, 12:00 PM
- **Team Members:** Samuel Atama, Malik Yildizhan, Santiago Meijide, Julian Soady, Elyas Mouhkli
- **Target Group:** WIMBIT23A

Dieses Projekt analysiert vorhandene Filialdaten und potenzielle neue Standorte in Deutschland. Ziel ist es, die erwartete monatliche Profitabilität neuer CoffeeTime-Filialen vorherzusagen und die fünf besten Empfehlungen in einem klar strukturierten Ausgabeordner abzulegen.

## Projektübersicht

- Eingabedaten:
  - `files/coffee_chain_stores_2024.csv`
  - `files/potential_store_locations_germany.csv`
- Hauptskript:
  - `python/test.py` – Lädt Daten, bereitet sie auf, trainiert Modelle und erstellt Prognosen.
- Berichtserstellung:
  - `python/generate_report_pdf.py` – Erzeugt optional ein PDF aus dem generierten Markdown-Bericht.
- Ausgabeordner:
  - `outputs/csv/`
  - `outputs/png/`
  - `outputs/other/`

## Struktur der Ausgaben

Nach der Ausführung von `python/test.py` entstehen folgende Dateien:

- `outputs/csv/model_metrics.csv` – Auswertung der Modellgüte für alle getesteten Modelle.
- `outputs/csv/predicted_locations.csv` – Alle potenziellen Standorte mit vorhergesagten Renditen.
- `outputs/csv/top_5_recommendations.csv` – Die fünf besten Standortempfehlungen.
- `outputs/png/monthly_profit_distribution.png` – Histogramm der historischen Profitabilität.
- `outputs/png/predicted_profit_distribution.png` – Histogramm der prognostizierten Profitabilität.
- `outputs/other/recommendation_report.md` – Zusammenfassender Bericht mit Ergebnissen und Empfehlungen.

Optional erzeugt `python/generate_report_pdf.py` eine PDF-Version des Berichts in:

- `outputs/other/recommendation_report.pdf`

## Voraussetzungen

Die Skripte benötigen folgende Python-Bibliotheken. Alternativ kannst du `python/requirements.txt` verwenden:

- pandas
- scikit-learn
- matplotlib
- seaborn
- reportlab

## Ausführung

1. Wechsle ins Python-Verzeichnis:
   - `cd python`
2. Starte die Hauptpipeline:
   - `python test.py`
3. Optional: Erstelle das PDF aus dem Markdown-Bericht:
   - `python generate_report_pdf.py`

## Hinweise

- Der Ausgabeordner `outputs/` wird jetzt im Projektstamm erzeugt.
- CSV-Daten werden unter `outputs/csv/` abgelegt, Diagramme unter `outputs/png/` und Text-/Berichtsdateien unter `outputs/other/`.
- So sind Ergebnisse klar getrennt und leichter weiterzuverwenden.
