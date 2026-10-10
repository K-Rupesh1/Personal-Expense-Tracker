from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,Date


Base=declarative_base()

class Expense(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    amount = Column(Integer)
    category = Column(String)
    expense_date = Column(Date)

class Expense(Base):
    __tablename__ = "expenses1"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    amount = Column(Integer)
    category = Column(String)
    expense_date = Column(Date)
class Users(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True)
    age = Column(Integer, nullable=True)