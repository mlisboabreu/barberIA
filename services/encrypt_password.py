from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from fastapi import HTTPException


ph = PasswordHasher()

def encrypt_password(password:str) -> str:
    return ph.hash(password)


def verify_password(password_encrypt:str, password_normal: str) -> bool:
    try:
        return ph.verify(password_encrypt,password_normal)
    except VerifyMismatchError:
        raise HTTPException(status_code=400, detail="incorret email or password")
    