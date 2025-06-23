from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text
from sqlalchemy.sql import func
from database.database import Base
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(Base):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True)
    full_name = Column(String(100), nullable=False)
    full_name_ar = Column(String(100), nullable=False)
    hashed_password = Column(String(255), nullable=False)
    role = Column(String(20), default="security_officer")  # admin, security_officer, viewer
    is_active = Column(Boolean, default=True)
    department = Column(String(100))
    employee_id = Column(String(20), unique=True)
    phone = Column(String(20))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    last_login = Column(DateTime(timezone=True))
    
    def verify_password(self, password: str) -> bool:
        return pwd_context.verify(password, self.hashed_password)
    
    @staticmethod
    def get_password_hash(password: str) -> str:
        return pwd_context.hash(password)