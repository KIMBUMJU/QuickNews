from newspaper import Article
from fastapi import HTTPException
from langchain_core.documents import Document

def extract_article_content(url:str) -> Document:
    """
    URL에서 기사를 추출합니다.
    """
    try:
        article = Article(url)
        article.download()
        article.parse()
        document = Document(
            page_content=article.text,
            metadata={"source": url},
        )
        return document
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to extract article: {str(e)}")