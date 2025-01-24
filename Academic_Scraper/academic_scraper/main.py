from fastapi import FastAPI, Query, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from .scraper import fetch_all
from .keyword_analysis import analyze_keywords

app = FastAPI()

# 設置模板目錄
templates = Jinja2Templates(directory="academic_scraper/templates")

# 設置靜態文件目錄
app.mount("/static", StaticFiles(directory="academic_scraper/static"), name="static")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    """渲染首頁"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/fetch-papers")
def fetch_papers(query: str = Query(..., min_length=1)):
    """根據關鍵詞從多網站爬取論文"""
    papers = fetch_all(query) # 爬取論文
    return papers

@app.get("/analyze", response_class=HTMLResponse)
def analyze(request: Request, query: str = Query(..., min_length=1)):
    """爬取並分析關鍵詞，並渲染結果頁面"""
    papers = fetch_all(query)
    combined_papers = [paper for source in papers.values() for paper in source] # 合併所有論文
    analysis = analyze_keywords(combined_papers) # 分析關鍵詞
    return templates.TemplateResponse("analysis.html", {"request": request, "analysis": analysis.to_dict(orient="records")})