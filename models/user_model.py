import sys

from core.configs import settings
from sqlalchemy import Column, Integer, String

class UserModel(settings.DBBaseModel):
    __tablename__ = "Users"
    id: int = Column(Integer, 
                     primary_key=True, autoincrement=True)
    fullname: str = Column(String(255))
    
    