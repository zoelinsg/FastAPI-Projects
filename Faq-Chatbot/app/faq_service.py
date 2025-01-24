from app.models import Question
from datetime import datetime

def get_answer(question: Question) -> str:
    # 定義問答字典
    faq_dict = {
        "你好": "你好！有什麼我可以幫助你的嗎？",
        "天氣": "今天的天氣很好，適合外出散步。",
        "名字": "我是 FAQ Chatbot，很高興認識你！",
        "功能": "我可以回答你的問題，提供資訊，幫助你解決問題。",
        "價格": "這取決於你所詢問的產品或服務。請提供更多資訊。",
        "時間": f"現在是 {datetime.now().strftime('%H:%M:%S')}",
        "日期": f"今天的日期是 {datetime.now().strftime('%Y-%m-%d')}",
        "烏薩奇": f"呀哈",
        "吉伊": f"羊粑粑",
        "謝謝": "不客氣！祝你有美好的一天！",
        "再見": "再見！歡迎隨時回來找我！"
    }

    # 根據問題返回對應的回答
    for key in faq_dict:
        if key in question.question:
            return faq_dict[key]

    return "這是一個預設的回答。"  # 這裡可以加入實際的回答邏輯