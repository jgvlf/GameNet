from typing import Optional
from pydantic import BaseModel as SchemaBaseModel

class BetSchema(SchemaBaseModel):
    id: Optional[int]
    firstTeam: str
    secondTeam: str
    firstTeamQuantyGoals: int
    secondTeamQuantyGoals: int
    user: int
    
    class Config:
        orm_mode = True