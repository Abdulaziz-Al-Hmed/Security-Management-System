from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_contractors():
    return {"message": "قائمة المقاولين"}

@router.post("/")
async def create_contractor():
    return {"message": "إنشاء مقاول جديد"}