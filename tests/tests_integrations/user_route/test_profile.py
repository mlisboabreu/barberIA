
from fastapi.testclient import TestClient
from main import app
from models.database import db,Base
from services.create_user_for_tests import create_user_for_tests
from services.setup_db import setub_db

client = TestClient(app)



def test_profile(create_user_for_tests):
    response_for_token = client.post("/auth/login_form",data={"username":"marciorlisboa7@gmail.com","password":"123"})
    token = response_for_token.json()["access_token"]

    response = client.get("/user/profile",headers={"Authorization": f"Bearer {token}"})

    assert response.status_code == 200
    assert response.json()["name"] == "marcio"