import pytest
from models.user_model import User 
from sqlalchemy.orm import sessionmaker
from main import app
from models.database import db
from services.encrypt_password import encrypt_password

@pytest.fixture
def create_user_for_tests():
    password_encrypted = encrypt_password("123")
    Session = sessionmaker(bind=db)
    session = Session()
    user = User(
        name="marcio",
        email="marciorlisboa7@gmail.com",
        password=password_encrypted,
        sup=True
    )
    session.add(user)
    session.commit()
    yield user
    session.refresh(user)
    session.close()