from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.database import get_db
from models.employee import Employee
from models.contractor import Contractor
from models.vehicle import Vehicle

router = APIRouter()

@router.get("/stats")
async def get_dashboard_stats(db: Session = Depends(get_db)):
    try:
        # Get actual counts from database
        employees_count = db.query(Employee).filter(Employee.is_active == True).count()
        contractors_count = db.query(Contractor).filter(Contractor.is_active == True).count()
        vehicles_count = db.query(Vehicle).filter(Vehicle.is_active == True).count()
        
        return {
            "employees_count": employees_count,
            "contractors_count": contractors_count,
            "vehicles_count": vehicles_count,
            "violations_count": 0  # This will be implemented when you add violations model
        }
    except Exception as e:
        print(f"Dashboard stats error: {e}")
        # Return default values if there's an error
        return {
            "employees_count": 0,
            "contractors_count": 0,
            "vehicles_count": 0,
            "violations_count": 0
        }