from sqlalchemy import Integer, String, TIMESTAMP
from sqlalchemy.orm import declarative_base
from sqlalchemy.testing.schema import Column

Base = declarative_base()


class Operation(Base):
    __tablename__ = 'operation'

    id = Column(Integer, primary_key=True)
    quantity = Column(String)
    figi = Column(String)
    instrument_type = Column(String, nullable=True)
    date = Column(TIMESTAMP)
    type = Column(String)
