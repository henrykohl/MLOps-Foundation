# MLOps-Foundation

* 日期標題後'()' 中為Lecture 實作時的目錄路徑，因此要實作時須先切換到實作目標目錄的路徑，

## Day1 -- Introduction

* [Lecture Video](https://www.youtube.com/watch?v=eRyQDkCrZrk)

* (35:18) MLOPs
  1. Data Management -- DVC
  2. Version Control -- Github
  3. Automation (pipeline) -- Salemaker
  4. Experiment Tracking -- MLflow
  5. CI/CD -- Genkins, CircleCI, Github Action
  6. Monitoring -- Grafana
  7. Retraining -- Airflow

## Day2 (01.Linux cmd)

* [Lecture Video](https://www.youtube.com/watch?v=dfnVzbW423E)

* (3:29)
  - Machine Learning -- Scikit learn
  - Deep Learning -- Tensorflow, Pytorch
  - Generative AI -- LangChine, LlamaIndex

* (07:49)
  Dev -> project -> Deploy (AWS,GCP,AZURE,Alibaba)

* (19:10)
  ```bash
  sudo apt update
  sudo apt-get update -y
  ```

## Day3 (02.Git-Github)

* [Lecture Video](https://www.youtube.com/watch?v=ipVlWGPOijI)

* (11:33)
  <pre>
                  git                                               Github
  Is a version control software                | Is a web application that hosts remote git repo 
  Is used as a command line tool & run locally | Owned by Microsoft. It's running on remote
  </pre>

## Day4 (03.DVC-demo)

* [Lecture Video](https://www.youtube.com/watch?v=pI6r5N7q828)

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

## Day5 -- Cloud Platforms

* [Lecture Video](https://www.youtube.com/watch?v=v8RtyRIQoNU)

* GCP
  ![GCP](figures/05/GCPdashboard.png)

* GCP Buckets ~ AWS S3 Bucket

## Day6 (04.MLflow)

* [Lecture Video](https://www.youtube.com/watch?v=Y_BlkXUfkzY)

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

* [MLflow Python API](https://mlflow.org/docs/latest/api_reference/python_api/index.html#python-api)

* [Red Wine Quality -- Kaggle](https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009)

* 建立 `demp.py`

* 註冊 dagshub 帳號 [DagsHub](dagshub.com)，後去 'connect a repository'，在 'MLflow Tracking remote' 中得到 url
  ![Dagshub_Tracking](figures/06/Dagshubtracking.png)

* 執行 `python demo.py`

* 執行 `python demo.py 0.3 0.6`
  
* 執行 `python demo.py 0.3 0.7`

* 在 [dagshub/MLOps-Foundation](dagshub.com/henrykohl/MLOps-Foundation.mlflow/#/experiments) 運行結果列表中(可由上圖中點選 'Go to mlflow UI'進入) ，勾選欲檢視的 experiments 後，執行 'Compare'
  ![experiments](figures/06/mlflowexperiments1.png)

  > 指定欲比較的 Metrics，即會顯示 experiments 相關結果

  ![experiments](figures/06/mlflowexperiments2.png)

## Day7 

* [Lecture Video](https://www.youtube.com/watch?v=4HXhYvqOj2Y)

* (21:03) [Install Docker Desktop on Windows](https://docs.docker.com/desktop/setup/install/windows-install/)

* (26:29) [Docker Hub Explore](https://hub.docker.com/explore)

* 執行 
  ```bash
  docker pull hello-world
  docker images
  docker run hello-world
  ```

* Lecture Demo：在 Docker Desktop on Windows 中檢視結果
  ![Dockerer_desktop](figures/07/Dockerdesktop.png)


* 執行
  ```bash
  docker ps -a # 複製CONTAINER ID
  docker rm <上面的CONTAINER ID>
  docker ps -a
  docker rmi hello-world
  docker images
  ```

## Containerization - Creating, Tagging, and Managing Custom Docker Images 

* [Lecture Video](https://www.youtube.com/watch?v=5LktCrQIcys)

* [Github resource](https://github.com/entbappy/Ultimate-MLOps-Full-Course)

* 建立 `Docker-demo` 目錄

* 建立 `Docker-demo/README.md`
  ```markdown
  # how to run
  conda create -n test python=3.11 -y
  conda activate test
  pip install -r requirements.txt
  ```

* 建立 `Docker-demo/requirements.txt`
  ```txt
  Flask==1.1.2
  Ifaddr=0.1.7
  Itsdangerous==1.1.0
  Jinja2==2.11.2
  MarkupSafe==1.1.1
  Werkzeug==1.0.1
  Zeroconf==0.28.0
  gunicorn==20.1.0
  ```

* 執行
  ```bash
  conda create -n test python=3.11 -y
  conda activate test
  pip install -r requirements.txt
  ```

* 建立 `Docker-demo/calculator.py`

* 執行 `python calculator.py` (輸入 44 與 45)


* 建立資料夾 `Docker-demo/static` 與 `Docker-demo/templates`

* 建立檔案 \
  `Docker-demo/static/main.css` \
  `Docker-demo/static/style.css` \
  `Docker-demo/templates/index.html` \
  `Docker-demo/templates/results.html`
  