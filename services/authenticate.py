from pydantic import EmailStr
from sqlalchemy.orm import Session
from fastapi import HTTPException 
from models.user_model import User
from services.encrypt_password import verify_password
from services.JWT_token import generate_token




def authenticate_user(email:EmailStr ,password: str, session: Session):
    try:
        user = session.query(User).filter(User.email == email).first()
        verify_password(user.password, password)
        jwt_token = generate_token(user.id)
        return {
        "access_token":jwt_token,
        "token_type": "bearer",
        "message" : "sucefull login"
    }

    except:
        raise HTTPException(status_code=400, detail="incorrect email or password")