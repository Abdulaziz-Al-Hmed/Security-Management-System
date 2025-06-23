from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, Date
from sqlalchemy.sql import func
from database.database import Base

class Employee(Base):
    __tablename__ = "employees"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(String(20), unique=True, index=True, nullable=False)
    full_name = Column(String(100), nullable=False)
    full_name_ar = Column(String(100), nullable=False)
    department = Column(String(100), nullable=False)
    position = Column(String(100))
    email = Column(String(100))
    phone = Column(String(20))
    national_id = Column(String(20), unique=True)
    hire_date = Column(Date)
    birth_date = Column(Date)
    nationality = Column(String(50))
    address = Column(Text)
    emergency_contact = Column(String(100))
    emergency_phone = Column(String(20))
    is_active = Column(Boolean, default=True)
    badge_number = Column(String(20), unique=True)
    access_level = Column(String(20), default="basic")  # basic, medium, high, restricted
    photo_path = Column(String(255))
    notes = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    created_by = Column(Integer)

