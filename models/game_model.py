from core.configs import settings
from sqlalchemy import Column, Integer, String, ForeignKey

class GameModel(settings.DBBaseModel):
    __tablename__ = "Games"
    id: int = Column(Integer, primary_key=True, 
    autoincrement=True)
    firstTeam: str = Column(String(255))
    secondTeam: str = Column(String(255))