from models.database import Base
from sqlalchemy import  Column, Integer, Float, ForeignKey, Date, String, Table
from sqlalchemy.orm import relationship

service_association = Table(
    'service_association',
    Base.metadata,
    Column("agendamento", Integer, ForeignKey("services.id")),
    Column("service", Integer, ForeignKey("service.id"))
)

class Services(Base):
    __tablename__ = 'services'
    id = Column('id',Integer,autoincrement=True,primary_key=True)
    user = Column('user',ForeignKey("user.id"))
    items = relationship(
        "Service",
        secondary=service_association,
        backref="agendamento"

    )
    price = Column('price',Float)
    date = Column('date', String)
    status = Column('status', String, default="pendente")

    def __init__(self,user,items,price,date,status):
        self.user = user
        self.items = items or []
        self.price = price
        self.date = date
        self.status = status
        
        
