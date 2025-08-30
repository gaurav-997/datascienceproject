import os 
from src.datascience.utils import logger
import pandas as pd
import numpy as np 
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import joblib
from pathlib import Path
from src.datascience.entity.config_entity import ModelEvaluationConfig
from src.datascience.utils.common import save_json
from src.datascience.constants import *

os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/chauhan7gaurav/datascienceproject.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"]="chauhan7gaurav"
os.environ["MLFLOW_TRACKING_PASSWORD"]="74060f9fdeeba990c5da5628e310aea51648d1e2"



class ModelEvaluation:
    def __init__(self,config:ModelEvaluationConfig):
        self.config = config
        
    def eval_metrics(self,actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2
    
    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]

        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():

            predicted_qualities = model.predict(test_x)

            (rmse, mae, r2) = self.eval_metrics(test_y, predicted_qualities)

            # Save metrics locally
            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            save_json(path=Path(self.config.metrics_file_name), data=scores)

            # Log metrics & params
            mlflow.log_params(self.config.all_parms)
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2", r2)

            # ✅ Instead of log_model (unsupported by DagsHub)
            model_dir = Path("artifacts/model_evaluation/sklearn_model")
            mlflow.sklearn.save_model(model, model_dir)

            # Log as artifact so it shows up in DagsHub
            mlflow.log_artifact(str(model_dir), artifact_path="model")
