from dotenv import load_dotenv
import os
import jwt

from datetime import datetime, timedelta, timezone

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"


def generate_token(data: int, expiration_minute: int = 60) -> str :
    
    time_expiration = datetime.now(timezone.utc) + timedelta(minutes = expiration_minute)
    data_token = {"sub":str(data) , "exp":time_expiration}
    token_jwt = jwt.encode(data_token,SECRET_KEY,algorithm=ALGORITHM)
    return token_jwt

