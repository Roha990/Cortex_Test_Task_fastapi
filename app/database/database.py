from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Date, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship

from app.config import get_datebase

DATABASE_URL = get_datebase()

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class Position(Base):
    __tablename__ = "positions"

    id = Column(Integer, primary_key=True)
    title = Column(String)

    employees = relationship("Employee", back_populates="position")


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    last_name = Column(String)
    first_name = Column(String)
    middle_name = Column(String)
    position_id = Column(Integer, ForeignKey("positions.id"))
    hire_date = Column(Date)

    position = relationship("Position", back_populates="employees")
