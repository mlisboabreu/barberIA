import pytest
from fastapi.testclient import TestClient
from main import app
from models.database import Base, db
from sqlalchemy.orm import sessionmaker
from models.user_model import User
from services.encrypt_password import encrypt_password




client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_db():
    Base.metadata.create_all(bind = db)
    yield 
    Base.metadata.drop_all(bind = db)

@pytest.fixture
def create_user_for_tests():
    Session = sessionmaker(bind=db)
    session = Session()

    password_encrypt = encrypt_password("123")

    user = User(
        name = "marcio",
        email = "marciorlisboa7@gmail.com",
        password = password_encrypt,
        sup = False
    )

    session.add(user)
    session.commit()
    session.refresh(user)
    yield user
    session.close()


def test_login_user(create_user_for_tests):
    login_data = {
        "email": "marciorlisboa7@gmail.com",
        "password": "123"
    }

    response = client.post("/auth/login", json= login_data)

    assert response.status_code == 200
    assert response.json()["message"] == "sucefull login"


def test_login_email_erro(create_user_for_tests):
    login_data = {
        "email": "marciorlisboa78@gmail.com",
        "password": "123"
    }

    response = client.post("/auth/login", json= login_data)

    assert response.status_code == 400
    assert response.json()["detail"] == "incorrect email or password"

def test_login_password_erro(create_user_for_tests):
    login_data = {
        "email": "marciorlisboa7@gmail.com",
        "password": "1234"
    }

    response = client.post("/auth/login", json= login_data)

    assert response.status_code == 400
    assert response.json()["detail"] == "incorrect email or password"


def test_login_form(create_user_for_tests):
    login_data = {
        "username": "marciorlisboa7@gmail.com",
        "password": "123"
    }

    response = client.post("/auth/login_form", data=login_data)

    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"




