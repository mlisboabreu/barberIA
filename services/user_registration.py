from sqlalchemy.orm import Session
from models.user_model import User
from fastapi import HTTPException
from services.encrypt_password import encrypt_password


def email_exist(email: str,session: Session):
    user_email = session.query(User).filter(User.email == email).first()
    if user_email: raise HTTPException(status_code=400,detail="email already registered")
    return email


def superuser_exist(session: Session):
    any_super = session.query(User).filter(User.sup == True).first()
    if any_super:raise HTTPException(status_code=400,detail="super user already exist")
    return True


def user_registration(name_new:str,email_new:str,password_new:str, superuser_new: bool, session:Session):
    new_user = User(
        name_new,
        email = email_exist(email_new,session),
        password = encrypt_password(password_new),
        sup=superuser_exist(session) if superuser_new else False
        )
    session.add(new_user)
    session.commit()
    return {"message":"sucefull register"}

    
    
