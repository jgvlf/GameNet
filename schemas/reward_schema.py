from typing import Optional
from pydantic import BaseModel as SchemaBaseModel

class RewardSchema(SchemaBaseModel):
    id: Optional[int]
    bet: int
    result: int
    prize: float