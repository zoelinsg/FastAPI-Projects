# Fastapi Academic Scraper

這是一個使用 FastAPI 構建的學術論文爬蟲與關鍵詞分析工具。該工具可以從多個學術網站爬取論文數據，並對論文標題進行關鍵詞分析。

## 功能

- **首頁**：輸入關鍵詞以開始爬取論文數據並進行關鍵詞分析。
- **關鍵詞分析**：顯示爬取到的論文標題中的關鍵詞及其出現次數。

## 安裝

1. 確保已安裝 [Python 3.10](https://www.python.org/downloads/) 或更高版本。
2. 安裝 [Poetry](https://python-poetry.org/docs/#installation) 來管理依賴項目。
3. 克隆此倉庫並進入專案目錄：

    ```sh
    git clone https://github.com/zoelinsg/FastAPI-Projects.git
    cd Academic-Scraper
    ```

4. 使用 Poetry 安裝依賴：

    ```sh
    poetry install
    ```

## 使用

1. 啟動 FastAPI 伺服器：

    ```sh
    poetry run uvicorn academic_scraper.main:app --reload
    ```

2. 打開瀏覽器並訪問 `http://127.0.0.1:8000` 以使用應用程式。

## 觀看 Demo

[Demo 影片](https://youtu.be/qSAw5xXe9Gc)