import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

from sqlalchemy.orm import Session
from app.database.database import SessionLocal, create_tables
from app.models.user import User

def create_admin_user():
    create_tables()
    db = SessionLocal()
    
    try:
        # التحقق من وجود المستخدم
        existing_user = db.query(User).filter(User.username == "1").first()
        if existing_user:
            print("المستخدم موجود بالفعل")
            print("اسم المستخدم: 1")
            print("كلمة المرور: 1")
            return
        
        # إنشاء مستخدم admin
        admin_user = User(
            username="1",
            email="admin@company.com",
            full_name="System Administrator",
            full_name_ar="مدير النظام",
            hashed_password=User.get_password_hash("1"),
            role="admin",
            department="Security",
            employee_id="SEC001"
        )
        
        db.add(admin_user)
        db.commit()
        print("✅ تم إنشاء المستخدم admin بنجاح")
        print("اسم المستخدم: 1")
        print("كلمة المرور: 1")
        
    except Exception as e:
        print(f"❌ خطأ في إنشاء المستخدم: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    create_admin_user()