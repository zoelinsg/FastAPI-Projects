from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.models import Question
from app.faq_service import get_answer  # 引入新的服務

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

# 根據請求返回首頁模板
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(request, "index.html", {"request": request})

# 處理 FAQ 問題的 API
@app.post("/faq")
async def get_faq(question: Question):
    answer = get_answer(question)  # 使用新的服務來獲取回答
    return {"answer": answer}