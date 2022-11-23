import sys

from core.configs import settings
from models.game_model import GameModel
from models.user_model import UserModel
from sqlalchemy.orm import relationships
from sqlalchemy import Column, Integer, String, ForeignKey

class BetModel(settings.DBBaseModel):
    __tablename__ = "Bets"
    id: int = Column(Integer, primary_key=True, 
    autoincrement=True)
    game: int = Column(Integer, ForeignKey("Games.id"))
    firstTeamQuantyGoals: int = Column(Integer)
    secondTeamQuantyGoals: int = Column(Integer)
    user: int = Column(Integer, ForeignKey("Users.id"))

