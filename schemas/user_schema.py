from typing import Optional
from pydantic import BaseModel as SchemaBaseModel

class UserSchema(SchemaBaseModel):
    id: Optional[int]
    fullname: str
    
    class Config:
        orm_mode = True