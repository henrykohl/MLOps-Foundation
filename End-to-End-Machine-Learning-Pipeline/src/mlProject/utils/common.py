import os
from box.exceptions import BoxValueError # 這通常在處理空的或格式錯誤的內容時會觸發。
import yaml
from mlProject import logger
import json                              # 這讓你能夠處理 JSON 格式的資料轉換（編碼與解碼）。
import joblib
from ensure import ensure_annotations
from box import ConfigBox                # 能把 Python 的字典包裝起來，使可以像存取物件屬性一樣讀取設定。
from pathlib import Path
from typing import Any



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:    # 唯讀模式打開路徑 path_to_yaml 的檔案，並將其指派給 yaml_file。
            content = yaml.safe_load(yaml_file)  # 使用 PyYAML 庫的 safe_load 函數，將 YAML 檔案內容解析成 Python 的原始資料結構（通常是字典或列表）。
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)            # 將解析後的資料（content）傳入 ConfigBox 進行封裝並回傳。
    except BoxValueError:                        # 如果傳給 ConfigBox 的內容有問題（例如檔案內容是空的），則會捕捉到這個特定錯誤。 
        raise ValueError("yaml file is empty")   # 若捕捉到上述錯誤，就丟出一個自定義的 ValueError，並顯示「yaml file is empty」訊息。
    except Exception as e:                       # 捕捉所有其他類型的錯誤（例如檔案路徑不存在、權限不足等）。
        raise e                                  # 將捕捉到的原始錯誤直接再次拋出，不做額外處理。
    


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories (path 可以是 str 類或是 PosixPath 類)
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f: # 使用上下文管理器打開位於 path 路徑的檔案，將打開的檔案物件命名為 f。
        json.dump(data, f, indent=4) # 將 data 物件序列化為 JSON 格式，並寫入檔案物件 f 中。設定縮排為 4 個空格。

    logger.info(f"json file saved at: {path}")




@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    
    
    # 換後的資料，供後續程式使用。
    with open(path) as f:       # 開啟位於 path 路徑的檔案--預設為唯讀模式 ("r")--將讀取到的物件命名為 f
        content = json.load(f)  # 從中讀取 JSON 字串，並將其反序列化回資料結構（如 dict），後指派給變數 content。

    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path) # 此方法，專門用於將指定要儲存的物件 data 儲存到 path 所指定儲存的檔案路徑與名稱
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path) # 開啟位於 path 的檔案，並將其二進位內容反序列化成原本的物件（例如機器學習模型），並指派給變數 data。
    logger.info(f"binary file loaded from: {path}")
    return data



@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"