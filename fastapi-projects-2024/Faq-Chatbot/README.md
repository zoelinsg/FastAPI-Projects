# FAQ Chatbot

FAQ Chatbot 是一個基於 FastAPI 的問答機器人，能夠自動回應用戶的問題。

## 功能

- 問答機器人：根據用戶的問題提供自動回應。
- 自動回應系統：內建多種常見問題的回答。

## 安裝

1. 確保已安裝 [Python 3.12](https://www.python.org/downloads/) 或更高版本。
2. 安裝 [Poetry](https://python-poetry.org/docs/#installation) 來管理依賴項目。
3. 克隆此倉庫並進入專案目錄：

    ```sh
    git clone https://github.com/zoelinsg/FastAPI-Projects.git
    cd Faq-Chatbot
    ```

4. 使用 Poetry 安裝依賴：

    ```sh
    poetry install
    ```

## 使用

1. 啟動 FastAPI 伺服器：

    ```sh
    poetry run uvicorn app.main:app --reload
    ```

2. 打開瀏覽器並訪問 `http://127.0.0.1:8000` 以使用應用程式。

## 測試

1. 使用以下命令運行測試：

    ```sh
    poetry run pytest
    ```

## 觀看 Demo

[Demo 影片](https://youtu.be/EWkxuLoMrPs)