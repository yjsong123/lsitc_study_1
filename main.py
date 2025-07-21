from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.question import question_router

app = FastAPI()

origins = [
    "http://localhost:5173",  # 프론트엔드 개발 서버
    "http://127.0.0.1:5173",  # 프론트엔드 개발 서버 (IP 주소)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# hello API
# @app.get("/hello")
# def hello():
#     return {"message": "안녕하세요 파이보"}


app.include_router(question_router.router)
