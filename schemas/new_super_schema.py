from pydantic import BaseModel, ConfigDict

class NewSuperSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
