#Todo: move connection string to other file
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('mysql://root:SuperSecretDBPassword@localhost:3306/air_fryer_heaven', echo=True)

Base = declarative_base()

Session = sessionmaker(bind=engine)