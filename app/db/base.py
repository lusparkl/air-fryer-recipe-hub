import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()
CONNECTION_STRING=os.getenv("CONNECTION_STRING")

engine = create_engine(CONNECTION_STRING, echo=True)

Base = declarative_base()

Session = sessionmaker(bind=engine)