# Empfehlung: Neue CoffeeTime-Standorte in Deutschland

## Ergebnisüberblick
Basierend auf dem historischen Datensatz wurden lineare und polynomiale Regressionsmodelle
trainiert. Das beste Modell wurde anhand des $R^2$-Wertes auf dem Testdatensatz gewählt.

### Modellgüte
| model      |         mse |     r2 |
|:-----------|------------:|-------:|
| Linear     | 1.47208e+06 | 0.5585 |
| Polynomial | 2.8438e+06  | 0.1471 |

### Top 5 Standorte nach vorhergesagter Profitabilität
| potential_location_id   | city       |   predicted_monthly_profit |   population_density |   median_household_income |   number_of_competitors_1km |   traffic_count_nearby |   walkability_score |
|:------------------------|:-----------|---------------------------:|---------------------:|--------------------------:|----------------------------:|-----------------------:|--------------------:|
| POT_LOC_022             | Berlin     |                    6937.13 |              4612.75 |                   52637.3 |                           4 |                   3425 |            0.929758 |
| POT_LOC_036             | Düsseldorf |                    6576.94 |              8356.14 |                   60465.6 |                           2 |                   1633 |            0.829328 |
| POT_LOC_002             | Leipzig    |                    6060.34 |              5884.37 |                   49234.8 |                           2 |                   2503 |            0.813371 |
| POT_LOC_058             | Berlin     |                    5852.96 |              4812.35 |                   48844.6 |                           5 |                   2339 |            0.791808 |
| POT_LOC_079             | Hamburg    |                    5691.42 |              7141.52 |                   48266.7 |                           3 |                    749 |            0.582357 |

## Grenzen und reale Einflussfaktoren
- **Nicht beobachtbare Faktoren:** Mietverhandlungen, lokale Marketingeffekte oder Konkurrenzaktionen
  sind nicht im Datensatz enthalten.
- **Saisonalität/Trends:** Die Daten repräsentieren nur das Jahr 2024. Änderungen in 2025 oder
  spätere Trends können die tatsächliche Performance beeinflussen.
- **Datenqualität:** Die synthetische Herkunft der Daten kann zu Verzerrungen oder unrealistischen
  Verteilungen führen.
- **Modellannahmen:** Lineare bzw. polynomiale Modelle bilden nur begrenzt komplexe Zusammenhänge ab.

## Empfehlung
Die oben genannten Standorte sollten für die nächste Expansionsrunde priorisiert geprüft werden.
Eine finale Entscheidung sollte zusätzlich qualitative Standortanalysen, Mietkonditionen und
aktuelle Marktbeobachtungen berücksichtigen.
