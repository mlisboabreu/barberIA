from sqlalchemy.orm import Session
from schemas.user_schema import UserSchema
from models.user_model import User

def is_super (id:int , session: Session) -> bool:
    if session.query(User).filter(User.id == id).first().sup :
        return True
    return False