import os
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import numpy as np
import joblib
from mlProject.entity.config_entity import ModelEvaluationConfig
from pathlib import Path
from mlProject.utils.common import save_json


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    
    def eval_metrics(self,actual, pred):                 # actual 類型: Series, pred 類型: Series
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2
    


    def save_results(self):
        
        test_data = pd.read_csv(self.config.test_data_path) ## 從 artifacts/data_transformation/test.csv
        model = joblib.load(self.config.model_path)         ## 從 artifacts/model_trainer/model.joblib

        test_x = test_data.drop([self.config.target_column], axis=1)   ## test_data 捨棄 quality 欄 
        test_y = test_data[[self.config.target_column]]                ## test_data 取得 quality 欄 

        predicted_qualities = model.predict(test_x)                      ## 輸出 Series

        (rmse, mae, r2) = self.eval_metrics(test_y, predicted_qualities) ## 輸入 (Series, Series)

        # Saving metrics as local
        scores = {"rmse": rmse, "mae": mae, "r2": r2}                    ## 輸入 (float, float, float)
        save_json(path=Path(self.config.metric_file_name), data=scores)  ## 到 artifacts/model_evaluation/metrics.json