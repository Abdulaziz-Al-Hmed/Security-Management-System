from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
import os
import sys

# إضافة مجلد الجذر للمسار
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.config import settings
from database.database import create_tables
from api.v1.api import api_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # إنشاء الجداول عند بدء التطبيق
    create_tables()
    print("🚀 تم تشغيل النظام بنجاح")
    yield
    print("⚡ تم إغلاق النظام")

# إنشاء تطبيق FastAPI
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="نظام إدارة شامل للأمان والهوية في بيئة العمل",
    lifespan=lifespan
)

# إعداد CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# إضافة الـ API routes
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {
        "message": "مرحباً بك في نظام إدارة الأمان والهوية",
        "message_en": "Welcome to Security Management System",
        "version": settings.APP_VERSION,
        "status": "running"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "النظام يعمل بشكل طبيعي"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        log_level="info"
    )