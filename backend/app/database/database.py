from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from core.config import settings
import os

# إنشاء مجلد قاعدة البيانات إذا لم يكن موجوداً
db_dir = os.path.dirname(settings.DATABASE_URL.replace("sqlite:///", ""))
os.makedirs(db_dir, exist_ok=True)

# إنشاء المحرك
engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False},
    echo=settings.DEBUG
)

# إنشاء جلسة قاعدة البيانات
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# إنشاء القاعدة الأساسية للنموذج
Base = declarative_base()

# دالة للحصول على جلسة قاعدة البيانات
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# دالة لإنشاء الجداول
def create_tables():
    Base.metadata.create_all(bind=engine)
    print("✅ تم إنشاء جداول قاعدة البيانات")