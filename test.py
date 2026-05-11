from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, PolynomialFeatures, StandardScaler

matplotlib.use("Agg")


DATA_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = DATA_DIR / "outputs"
RANDOM_STATE = 42


@dataclass
class ModelResult:
	name: str
	pipeline: Pipeline
	mse: float
	r2: float


def load_data() -> tuple[pd.DataFrame, pd.DataFrame]:
	stores = pd.read_csv(DATA_DIR / "coffee_chain_stores_2024.csv")
	locations = pd.read_csv(DATA_DIR / "Potential Store Locations Germany.csv")
	return stores, locations


def prepare_datasets(
	stores: pd.DataFrame, locations: pd.DataFrame
) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.DataFrame, list[str]]:
	stores = stores.copy()
	locations = locations.copy()

	stores["monthly_profit"] = stores["monthly_revenue"] - stores["monthly_costs"]

	if "country" not in locations.columns:
		locations["country"] = "Germany"

	if "square_meters" not in locations.columns and "property_sqft" in locations.columns:
		locations["square_meters"] = locations["property_sqft"] * 0.092903

	excluded = {
		"store_id",
		"location_id",
		"potential_location_id",
		"opening_date",
		"monthly_revenue",
		"monthly_costs",
		"monthly_fixed_costs",
		"monthly_variable_costs",
		"monthly_profit",
		"property_sqft",
	}

	common_cols = set(stores.columns) & set(locations.columns)
	feature_cols = sorted([col for col in common_cols if col not in excluded])

	if "square_meters" in stores.columns and "square_meters" in locations.columns:
		if "square_meters" not in feature_cols:
			feature_cols.append("square_meters")

	X = stores[feature_cols]
	y = stores["monthly_profit"]
	X_locations = locations[feature_cols]

	return stores, X, y, X_locations, feature_cols


def build_preprocessor(
	numeric_features: Iterable[str],
	categorical_features: Iterable[str],
	use_polynomial: bool,
) -> ColumnTransformer:
	numeric_steps: list[tuple[str, object]] = [
		("imputer", SimpleImputer(strategy="median")),
	]

	if use_polynomial:
		numeric_steps.append(("poly", PolynomialFeatures(degree=2, include_bias=False)))

	numeric_steps.append(("scaler", StandardScaler()))

	numeric_transformer = Pipeline(steps=numeric_steps)
	categorical_transformer = Pipeline(
		steps=[
			("imputer", SimpleImputer(strategy="most_frequent")),
			("onehot", OneHotEncoder(handle_unknown="ignore")),
		]
	)

	return ColumnTransformer(
		transformers=[
			("num", numeric_transformer, list(numeric_features)),
			("cat", categorical_transformer, list(categorical_features)),
		]
	)


def evaluate_model(
	name: str,
	preprocessor: ColumnTransformer,
	X_train: pd.DataFrame,
	X_test: pd.DataFrame,
	y_train: pd.Series,
	y_test: pd.Series,
) -> ModelResult:
	pipeline = Pipeline(
		steps=[
			("preprocessor", preprocessor),
			("model", LinearRegression()),
		]
	)
	pipeline.fit(X_train, y_train)
	predictions = pipeline.predict(X_test)
	mse = mean_squared_error(y_test, predictions)
	r2 = r2_score(y_test, predictions)
	return ModelResult(name=name, pipeline=pipeline, mse=mse, r2=r2)


def select_best_model(results: list[ModelResult]) -> ModelResult:
	return max(results, key=lambda item: item.r2)


def save_plots(
	stores: pd.DataFrame, predictions: pd.Series, output_dir: Path
) -> None:
	output_dir.mkdir(parents=True, exist_ok=True)

	plt.figure(figsize=(8, 5))
	sns.histplot(stores["monthly_profit"], kde=True, bins=30)
	plt.title("Distribution der monatlichen Profitabilität")
	plt.xlabel("Monthly Profit")
	plt.ylabel("Count")
	plt.tight_layout()
	plt.savefig(output_dir / "monthly_profit_distribution.png")
	plt.close()

	plt.figure(figsize=(8, 5))
	sns.histplot(predictions, kde=True, bins=30, color="tab:green")
	plt.title("Vorhergesagte Profitabilität (Potenzialstandorte)")
	plt.xlabel("Predicted Monthly Profit")
	plt.ylabel("Count")
	plt.tight_layout()
	plt.savefig(output_dir / "predicted_profit_distribution.png")
	plt.close()


def write_report(
	top_locations: pd.DataFrame, metrics: pd.DataFrame, output_dir: Path
) -> None:
	report_path = output_dir / "recommendation_report.md"
	top_table = top_locations.to_markdown(index=False)
	metrics_table = metrics.to_markdown(index=False)

	report = f"""# Empfehlung: Neue CoffeeTime-Standorte in Deutschland

## Ergebnisüberblick
Basierend auf dem historischen Datensatz wurden lineare und polynomiale Regressionsmodelle
trainiert. Das beste Modell wurde anhand des $R^2$-Wertes auf dem Testdatensatz gewählt.

### Modellgüte
{metrics_table}

### Top 5 Standorte nach vorhergesagter Profitabilität
{top_table}

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
"""

	report_path.write_text(report, encoding="utf-8")


def main() -> None:
	OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

	stores, locations = load_data()
	stores, X, y, X_locations, feature_cols = prepare_datasets(stores, locations)

	numeric_features = X.select_dtypes(include=["number"]).columns
	categorical_features = [
		col for col in X.columns if col not in numeric_features
	]

	X_train, X_test, y_train, y_test = train_test_split(
		X, y, test_size=0.2, random_state=RANDOM_STATE
	)

	results: list[ModelResult] = []
	for name, use_poly in [("Linear", False), ("Polynomial", True)]:
		preprocessor = build_preprocessor(
			numeric_features, categorical_features, use_polynomial=use_poly
		)
		results.append(
			evaluate_model(name, preprocessor, X_train, X_test, y_train, y_test)
		)

	best_model = select_best_model(results)

	metrics_df = pd.DataFrame(
		[
			{
				"model": result.name,
				"mse": round(result.mse, 2),
				"r2": round(result.r2, 4),
			}
			for result in results
		]
	).sort_values("r2", ascending=False)

	best_model.pipeline.fit(X, y)
	location_predictions = best_model.pipeline.predict(X_locations)
	locations_scored = locations.copy()
	locations_scored["predicted_monthly_profit"] = location_predictions

	top_locations = (
		locations_scored.sort_values("predicted_monthly_profit", ascending=False)
		.head(5)
		.loc[
			:,
			[
				"potential_location_id",
				"city",
				"predicted_monthly_profit",
				"population_density",
				"median_household_income",
				"number_of_competitors_1km",
				"traffic_count_nearby",
				"walkability_score",
			],
		]
	)

	metrics_df.to_csv(OUTPUT_DIR / "model_metrics.csv", index=False)
	locations_scored.to_csv(OUTPUT_DIR / "predicted_locations.csv", index=False)
	top_locations.to_csv(OUTPUT_DIR / "top_5_recommendations.csv", index=False)

	save_plots(stores, pd.Series(location_predictions), OUTPUT_DIR)
	write_report(top_locations, metrics_df, OUTPUT_DIR)

	print("Pipeline abgeschlossen.")
	print("Top-5-Empfehlungen gespeichert in outputs/top_5_recommendations.csv")
	print("Report gespeichert in outputs/recommendation_report.md")


if __name__ == "__main__":
	main()