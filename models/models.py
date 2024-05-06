import datetime
from sqlalchemy import Integer, String, TIMESTAMP, ForeignKey, Column, JSON, MetaData

Base = MetaData()


class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    permission = Column(JSON)


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    password = Column(Integer, nullable=False)
    registration_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)
    role_id = Column(Integer, ForeignKey("roles.id"))
