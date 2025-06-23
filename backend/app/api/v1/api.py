from fastapi import APIRouter
from api.v1.endpoints import auth, employees, contractors, vehicles, dashboard
from api.v1.endpoints import temp_create_admin  # أضف هذا السطر

api_router = APIRouter()

# إضافة جميع المسارات
api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
api_router.include_router(employees.router, prefix="/employees", tags=["Employees"])
api_router.include_router(contractors.router, prefix="/contractors", tags=["Contractors"])
api_router.include_router(vehicles.router, prefix="/vehicles", tags=["Vehicles"])
api_router.include_router(dashboard.router, prefix="/dashboard", tags=["Dashboard"])
api_router.include_router(temp_create_admin.router, prefix="/temp", tags=["Temp"])  # أضف هذا السطر