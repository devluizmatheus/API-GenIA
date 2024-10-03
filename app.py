from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router.router import router

app = FastAPI(
    debug= True,
    title="Desafio Lizard",
    summary="API de integração com o Gemini"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(router)