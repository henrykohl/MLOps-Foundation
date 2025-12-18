from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_transformation import DataTransformation
from mlProject import logger
from pathlib import Path




STAGE_NAME = "Data Transformation stage"

class DataTransformationTrainingPipeline:
  def __init__(self):
    pass


  def main(self):
    try:
      with open(Path("artifacts/data_validation/status.txt"), "r") as f:
        status = f.read().split(" ")[-1]

      if status == "True":
        config = ConfigurationManager()                                            ## 例化configuration，建立主目錄
        data_transformation_config = config.get_data_transformation_config()       ## 執行configuration，建立次目錄，例化entity
        data_transformation = DataTransformation(config=data_transformation_config)## 例化 component
        data_transformation.train_test_spliting()                                  ## 執行 component，進行資料分割

      else:
        raise Exception("You data schema is not valid")

    except Exception as e:
      print(e)