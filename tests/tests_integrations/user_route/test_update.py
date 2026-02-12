import pytest
from fastapi.testclient import TestClient
from models.user_model import User 
from sqlalchemy.orm import sessionmaker
from main import app
from models.database import db,Base
from services.encrypt_password import encrypt_password

client = TestClient(app)

@pytest.fixture(autouse=True)

def setub_db():
    Base.metadata.create_all(bind=db)
    yield 
    Base.metadata.drop_all(bind=db)

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

def test_profile(create_user_for_tests):
    response_for_token = client.post("/auth/login_form",data={"username":"marciorlisboa7@gmail.com","password":"123"})
    token = response_for_token.json()["access_token"]

    req_data = {
        "name":"augusto",
        "email":"augusto@example.com"
    }

    response = client.patch("/user/profile/update",headers={"Authorization": f"Bearer {token}"},json=req_data)

    assert response.status_code == 200
    assert response.json()["message"] == "user data change"