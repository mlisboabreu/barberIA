from fastapi import APIRouter, Depends
from dependencies.oauth2 import verify_token
from sqlalchemy.orm import Session
from dependencies.session_dependencie import take_session
from models.user_model import User
from schemas.user_update_schema import UserUpdate
from schemas.services_schema import ServicesSchema
from models.services_model import Services
from models.service_model import Service
from datetime import datetime
from services.show_profile import show_profile
from services.user_update import user_update

user_router = APIRouter(prefix="/user", tags=["user"])


@user_router.get("/profile")
async def profile (token:str = Depends(verify_token), session: Session = Depends(take_session)):
    return show_profile(token,session)

@user_router.patch("/profile/update")
async def profile_update(user_update_dict: UserUpdate, token:str = Depends(verify_token), session: Session = Depends(take_session)):
    return user_update(user_update_dict,token,session)

@user_router.post("/schedule_service")
async def schedule_service (services:ServicesSchema ,token: int = Depends(verify_token), session: Session = Depends(take_session)):
   servicos_encontrados = session.query(Service).filter(Service.service_name.in_(services.items)).all()
   if not servicos_encontrados:
       return {"message":"service not found"}
   
   preco_total = sum(s.price for s in servicos_encontrados)
   data = datetime.now()
   data_formatada = data.strftime("%d/%m/%Y - %H:%M")
   user_token = session.query(User).filter(User.id == token).first().id

   new_service = Services(user_token,servicos_encontrados,preco_total,data_formatada,"pendente")

   session.add(new_service)
   session.commit()
   return {"message":"scheduled service"}

@user_router.get("/complete_service")
async def complete_service(token: int = Depends(verify_token), session:Session = Depends(take_session)):
    service_encontrado = session.query(Services).filter(Services.user == token).first()
    service_encontrado.status = "concluido"
    session.query(User).filter(User.id == token).first().frequency += 1

    session.commit()

    return {"msg":"serviço finalizado e frequencia atualizada"}


@user_router.get("/cancel_service")
async def cancel_service(token: int = Depends(verify_token), session:Session = Depends(take_session)):
    service_encontrado = session.query(Services).filter(Services.user == token).first()
    service_encontrado.status = "cancelado"

    session.commit()

    return {"msg":"serviço cancelado"}

       



    
@user_router.delete("/profile/delete")
async def profile_update(token:str = Depends(verify_token), session: Session = Depends(take_session)):
    user = session.query(User).filter(User.id == token).first()
    session.delete(user)
    session.commit()
    return {"message":"user deleted"}
