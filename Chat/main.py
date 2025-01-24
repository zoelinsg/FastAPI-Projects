from fastapi import FastAPI, WebSocket, Request, WebSocketDisconnect
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from dataclasses import dataclass
from typing import Dict
import uuid
import json

# 設定模板目錄為 "templates"
templates = Jinja2Templates(directory="templates")

@dataclass
class ConnectionManager:
    """管理 WebSocket 連線的類別"""
    def __init__(self) -> None:
        # 使用字典來儲存活躍的連線，key 為連線 id，value 為 WebSocket 物件
        self.active_connections: dict = {}

    async def connect(self, websocket: WebSocket):
        """接受 WebSocket 連線並儲存"""
        await websocket.accept()
        # 產生唯一的連線 ID
        id = str(uuid.uuid4())
        self.active_connections[id] = websocket

    async def broadcast(self, decoded_data: dict, webSocket: WebSocket):
        """廣播訊息給所有已連線的客戶端"""
        for connection in self.active_connections.values():
            is_me = False
            if connection == webSocket:
                is_me = True  # 標記訊息是由當前客戶端發送的

            # 發送訊息給每個已連線的客戶端
            await connection.send_text(json.dumps({
                "isMe": is_me, 
                "data": decoded_data['message'], 
                "username": decoded_data['username']
            }))

    def disconnect(self, websocket: WebSocket):
        """斷開 WebSocket 連線並移除其 ID"""
        id = self.find_connection_id(websocket)  # 根據 WebSocket 找到連線 ID
        del self.active_connections[id]  # 從活躍連線中移除該連線
        return id

    def find_connection_id(self, websocket: WebSocket) -> str:
        """根據 WebSocket 找到連線 ID"""
        for id, connection in self.active_connections.items():
            if connection == websocket:
                return id
        return ""

# 創建 FastAPI 應用實例
app = FastAPI()

# 設定靜態檔案路徑，讓應用可以服務靜態檔案（例如：CSS、JS）
app.mount("/static", StaticFiles(directory="static"), name="static")

# 添加根路徑的路由
@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# 創建 ConnectionManager 實例
manager = ConnectionManager()

# 添加 WebSocket 路由
@app.websocket("/message")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            decoded_data = json.loads(data)
            await manager.broadcast(decoded_data, websocket)
    except WebSocketDisconnect:
        manager.disconnect(websocket)