import sys
import os
from fastapi.testclient import TestClient

# 將專案根目錄添加到 sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.main import app

client = TestClient(app)

# 測試根路徑
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "歡迎來到 FAQ Chatbot" in response.text  # 檢查回應內容

# 測試 FAQ 問題的 API
def test_get_faq():
    response = client.post("/faq", json={"question": "你好"})
    assert response.status_code == 200
    assert response.json() == {"answer": "你好！有什麼我可以幫助你的嗎？"}

    response = client.post("/faq", json={"question": "天氣"})
    assert response.status_code == 200
    assert response.json() == {"answer": "今天的天氣很好，適合外出散步。"}

    response = client.post("/faq", json={"question": "名字"})
    assert response.status_code == 200
    assert response.json() == {"answer": "我是 FAQ Chatbot，很高興認識你！"}

    response = client.post("/faq", json={"question": "功能"})
    assert response.status_code == 200
    assert response.json() == {"answer": "我可以回答你的問題，提供資訊，幫助你解決問題。"}

    response = client.post("/faq", json={"question": "價格"})
    assert response.status_code == 200
    assert response.json() == {"answer": "這取決於你所詢問的產品或服務。請提供更多資訊。"}

    response = client.post("/faq", json={"question": "時間"})
    assert response.status_code == 200
    assert "現在是" in response.json()["answer"]

    response = client.post("/faq", json={"question": "日期"})
    assert response.status_code == 200
    assert "今天的日期是" in response.json()["answer"]

    response = client.post("/faq", json={"question": "烏薩奇"})
    assert response.status_code == 200
    assert response.json() == {"answer": "呀哈"}

    response = client.post("/faq", json={"question": "吉伊"})
    assert response.status_code == 200
    assert response.json() == {"answer": "羊粑粑"}

    response = client.post("/faq", json={"question": "謝謝"})
    assert response.status_code == 200
    assert response.json() == {"answer": "不客氣！祝你有美好的一天！"}

    response = client.post("/faq", json={"question": "再見"})
    assert response.status_code == 200
    assert response.json() == {"answer": "再見！歡迎隨時回來找我！"}

    response = client.post("/faq", json={"question": "未知問題"})
    assert response.status_code == 200
    assert response.json() == {"answer": "這是一個預設的回答。"}