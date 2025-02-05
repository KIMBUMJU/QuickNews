from fastapi import FastAPI, HTTPException
from app.services.extractor import extract_article_content
from app.models.request import ArticleRequest
from app.services.summarizer import summarize_article

# FastAPI 앱 초기화
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to QuickNews API!"}


@app.post("/summarize")
def summarize_endpoint(request: ArticleRequest):

    # 기사 내용 추출
    document = extract_article_content(str(request.url))
    if not document:
        raise HTTPException(status_code=400, detail=f"Failed to extract article content.")

    # 기사 요약
    result = summarize_article(document)
    return result