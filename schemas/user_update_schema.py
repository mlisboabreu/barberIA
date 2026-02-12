from pydantic import BaseModel,EmailStr,ConfigDict
from typing import Optional






class UserUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name : Optional[str] = None
    email: Optional[EmailStr] = None
