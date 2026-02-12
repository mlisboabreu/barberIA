from pydantic import BaseModel,ConfigDict


class ServiceSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    service_name: str
    price: float
