from mlProject.config.configuration import ConfigurationManager  ## '5. configuration'
from mlProject.components.data_validation import DataValiadtion  ## '6. components'
from mlProject import logger                                     ## (或許不需要)


STAGE_NAME = "Data Validation stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):                                             ## 省略 try...exception block
        config = ConfigurationManager()                                 ## 例化configuration，建立主目錄
        data_validation_config = config.get_data_validation_config()    ## 執行configuration，建立次目錄，例化entity
        data_validation = DataValiadtion(config=data_validation_config) ## 例化 component
        data_validation.validate_all_columns()                          ## 執行 component