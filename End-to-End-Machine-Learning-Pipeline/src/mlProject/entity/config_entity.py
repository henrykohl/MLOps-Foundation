from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path           ## 定義在 config.yaml 之 data_ingestion; 實際輸入類型 str
    source_URL: str          ## 定義在 config.yaml 之 data_ingestion;
    local_data_file: Path    ## 定義在 config.yaml 之 data_ingestion; 實際輸入類型 str (data.zip 路徑)
    unzip_dir: Path          ## 定義在 config.yaml 之 data_ingestion; 實際輸入類型 str



@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path           ## 定義在 config.yaml 之 data_validation; 實際輸入類型 str
    STATUS_FILE: str         ## 定義在 config.yaml 之 data_validation;
    unzip_data_dir: Path     ## 定義在 config.yaml 之 data_validation; 實際輸入類型 str (csv 檔案路徑)
    all_schema: dict         ## 定義在 config.yaml 之 data_validation; 實際輸入類型 ConfigBox


@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path           ## 定義在 config.yaml 之 data_transformation; 實際輸入類型 str
    data_path: Path          ## 定義在 config.yaml 之 data_transformation; 實際輸入類型 str



@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path           ## 定義在 config.yaml 之 model_trainer; 實際類型 str
    train_data_path: Path    ## 定義在 config.yaml 之 model_trainer; 實際類型 str
    test_data_path: Path     ## 定義在 config.yaml 之 model_trainer; 實際類型 str
    model_name: str          ## 定義在 config.yaml 之 model_trainer
    alpha: float             ## 定義在 params.yaml 之 ElasticNet
    l1_ratio: float          ## 定義在 params.yaml 之 ElasticNet
    target_column: str       ## 定義在 schema.yaml 之 TARGET_COLUMN



@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path           ## 定義在 config.yaml 之 model_evaluation; 實際類型 str
    test_data_path: Path     ## 定義在 config.yaml 之 model_evaluation; 實際類型 str
    model_path: Path         ## 定義在 config.yaml 之 model_evaluation; 實際類型 str
    all_params: dict         ## 定義在 params.yaml 之 ElasticNet; 實際類型 ConfigBox 
    metric_file_name: Path   ## 定義在 config.yaml 之 model_evaluation; 實際類型 str
    target_column: str       ## 定義在 schema.yaml 之 TARGET_COLUMN; 