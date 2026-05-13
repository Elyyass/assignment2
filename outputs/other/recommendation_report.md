# Empfehlung: Neue CoffeeTime-Standorte in Deutschland

## Ergebnisüberblick
Basierend auf dem historischen Datensatz wurden lineare und polynomiale Regressionsmodelle
trainiert. Das beste Modell wurde anhand des $R^2$-Wertes auf dem Testdatensatz gewählt.

### Modellgüte
| model      |         mse |     mae |     r2 |
|:-----------|------------:|--------:|-------:|
| Linear     | 1.51347e+09 | 28476.5 | 0.635  |
| Polynomial | 3.36185e+09 | 44656.9 | 0.1893 |

### Top 10 Standorte nach vorhergesagter Umsatzprognose
| potential_location_id   | city       |   predicted_annual_turnover_kEUR |   population_density |   median_household_income |   number_of_competitors_1km |   traffic_count_nearby |   walkability_score |
|:------------------------|:-----------|---------------------------------:|---------------------:|--------------------------:|----------------------------:|-----------------------:|--------------------:|
| POT_LOC_022             | Berlin     |                           255850 |              4612.75 |                   52637.3 |                           4 |                   3425 |            0.929758 |
| POT_LOC_036             | Düsseldorf |                           239461 |              8356.14 |                   60465.6 |                           2 |                   1633 |            0.829328 |
| POT_LOC_002             | Leipzig    |                           219981 |              5884.37 |                   49234.8 |                           2 |                   2503 |            0.813371 |
| POT_LOC_058             | Berlin     |                           212205 |              4812.35 |                   48844.6 |                           5 |                   2339 |            0.791808 |
| POT_LOC_079             | Hamburg    |                           205028 |              7141.52 |                   48266.7 |                           3 |                    749 |            0.582357 |
| POT_LOC_006             | Berlin     |                           202754 |              4838.27 |                   50959.8 |                           2 |                   1325 |            0.763378 |
| POT_LOC_053             | Essen      |                           180004 |              3655.41 |                   48467.9 |                           1 |                   2177 |            0.633395 |
| POT_LOC_064             | Hamburg    |                           179000 |              2564.7  |                   40109.8 |                           5 |                   3822 |            0.90887  |
| POT_LOC_038             | Berlin     |                           176673 |              4308.83 |                   43102.1 |                           4 |                   2309 |            0.811326 |
| POT_LOC_024             | Hamburg    |                           166513 |              5130.37 |                   45975.4 |                           4 |                   2122 |            0.593353 |

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
