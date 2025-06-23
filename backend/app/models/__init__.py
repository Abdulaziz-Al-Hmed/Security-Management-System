# Import Base from the correct location
from database.database import Base

# Then import all models
from .user import User
from .employee import Employee
from .contractor import Contractor  
from .vehicle import Vehicle

__all__ = ["Base", "User", "Employee", "Contractor", "Vehicle"]