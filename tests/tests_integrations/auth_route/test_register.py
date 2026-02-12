import pytest
from fastapi.testclient import TestClient
from main import app
from models.database import Base, db
from sqlalchemy.orm import sessionmaker
from models.user_model import User

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_db():
    Base.metadata.create_all(bind = db)
    yield 
    Base.metadata.drop_all(bind = db)


@pytest.fixture
def user_for_tests():
    Session = sessionmaker(bind=db)
    session = Session()

    user = User (
        name = "maiara",
        email= "maiara@example.com",
        password= "1234",
        sup = True
        )
    session.add(user)
    session.commit()
    session.refresh(user)
    yield user
    session.close()



def test_register_use():
    register_data = {
        "name":"marcio",
        "email":"marciorlisboa7@gmail.com",
        "password":"123",
        "sup":"false"
    }

    response = client.post("/auth/register/user", json=register_data)

    assert response.status_code == 200
    assert response.json()["message"] == "sucefull register"


def test_email_already_exist(user_for_tests):
    register_data = {
        "name":"teste",
        "email":"maiara@example.com",
        "password":"123",
        "sup":"true"
    }

    response = client.post("/auth/register/user",json=register_data)

    assert response.status_code == 400
    assert response.json()["detail"] == "email already registered"


def test_superuser_already_exist(user_for_tests):
    register_data = {
        "name":"teste",
        "email":"maiara12@example.com",
        "password":"123",
        "sup":"true"
    }

    response = client.post("/auth/register/user",json=register_data)

    assert response.status_code == 400
    assert response.json()["detail"] == "super user already exist"



