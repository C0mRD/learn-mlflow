from mlflow import MlflowClient
from pprint import pprint
from sklearn.ensemble import RandomForestRegressor

client = MlflowClient(tracking_uri="http://127.0.0.1:8000")

# Provide an Experiment description that will appear in the UI
experiment_description = (
    "This is mlflow test project."
    "This experiment contains the produce models while learning mlflow."
)

# Provide searchable tags that define characteristics of the Runs that
# will be in this Experiment
experiment_tags = {
    "project_name": "learn-mlflow",
    "store_dept": "produce",
    "team": "stores-ml",
    "project_quarter": "Q3-2023",
    "mlflow.note.content": experiment_description,
}

# Create the Experiment, providing a unique name
produce_apples_experiment = client.create_experiment(
    name="learn-mlflow", tags=experiment_tags
)