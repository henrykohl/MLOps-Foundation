import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("mlProjectLogger") # 用來獲取或建立一個 Logger 物件，並指定這個記錄器的名字"mlProjectLogger"。
# 定義模組層級的： 
# Logger在各個子模組中，使用者可以透過 logging.getLogger(__name__) 取得日誌記錄器。
#  __name__ 會根據套件結構自動產生（例如 package.module），從而建立清晰的日誌層級，方便日後過濾和調試。