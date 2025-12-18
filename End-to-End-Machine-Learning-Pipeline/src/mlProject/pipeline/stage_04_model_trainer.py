from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_trainer import ModelTrainer
from mlProject import logger



STAGE_NAME = "Model Trainer stage"

class ModelTrainerTrainingPipeline:
  def __init__(self):
    pass

  def main(self):
    config = ConfigurationManager()                                  ## 例化configuration，建立主目錄
    model_trainer_config = config.get_model_trainer_config()         ## 執行configuration，建立次目錄，例化entity
    model_trainer_config = ModelTrainer(config=model_trainer_config) ## 例化 component
    model_trainer_config.train()                                     ## 執行 component，訓練模型後存成 joblib 檔