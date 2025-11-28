# MLOps-Foundation



## Day4 - DVC 

* ML/DL End-to-end Pipeline
  - Data Ingestion
  - Data Validation
  - Data Transformation
  - Model Training
  - Model Evaluation
  - Prediction Pipeline
  - User Application
  - Deployment

* 執行
  ```bash
  conda create -n mlops python=3.11 -y
  conda activate mlops
  ```

* 建立
  <pre>
  requirements.txt
  </pre>

* 執行 
  ```bash
  pip install -r requirements.txt
  ```

* (18:26) 如果還未啟動 git，要先執行
  ```bash
  git init
  ```

* 建立 
  <pre>
  pipeline/stage_01.py
  pipeline/stage_02.py
  pipeline/stage_03.py
  artifacts/text.txt
  </pre>

* 執行
  ```bash
  python pipeline/stage_01.py
  python pipeline/stage_02.py
  python pipeline/stage_03.py
  ```

* 建立
  <pre>
  main.py
  </pre>

* 執行
  ```bash
  python main.py
  ```

* Nothing has changed

* 建立
  <pre>
  dvc.yaml
  </pre>

* 執行，之後 `.dvc` 資料夾與 `.dvcignore` 檔案 會被建立
  ```bash
  dvc init
  ```

* 執行，之後 `dvc.lock` 會被建立
  ```bash
  dvc repro
  ```

* 此時對 檔案 `artifacts/text.txt` 增減內容後，執行 `dvc repro` 顯示 Stage '...' didn't change

* 刪除檔案 `artifacts/output.txt`，再分別兩次執行，藉此觀察兩次的輸出資訊有何不同
  ```bash
  dvc repro # 執行完後 artifacts/output.txt 會被重新建立
  dvc repro
  ```
  ![result](figures/03/dvcrepro.png)

* 執行
  ```bash
  dvc dag
  ```

## Day5 - Cloud Platforms

* GCP
  ![GCP](figures/05/GCPdashboard.png)

* GCP Buckets ~ AWS S3 Bucket

## Day6 - MLFlow

* Hyperparameter Tuning
  <pre>
  P1 = {learning rate: 0.001, 0.002, 0.003, ...}
  P2 = {optimizer: SGD, Adam, RMSprop}
  </pre>

* `conda activate chest`

* 建立 `requirements.txt`
  ```txt
  mlflow==2.2.2
  dagshub
  ```

* `pip install -r requirements.txt`

* [Red Wine Quality -- Kaggle](https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009)

* 建立 `demp.py`

* 註冊 dagshub 帳號 [DagsHub](dagshub.com)，後去 'connect a repository'，在 'MLflow Tracking remote' 中得到 url
  ![Dagshub_Tracking](figures/06/Dagshubtracking.png)

* 執行 `python demo.py`

* 執行 `python demo.py 0.3 0.6`
  
* 執行 `python demo.py 0.3 0.7`