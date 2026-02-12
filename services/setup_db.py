import pytest
from models.database import db,Base

@pytest.fixture(autouse=True)

def setub_db():
    Base.metadata.create_all(bind=db)
    yield 
    Base.metadata.drop_all(bind=db)