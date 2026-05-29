import setuptools # 匯入 Python 打包工具庫。它能處理套件的編譯、發佈與安裝。

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "End-to-End-Machine-Learning-Pipeline"
AUTHOR_USER_NAME = "henrykohl"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "henglikohl425@gmail.com"


setuptools.setup(
    name=SRC_REPO,    # 定義這個套件的名稱為 mlProject。當執行 pip install . 或將它上傳到 PyPI 時，這就是別人搜尋或引用它的名稱。
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"}, # 設定根目錄的對應關係。它告訴 setuptools：這套件的原始碼並不是直接放在專案根目錄下，而是通通放在一個名為 src 的資料夾裡。
    packages=setuptools.find_packages(where="src") # 這行會自動搜尋程式碼。find_packages 會掃描資料夾，找出所有包含 __init__.py 的目錄，將它們標記為子套件。
                                                   # where="src" 是再次強調：「請去 src 資料夾裡面找，別的地方不用看」。
)