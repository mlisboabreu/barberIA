from dependencies.session_dependencie import take_session
from sqlalchemy.orm import Session
from models.service_model import Service


def service_exist(name:str, session: Session) -> bool:
    service = session.query(Service).filter(Service.service_name == name).first()
    if service:
        return True
    
    return False

