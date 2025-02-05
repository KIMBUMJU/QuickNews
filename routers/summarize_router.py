from fastapi import APIRouter, HTTPException
from models.request import ArticleRequest
from services.summarizer import summarize_article
from services.extractor import extract_article_content

router = APIRouter()

@router.post("/summarize")
def summarize_endpoint(request: ArticleRequest):

    # 기사 내용 추출
    document = extract_article_content(str(request.url))
    if not document:
        raise HTTPException(status_code=400, detail=f"Failed to extract article content.")

    # 기사 요약
    result = summarize_article(document)
    return result