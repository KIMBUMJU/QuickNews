from fastapi import FastAPI
from routers import summarize_router

# FastAPI 앱 초기화
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to QuickNews API!"}

# 라우터 등록
app.include_router(summarize_router.router)