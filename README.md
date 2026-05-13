# CoffeeTime Standortanalyse

- **Course:** KI mit Python (Sommersemester 2026)
- **Deadline:** May 28, 2026, 12:00 PM
- **Team Members:** Samuel Atama, Malik Yildizhan, Santiago Meijide, Julian Soady, Elyas Mouhkli
- **Target Group:** WIMBIT23A

Dieses Projekt analysiert vorhandene Filialdaten und potenzielle neue Standorte in Deutschland. Ziel ist es, den erwarteten jährlichen Umsatz (Annual Turnover in kEUR) neuer CoffeeTime-Filialen vorherzusagen und die zehn besten Empfehlungen in einem klar strukturierten Ausgabeordner abzulegen.

---

## 📁 Projektstruktur

```
KI_Assignment2/
├── files/
│   ├── coffee_chain_stores_2024.csv           (Historische Filial-Daten)
│   └── potential_store_locations_germany.csv  (50 potenzielle Standorte)
├── python/
│   ├── test.py                      (Hauptskript: Daten → Modell → Prognosen)
│   ├── generate_report_pdf.py       (PDF-Generierung)
│   └── requirements.txt             (Python-Abhängigkeiten)
├── outputs/                         (Automatisch erzeugt nach Ausführung)
│   ├── csv/                        (Daten-Exports)
│   ├── png/                        (Visualisierungen)
│   └── other/                      (Markdown & PDF Berichte)
└── README.md                        (Diese Datei)
```

---

## 🔧 Installation & Voraussetzungen

### Python-Abhängigkeiten

```bash
pip install -r python/requirements.txt
```

Die folgenden Bibliotheken werden benötigt:

- **pandas** – Datenmanipulation
- **scikit-learn** – Machine Learning (Linear & Polynomial Regression)
- **matplotlib & seaborn** – Visualisierungen
- **reportlab** – PDF-Generierung

---

## ▶️ Ausführung

### Von der Projektwurzel aus (empfohlen):

```bash
# Hauptpipeline ausführen
python3 python/test.py

# Optional: PDF-Bericht generieren
python3 python/generate_report_pdf.py
```

### Oder aus dem `python/`-Verzeichnis:

```bash
cd python
python3 test.py
python3 generate_report_pdf.py
```

---

## 📊 Ausgabedateien

Nach der Ausführung entstehen folgende Dateien im `outputs/`-Ordner:

### CSV-Dateien (`outputs/csv/`)

| Datei                        | Inhalt                                                    |
| ---------------------------- | --------------------------------------------------------- |
| `model_metrics.csv`          | Modellgüte (MSE, MAE, R²) für Linear & Polynomial Modelle |
| `predicted_locations.csv`    | Alle 50 Standorte mit Umsatzprognose                      |
| `top_10_recommendations.csv` | Top 10 beste Standorte                                    |

### Visualisierungen (`outputs/png/`)

| Datei                               | Inhalt                                  |
| ----------------------------------- | --------------------------------------- |
| `annual_turnover_distribution.png`  | Histogramm des historischen Umsatzes    |
| `predicted_profit_distribution.png` | Histogramm der prognostizierten Umsätze |

### Berichte (`outputs/other/`)

| Datei                       | Inhalt                                       |
| --------------------------- | -------------------------------------------- |
| `recommendation_report.md`  | Markdown-Bericht mit Analysen & Empfehlungen |
| `recommendation_report.pdf` | PDF-Version des Berichts (optional)          |

---

## 🎯 Pipeline-Überblick

1. **Datenladen** – CSV-Dateien aus `files/` werden geladen
2. **Datenaufbereitung** – Feature-Engineering, One-Hot-Encoding, Imputation
3. **Train/Test-Split** – 80/20 Aufteilung
4. **Modelltraining** – Linear & Polynomial Regression getestet
5. **Evaluation** – MSE, MAE, R² berechnet
6. **Finales Training** – Bestes Modell auf gesamtem Datensatz trainiert
7. **Vorhersagen** – Umsatz für 50 potenzielle Standorte prognostiziert
8. **Ranking & Export** – Top 10 als CSV, Visualisierungen & Bericht generiert

---

## 📝 Hinweise

- Der Ausgabeordner `outputs/` wird automatisch im Projektstamm erzeugt
- Alle Pfade nutzen `Path(__file__).resolve()` für Robustheit
- Modell mit bester R²-Wertung wird für finale Vorhersagen verwendet
- Die zehn besten Standorte sind nach prognostiziertem Umsatz sortiert
