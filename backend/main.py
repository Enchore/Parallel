"""
Parallel 後端應用入口
FastAPI 應用初始化與路由配置
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import chat, mail, story
from backend.config.settings import settings

app = FastAPI(
    title="Parallel — 平行世界多智能體敘事系統",
    description="基於多智能體編排架構的互動敘事應用 API",
    version="1.0.0"
)

# CORS 中間件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 註冊路由
app.include_router(chat.router, prefix="/api/chat", tags=["即時通訊"])
app.include_router(mail.router, prefix="/api/mail", tags=["郵件系統"])
app.include_router(story.router, prefix="/api/story", tags=["劇情系統"])


@app.get("/api/health")
async def health_check():
    """健康檢查接口"""
    return {"status": "ok", "version": "1.0.0"}
