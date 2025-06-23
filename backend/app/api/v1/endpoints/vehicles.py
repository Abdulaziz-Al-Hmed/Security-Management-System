from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_vehicles():
    return {"message": "قائمة المركبات"}

@router.post("/")
async def create_vehicle():
    return {"message": "إنشاء مركبة جديدة"}