#!/home/pablo/Spymovil/python/proyectos/SPYALL/venv/bin/python3

from api_spyapp.config import settings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine_gda = create_engine(url=settings.URL_GDA, echo=False, isolation_level="AUTOCOMMIT", connect_args={'connect_timeout': 5})
Session_gda = sessionmaker(bind=engine_gda)
session_gda = Session_gda()

Base_gda = declarative_base()