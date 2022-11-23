import sys

from core.configs import settings
from models.user_model import UserModel
from sqlalchemy.orm import relationships
from sqlalchemy import Column, Integer, String, ForeignKey

class ResultModel(settings.DBBaseModel):
    __tablename__ = "Results"
    id: int = Column(Integer, primary_key=True, 
    autoincrement=True)
    bet: int = Column(Integer, ForeignKey("Bets.id"))
    firstTeamGoals: int = Column(Integer)
    secondTeamGoals: int = Column(Integer)

