import requests
from bs4 import BeautifulSoup

def fetch_arxiv(query: str):
    """爬取 arXiv 論文數據"""
    url = f"https://arxiv.org/search/?query={query}&searchtype=all"
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    papers = []
    for result in soup.select(".arxiv-result"):
        title = result.select_one(".title").get_text(strip=True) if result.select_one(".title") else "N/A"
        authors = result.select_one(".authors").get_text(strip=True) if result.select_one(".authors") else "N/A"
        abstract = result.select_one(".abstract").get_text(strip=True) if result.select_one(".abstract") else "N/A"
        link = result.select_one(".title a")["href"] if result.select_one(".title a") else "N/A"
        year = result.select_one(".published").get_text(strip=True).split()[-1] if result.select_one(".published") else "N/A"
        papers.append({
            "title": title,
            "authors": authors,
            "abstract": abstract,
            "link": f"https://arxiv.org{link}" if link.startswith("/") else link,
            "year": year
        })
    return papers

def fetch_ndltd(query: str):
    """爬取台灣博碩士論文知識加值系統 (https://ndltd.ncl.edu.tw)"""
    url = f"https://ndltd.ncl.edu.tw/cgi-bin/gs32/gsweb.cgi/tdetail?query={query}&language=zh-TW"
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    papers = []
    for row in soup.select(".basic-list-table tr"):
        title = row.select_one(".title").get_text(strip=True) if row.select_one(".title") else "N/A"
        author = row.select_one(".author").get_text(strip=True) if row.select_one(".author") else "N/A"
        year = row.select_one(".year").get_text(strip=True) if row.select_one(".year") else "N/A"
        papers.append({"title": title, "author": author, "year": year})
    return papers

def fetch_airiti(query: str):
    """爬取華藝線上圖書館論文 (https://www.airitilibrary.com)"""
    url = f"https://www.airitilibrary.com/Search/alThesisbrowse?searchField=Keyword&q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    papers = []
    for result in soup.select(".thesis-row"):
        title = result.select_one(".thesis-title").get_text(strip=True)
        author = result.select_one(".thesis-author").get_text(strip=True)
        abstract = result.select_one(".thesis-abstract").get_text(strip=True) if result.select_one(".thesis-abstract") else "N/A"
        year = result.select_one(".thesis-year").get_text(strip=True) if result.select_one(".thesis-year") else "N/A"
        papers.append({"title": title, "author": author, "abstract": abstract, "year": year})
    return papers

def fetch_ndltd_org(query: str):
    """爬取 Global ETD Search (https://ndltd.org)"""
    url = f"https://ndltd.org/results?q={query}"
    response = requests.get(url)
    if response.status_code == 404:
        return []
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    papers = []
    for item in soup.select(".record"):
        title = item.select_one(".record-title").get_text(strip=True)
        author = item.select_one(".record-author").get_text(strip=True) if item.select_one(".record-author") else "N/A"
        link = item.select_one("a")["href"] if item.select_one("a") else "N/A"
        year = item.select_one(".record-year").get_text(strip=True) if item.select_one(".record-year") else "N/A"
        papers.append({"title": title, "author": author, "link": link, "year": year})
    return papers

def fetch_all(query: str):
    """整合所有爬取函式"""
    return {
        "ndltd": fetch_ndltd(query),
        "airiti": fetch_airiti(query),
        "ndltd_org": fetch_ndltd_org(query),
        "arxiv": fetch_arxiv(query),
    }