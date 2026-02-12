from sqlalchemy.orm import Session
from models.user_model import User
from schemas.user_update_schema import UserUpdate


def user_update(data_for_update:UserUpdate,token:str,session:Session):
    try:
        user = session.query(User).filter(User.id == token).first()
        scan_dict(data_for_update,user)
        
        session.commit()
    
        return {"message":"user data change"}
    except:
        return {"message":"no update"} 
    



def scan_dict(data_for_update:UserUpdate, user:object):
    new_data = data_for_update.model_dump(exclude_unset = True)
    for key, value in new_data.items():
        if str(value).strip() != "":
            setattr(user,key,value)
