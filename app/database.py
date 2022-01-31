from sqlalchemy import create_engine
import urllib.parse
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
import time

SQLALCHEMY_DATABASE_URL = f'postgresql://postgres:Generous%402020@localhost/fastapi'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
urllib.parse.quote_plus("Generous@2020")


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


################# DATABASE CONNECTION ##################
#while True:
    #try:
        #conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='Generous@2020', cursor_factory=RealDictCursor)
        #cursor = conn.cursor()
       # print("Database connection was successful")
      #  break
    #except Exception as error:
       # print("Connection failed")
       # print("Error: ", error)
       # time.sleep(2)
