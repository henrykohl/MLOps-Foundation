from mlProject.config.configuration import ConfigurationManager ## '5. configuration'
from mlProject.components.data_ingestion import DataIngestion   ## '6. components'
from mlProject import logger                                    ## (或許不需要)



STAGE_NAME = "Data Ingestion stage"                             ## python 新增

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):                                             ## 省略 try...exception block
        config = ConfigurationManager()                              ## 例化configuration，建立主目錄
        data_ingestion_config = config.get_data_ingestion_config()   ## 執行configuration，建立次目錄，例化entity
        data_ingestion = DataIngestion(config=data_ingestion_config) ## 例化 component
        data_ingestion.download_file()                               ## 執行 component，下載 zip 檔案
        data_ingestion.extract_zip_file()                            ## 解壓 zip 檔案