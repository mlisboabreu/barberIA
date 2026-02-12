from fastapi import APIRouter, Depends
from dependencies.session_dependencie import take_session
from sqlalchemy.orm import Session
from schemas.user_schema import UserSchema
from services.user_registration import user_registration
from schemas.login_schema import LoginSchema
from fastapi.security import OAuth2PasswordRequestForm
from services.authenticate import authenticate_user



auth_router = APIRouter(prefix="/auth",tags=["auth"])

@auth_router.post("/register/user")
async def register_user(user:UserSchema, session: Session = Depends(take_session)):
    return user_registration(user.name, user.email, user.password, user.sup, session)


@auth_router.post("/login")
async def login(user:LoginSchema , session: Session = Depends(take_session)):
    return authenticate_user(user.email,user.password,session)
    


@auth_router.post("/login_form")
async def login_form (login:OAuth2PasswordRequestForm = Depends() , session: Session = Depends(take_session)):
    return authenticate_user(login.username, login.password, session)

    




