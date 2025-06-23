from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class EmployeeBase(BaseModel):
    employee_id: str = Field(..., description="رقم الموظف")
    full_name: str = Field(..., description="الاسم الكامل بالإنجليزية")
    full_name_ar: str = Field(..., description="الاسم الكامل بالعربية")
    department: str = Field(..., description="القسم")
    position: Optional[str] = Field(None, description="المنصب")
    phone: Optional[str] = Field(None, description="رقم الهاتف")
    hire_date: Optional[date] = Field(None, description="تاريخ التوظيف")
    is_active: bool = Field(True, description="نشط")

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(BaseModel):
    employee_id: Optional[str] = None
    full_name: Optional[str] = None
    full_name_ar: Optional[str] = None
    department: Optional[str] = None
    position: Optional[str] = None
    phone: Optional[str] = None
    hire_date: Optional[date] = None
    is_active: Optional[bool] = None

class EmployeeOut(EmployeeBase):
    id: int

    class Config:
        from_attributes = True  # هذا هو الإصلاح للتحذير