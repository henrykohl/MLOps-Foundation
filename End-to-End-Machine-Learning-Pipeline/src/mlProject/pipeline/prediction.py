import joblib 
import numpy as np
import pandas as pd
from pathlib import Path



class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path('artifacts/model_trainer/model.joblib'))

    
    def predict(self, data): # data 類型：numpy.ndarray，shpae 為 (1,11)
        prediction = self.model.predict(data)  ## 輸出類型 numpy.ndarray，shpae 為 (1,)


        return prediction