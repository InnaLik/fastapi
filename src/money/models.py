from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class MoneyUser(Base):
    __tablename__ = 'money_user'


    id = Column(Integer, primary_key=True)
    name = Column(String, max_length=100)
    type_operation = Column(String)
    amount = Column(Integer)

