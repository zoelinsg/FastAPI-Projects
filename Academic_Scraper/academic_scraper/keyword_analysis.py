import pandas as pd
from collections import Counter
from typing import List, Dict

# 定義停用詞列表
STOPWORDS = set([
    "the", "and", "of", "to", "a", "for", "in", "with", "is", "on", "that", "as", "we", "from", "by", "an", "be", "this", "which", "or", "at", "it", "are", "was", "but", "not", "have", "has", "had", "were", "can", "will", "would", "should", "could", "may", "might", "must", "shall", "do", "does", "did", "done", "been", "being", "if", "then", "than", "so", "such", "these", "those", "there", "here", "when", "where", "why", "how", "what", "who", "whom", "whose", "which", "about", "because", "through", "during", "before", "after", "above", "below", "between", "under", "over", "again", "further", "more", "most", "some", "any", "each", "other", "another", "much", "many", "few", "several", "all", "both", "either", "neither", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "first", "second", "third", "next", "last", "own", "same", "different", "new", "old", "good", "bad", "better", "best", "worse", "worst", "great", "small", "large", "big", "little", "long", "short", "high", "low", "early", "late", "young", "old", "right", "left", "up", "down", "out", "in", "off", "on", "over", "under", "again", "further", "then", "once", "here", "there", "where", "when", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now", "our", "its", "their", "used", "use", "using", "available", "present", "introduce", "across", "demonstrate", "time", "numerical", "paper"
])

def analyze_keywords(papers: List[Dict[str, str]]):
    """分析論文中的關鍵詞"""
    all_keywords = [] # 儲存所有關鍵詞
    for paper in papers: # 逐一讀取論文
        keywords = paper.get("title", "").split() # 以空白分割標題
        filtered_keywords = [word.lower() for word in keywords if word.lower() not in STOPWORDS] # 過濾停用詞
        all_keywords.extend(filtered_keywords) # 將過濾後的關鍵詞加入列表
    
    keyword_counts = Counter(all_keywords) # 計算每個關鍵詞出現的次數
    keyword_df = pd.DataFrame(keyword_counts.items(), columns=["keyword", "count"]) # 轉換成 DataFrame
    keyword_df = keyword_df.sort_values(by="count", ascending=False) # 依照出現次數排序
    return keyword_df