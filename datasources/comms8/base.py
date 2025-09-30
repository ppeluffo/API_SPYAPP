#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3

from config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine_bdcomms8 = create_engine(url=settings.URL_COMMS8, echo=False, isolation_level="AUTOCOMMIT", connect_args={'connect_timeout': 5})
Session_bdcomms8 = sessionmaker(bind=engine_bdcomms8)
session_bdcomms8 = Session_bdcomms8()

Base_comms8 = declarative_base()
