from models.database import Base
from sqlalchemy import  Column, Integer, String, Boolean

class User (Base):
    __tablename__ = 'user'
    id = Column("id",Integer,primary_key=True,autoincrement=True)
    name = Column("name",String)
    email = Column("email",String,unique=True)
    password = Column("password",String)
    frequency = Column('frequency',Integer, default=0)
    sup = Column('sup',Boolean, default=False)

    def __init__(self,name,email,password,frequency = 0,sup = False):
        self.name = name
        self.email = email
        self.password = password
        self.frequency = frequency
        self.sup = sup
        

