1. conda create -n mlops python=3.11 -y
2. conda activate mlops
3. pip install -r requirements.txt



### DVC cmd

1. dvc init
2. dvc repro
3. dvc dag

---

## Note

* ML/DL End-to-end Pipeline
  - Data Ingestion
  - Data Validation
  - Data Transformation
  - Model Training
  - Model Evaluation
  - Production Pipeline
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
  ![result](../figures/03/dvcrepro.png)

* 執行
  ```bash
  dvc dag
  ```