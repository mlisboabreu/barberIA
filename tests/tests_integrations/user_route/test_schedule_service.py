from fastapi.testclient import TestClient
from models.services_model import Services
from models.database import db,Base
from services.create_user_for_tests import create_user_for_tests
from services.setup_db import setub_db
from main import app
import pytest
from models.service_model import Service
from sqlalchemy.orm import sessionmaker

client = TestClient(app)

@pytest.fixture
def create_service_for_tests():
    Session = sessionmaker(bind=db)
    session = Session()
    
    service = Service(
        service_name="haircut",
        price= 30
    )

    session.add(service)
    session.commit()
    yield service
    session.refresh(service)
    session.close()


def test_schendule_service(create_user_for_tests,create_service_for_tests):
    response_for_token = client.post("/auth/login_form",data={"username":"marciorlisboa7@gmail.com","password":"123"})
    token = response_for_token.json()["access_token"]

    response = client.post("/user/schedule_service",headers={"Authorization": f"Bearer {token}"},json={"items":["haircut"]})

    assert response.status_code == 200
    assert response.json()["message"] == "scheduled service"


def test_schendule_service_service_not_found(create_user_for_tests,create_service_for_tests):
    response_for_token = client.post("/auth/login_form",data={"username":"marciorlisboa7@gmail.com","password":"123"})
    token = response_for_token.json()["access_token"]

    response = client.post("/user/schedule_service",headers={"Authorization": f"Bearer {token}"},json={"items":["beard"]})

    assert response.status_code == 200
    assert response.json()["message"] == "service not found"