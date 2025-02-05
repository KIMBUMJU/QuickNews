from pydantic import BaseModel, HttpUrl

class ArticleRequest(BaseModel):
    """
    API 요청 모델 정의
    """
    url: HttpUrl