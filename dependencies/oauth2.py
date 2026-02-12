from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException
import jwt
from services.JWT_token import SECRET_KEY, ALGORITHM



oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "/auth/login_form")



def verify_token (token : dict = Depends(oauth2_scheme)):
    try:
        dic_info = jwt.decode(token,SECRET_KEY, algorithms=[ALGORITHM])
    except Exception :
        
        raise HTTPException(status_code=401, detail = 'token invalido')
    
    user_id = dic_info.get('sub')
    return user_id
 
    