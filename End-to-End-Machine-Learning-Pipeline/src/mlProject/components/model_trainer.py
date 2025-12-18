import pandas as pd
import os
from mlProject import logger
from sklearn.linear_model import ElasticNet
import joblib
from mlProject.entity.config_entity import ModelTrainerConfig


class ModelTrainer:
  def __init__(self, config: ModelTrainerConfig):
    self.config = config

  
  def train(self):
    train_data = pd.read_csv(self.config.train_data_path) ## 讀取 artifacts/data_transformation/train.csv
    test_data = pd.read_csv(self.config.test_data_path) ## 讀取 artifacts/data_transformation/test.csv


    train_x = train_data.drop([self.config.target_column], axis=1) ## train_data 捨棄 quality 欄
    test_x = test_data.drop([self.config.target_column], axis=1)   ## test_data 捨棄 quality 欄 (沒用到)
    train_y = train_data[[self.config.target_column]]              ## train_data 取得 quality 欄
    test_y = test_data[[self.config.target_column]]                ## test_data 取得 quality 欄 (沒用到)

    ## self.config.alpha 為 float 類型, self.config.l1_ratio 為 float 類型
    lr = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42)
    lr.fit(train_x, train_y)
    ## 將 lr 存為 artifacts/model_trainer/model.joblib
    joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))