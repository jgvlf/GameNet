from typing import Optional
from pydantic import BaseModel as SchemaBaseModel

class ResultSchema(SchemaBaseModel):
    id: Optional[int]
    bet: int
    firstTeamGoals: int
    secondTeamGoals: int