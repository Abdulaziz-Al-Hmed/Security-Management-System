from pydantic_settings import BaseSettings
from typing import List
import os

class Settings(BaseSettings):
    # Application settings
    APP_NAME: str = "Security Management System"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True
    
    # Database
    DATABASE_URL: str = "sqlite:///./database/sqlite/security_system.db"
    
    # Security
    SECRET_KEY: str = "your-super-secret-key-change-this-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # CORS
    BACKEND_CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://127.0.0.1:3000"]
    
    # Company Info
    COMPANY_NAME: str = "شركة تحلية المياه"
    COMPANY_NAME_EN: str = "Water Desalination Company"
    
    class Config:
        env_file = ".env"
        case_sensitive = True

# إنشاء instance من الإعدادات
settings = Settings()

# إنشاء مجلدات قاعدة البيانات إذا لم تكن موجودة
os.makedirs("database/sqlite", exist_ok=True)
os.makedirs("database/backup", exist_ok=True)