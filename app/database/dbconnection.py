from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

db_username=os.getenv("DB_USERNAME")
db_password=os.getenv("DB_PASSWORD")

print(db_username)
print(db_password)
db_url=f"postgresql+psycopg2://{db_username}:{db_password}@localhost:5432/expenses_db"



#Establish DB connection
engine=create_engine(db_url)

session=sessionmaker(autocommit=False,autoflush=False,bind=engine)
