from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database.database import Base

class Vehicle(Base):
    __tablename__ = "vehicles"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    plate_number = Column(String(20), unique=True, index=True, nullable=False)
    owner_type = Column(String(20), nullable=False)  # employee, contractor
    owner_id = Column(Integer, nullable=False)  # employee_id or contractor_id
    vehicle_type = Column(String(50))  # car, truck, motorcycle, bus
    brand = Column(String(50))
    model = Column(String(50))
    year = Column(Integer)
    color = Column(String(30))
    color_ar = Column(String(30))
    registration_document_path = Column(String(255))
    insurance_document_path = Column(String(255))
    insurance_expiry_date = Column(DateTime)
    registration_expiry_date = Column(DateTime)
    is_active = Column(Boolean, default=True)
    is_authorized = Column(Boolean, default=False)
    notes = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    created_by = Column(Integer)

