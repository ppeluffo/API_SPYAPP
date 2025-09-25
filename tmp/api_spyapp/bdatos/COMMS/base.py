#!/home/pablo/Spymovil/python/proyectos/SPYALL/venv/bin/python3

from api_spyapp.config import settings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine_comms = create_engine(url=settings.URL_COMMS, echo=False, isolation_level="AUTOCOMMIT", connect_args={'connect_timeout': 5})
Session_comms = sessionmaker(bind=engine_comms)
session_comms = Session_comms()

Base_comms = declarative_base()