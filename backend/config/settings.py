"""
Parallel 後端配置
包含應用配置、LLM 配置、數據庫配置等
"""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """應用配置"""

    # 應用配置
    APP_NAME: str = "Parallel"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True

    # 服務端口
    PORT: int = 8000

    # LLM 配置
    OPENAI_API_KEY: str = ""
    OPENAI_BASE_URL: str = "https://api.openai.com/v1"
    CHAT_MODEL: str = "gpt-4o-mini"
    WORLD_MODEL: str = "qwen-plus"
    STORY_MODEL: str = "qwen-plus"

    # 數據庫配置
    SQLITE_DB_PATH: str = "parallel.db"
    REDIS_URL: str = "redis://localhost:6379/0"

    # CORS
    CORS_ORIGINS: list = ["*"]

    class Config:
        env_file = ".env"


settings = Settings()
