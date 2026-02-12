from fastapi import APIRouter, Depends, HTTPException
from dependencies.oauth2 import verify_token
from sqlalchemy.orm import Session
from dependencies.session_dependencie import take_session
from services.service_exist import service_exist
from models.service_model import Service
from schemas.service_schema import ServiceSchema
from models.user_model import User
from schemas.new_super_schema import NewSuperSchema
from schemas.service_schema import ServiceSchema

super_user_router = APIRouter(prefix="/super", tags=["super"])

@super_user_router.post("/home")
async def register_super(token : int = Depends(verify_token), session: Session = Depends(take_session)):
    pass
    if super(session.query(User).filter(User.id == token).first().id,session):
        raise HTTPException(status_code=200, detail= "is super")
    
    raise HTTPException(status_code=400, detail= "you are not a super")


@super_user_router.post("/registe/super")
async def register_super(new_super:NewSuperSchema, token: int = Depends(verify_token), session: Session = Depends(take_session)):
    super_user = session.query(User).filter(User.id == token).first()
    if super_user.sup == True:
        user = session.query(User).filter(User.id == new_super.id).first()
        user.sup = True
        session.commit()
        return {"message":f"{user.name} is a new super"}
    raise HTTPException(status_code=400, detail="no super")

@super_user_router.post("/register/service")
async def register_service(service: ServiceSchema,token: int = Depends(verify_token), session: Session = Depends(take_session)):
    user = session.query(User).filter(User.id == token).first()
    if user.sup:
        if service_exist(service.service_name,session):
            raise HTTPException(status_code=400, detail='service already exist')
        service_created = Service(service.service_name,service.price)
        session.add(service_created)
        session.commit()
        return {"msg":"service created"}
    return {"msg":"not super"}

@super_user_router.get("/view/users")
async def view_users(token : int = Depends(verify_token), session:Session = Depends(take_session)):
    user = session.query(User).filter(User.id == token).first()
    if user.sup:
        users = session.query(User).all()
        return {"lala": users}