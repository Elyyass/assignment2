# Programming Assignment 2 – CoffeeTime Standortanalyse

Dieses Projekt implementiert eine vollständige Data-Science-Pipeline zur Vorhersage der erwarteten Profitabilität neuer CoffeeTime-Filialen in Deutschland. Die Auswertung basiert auf den bereitgestellten CSV-Datensätzen und liefert eine Rangliste der fünf besten Standorte.

## Group Submission Details

- **Course:** KI mit Python (Sommersemester 2026)
- **Deadline:** May 28, 2026, 12:00 PM
- **Team Members:** Samuel Atama, Malik Yildizhan, Santiago Meijide, Julian Soady, Elyas Mouhkli
- **Target Group:** WIMBIT23A

## Requirements

Zur Ausführung der Skripte werden folgende Python-Bibliotheken benötigt:

- pandas: Zur Datenmanipulation und Analyse der CSV-Dateien.
- scikit-learn: Für das Training des Machine Learning Modells (Random Forest Regressor).
- matplotlib & seaborn: Zur Visualisierung der Datenverteilungen und Vorhersagen.
- reportlab: Zur automatischen Generierung des geforderten PDF-Berichts.
- tabulate: Zur Formatierung von Tabellendaten innerhalb der Skripte.

## Inhalte

- `test.py`: Vollständiges Python-Skript mit Datenaufbereitung, Modelltraining, Evaluation und Ranking.
- `outputs/`: Automatisch erzeugte Ergebnisse (CSV, PNG und Report).

## Ausführung

1. Virtuelle Umgebung aktivieren.
2. Script starten: `python test.py`

## Ergebnisse

Nach dem Lauf befinden sich folgende Dateien im Ordner `outputs/`:

- `top_5_recommendations.csv`: Top-5-Standorte
- `predicted_locations.csv`: Alle Standorte mit Prognose
- `model_metrics.csv`: Modellgüte
- `recommendation_report.md`: Bericht mit Modellreflexion
- `monthly_profit_distribution.png`, `predicted_profit_distribution.png`: Visualisierungen

## PDF-Bericht

Für die Abgabe kann `outputs/recommendation_report.md` bei Bedarf in ein PDF konvertiert werden (z. B. über einen Markdown-zu-PDF-Exporter).
