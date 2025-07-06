# FastAPI Blog

這是一個使用 FastAPI、HTML、CSS 和 JSON 建立的簡單部落格應用程式。該應用程式允許用戶創建、閱讀、編輯和刪除部落格文章。

## 功能

- **首頁**：顯示所有部落格文章。
- **文章詳情**：顯示單篇文章的詳細內容。
- **創建文章**：允許用戶創建新文章。
- **編輯文章**：允許用戶編輯現有文章。
- **刪除文章**：允許用戶刪除文章。

## 安裝

1. 確保已安裝 [Python 3.12](https://www.python.org/downloads/) 或更高版本。
2. 安裝 [Poetry](https://python-poetry.org/docs/#installation) 來管理依賴項目。
3. 克隆此倉庫並進入專案目錄：

    ```sh
    git clone https://github.com/zoelinsg/FastAPI-Projects.git
    cd Blog
    ```

4. 使用 Poetry 安裝依賴：

    ```sh
    poetry install
    ```

## 使用

1. 啟動 FastAPI 伺服器：

    ```sh
    poetry run uvicorn main:app --reload
    ```

2. 打開瀏覽器並訪問 `http://127.0.0.1:8000` 以使用應用程式。

## 參考教學

[Building a Simple Blog App Using FastAPI, HTML, CSS, and JSON](https://dev.to/jagroop2001/building-a-simple-blog-app-using-fastapi-html-css-and-json-1dc)