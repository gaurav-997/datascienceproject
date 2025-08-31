# here we will load the model ( model.joblib) & do the prediction
import joblib
import numpy as np
import pandas as pd
from pathlib import Path

STAGE_NAME="Model Prediction Stage"

class ModelPredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path("artifacts/data_training/model.joblib"))
    
    def predict(self,data):
        prediction = self.model.predict(data)
        return prediction