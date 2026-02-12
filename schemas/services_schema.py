from pydantic import BaseModel,ConfigDict

class ServicesSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    items : list = [str]

