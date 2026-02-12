from pydantic import BaseModel,EmailStr,ConfigDict


class UserSchema(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    name: str
    email: EmailStr
    password: str
    sup : bool = False


