from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database.database import get_db
from models.employee import Employee
from schemas.employee import EmployeeCreate, EmployeeOut

router = APIRouter()

@router.get("/", response_model=List[EmployeeOut])
def get_employees(db: Session = Depends(get_db)):
    employees = db.query(Employee).all()
    return employees

@router.post("/", response_model=EmployeeOut, status_code=status.HTTP_201_CREATED)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    # تحقق من عدم تكرار رقم الهوية
    if db.query(Employee).filter(Employee.employee_id == employee.employee_id).first():
        raise HTTPException(status_code=400, detail="رقم الهوية مستخدم بالفعل")
    emp = Employee(**employee.dict())
    db.add(emp)
    db.commit()
    db.refresh(emp)
    return emp

@router.get("/{employee_id}", response_model=EmployeeOut)
def get_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="الموظف غير موجود")
    return employee

@router.put("/{employee_id}", response_model=EmployeeOut)
def update_employee(employee_id: int, employee: EmployeeCreate, db: Session = Depends(get_db)):
    db_employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not db_employee:
        raise HTTPException(status_code=404, detail="الموظف غير موجود")
    
    # تحقق من عدم تكرار رقم الهوية (إذا تم تغييره)
    if employee.employee_id != db_employee.employee_id:
        if db.query(Employee).filter(Employee.employee_id == employee.employee_id).first():
            raise HTTPException(status_code=400, detail="رقم الهوية مستخدم بالفعل")
    
    # تحديث البيانات
    for key, value in employee.dict().items():
        setattr(db_employee, key, value)
    
    db.commit()
    db.refresh(db_employee)
    return db_employee

@router.delete("/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="الموظف غير موجود")
    
    db.delete(employee)
    db.commit()
    return {"message": "تم حذف الموظف بنجاح"}