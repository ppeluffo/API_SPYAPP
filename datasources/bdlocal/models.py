#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3

from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
import pytz # For creating timezone-aware datetime objects
from sqlalchemy.ext.declarative import declarative_base

Base_local = declarative_base()

class Usuarios(Base_local):

    __tablename__ = 'usuarios'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False, index=True)
    code = Column(String(50), nullable=True, default='000000')
    fecha_emision_code = Column(DateTime(timezone=True), nullable=True, default=datetime.now(pytz.utc))
    password = Column(String(512), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.fecha_emision_code = None
        self.code = None

    def __repr__(self):
        return f'Usuario({self.username}, {self.password}, {self.fecha_emision_code}, {self.code})'

    def __str__(self):
        return self.username
    