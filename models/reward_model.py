import sys

from core.configs import settings
from models.game_model import GameModel
from models.user_model import UserModel
from sqlalchemy.orm import relationships
from sqlalchemy import Column, Integer, Float, ForeignKey

class RewardModel(settings.DBBaseModel):
    __tablename__ = "Rewards"
    id: int = Column(Integer, primary_key=True, 
    autoincrement=True)
    bet: int = Column(Integer, ForeignKey("Bets.id"))
    result: int = Column(Integer, ForeignKey("Results.id"))
    prize: float = Column(Float)

