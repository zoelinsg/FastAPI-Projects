from pydantic import BaseModel

# 定義 FAQ 模型
class FAQ(BaseModel):
    question: str  # 問題
    answer: str    # 答案

# 定義問題模型
class Question(BaseModel):
    question: str  # 問題