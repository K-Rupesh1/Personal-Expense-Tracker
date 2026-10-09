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
