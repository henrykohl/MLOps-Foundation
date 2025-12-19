from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_evaluation import ModelEvaluation
from mlProject import logger

STAGE_NAME = "Model evaluation stage"

class ModelEvaluationTrainingPipeline:
  def __init__(self):
    pass

  def main(self):
    config = ConfigurationManager()                                  ## 例化configuration，建立主目錄
    model_evaluation_config = config.get_model_evaluation_config()   ## 執行configuration，建立次目錄，例化entity
    model_evaluation_config = ModelEvaluation(config=model_evaluation_config) ## 例化 component
    model_evaluation_config.save_results()                                    ## 執行 component，測試結果存成 json 檔