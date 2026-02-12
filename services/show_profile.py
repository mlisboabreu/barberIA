from sqlalchemy.orm import Session
from models.user_model import User

def show_profile(token:str,session:Session):
    user = session.query(User).filter(User.id == token).first()

    return {"name":user.name}