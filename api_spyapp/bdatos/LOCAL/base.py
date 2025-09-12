#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3

from api_spyapp.config import settings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine_local = create_engine(url=settings.URL_LOCAL, echo=False, isolation_level="AUTOCOMMIT", connect_args={'connect_timeout': 5})
Session_local = sessionmaker(bind=engine_local)
session_local = Session_local()

Base_local = declarative_base()
