import sys

from core.configs import settings
from sqlalchemy import Column, Integer, String, ForeignKey

class BetModel(settings.DBBaseModel):
    __tablename__ = "Bets"
    id: int = Column(Integer, primary_key=True, 
    autoincrement=True)
    firstTeam: str = Column(String(255))
    secondTeam: str = Column(String(255))
    firstTeamQuantyGoals: int = Column(Integer)
    secondTeamQuantyGoals: int = Column(Integer)
    user: int = Column(Integer, ForeignKey("Users.id"))

