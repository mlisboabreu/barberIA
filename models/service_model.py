from models.database import Base
from sqlalchemy import  Column, Integer, String, Float

class Service(Base):
    __tablename__ = 'service'
    id = Column('id',Integer, autoincrement=True, primary_key=True)
    service_name = Column('service_name',String)
    price = Column('price',Float)

    def __init__(self,service_name,price):
        self.service_name = service_name
        self.price = price