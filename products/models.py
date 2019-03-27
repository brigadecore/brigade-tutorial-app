from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


class Base:
    pass


DeclarativeBase = declarative_base(cls=Base)


class Product(DeclarativeBase):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
