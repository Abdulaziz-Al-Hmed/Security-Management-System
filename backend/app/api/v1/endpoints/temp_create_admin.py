from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.database import get_db
from models.user import User

router = APIRouter()

@router.post("/create-temp-admin")
def create_temp_admin(db: Session = Depends(get_db)):
    # تحقق من وجود المستخدم مسبقاً
    existing_user = db.query(User).filter(User.username == "1").first()
    if existing_user:
        return {"message": "المستخدم موجود بالفعل", "username": "1", "password": "1"}
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
    return {"message": "تم إنشاء المستخدم بنجاح", "username": "1", "password": "1"}