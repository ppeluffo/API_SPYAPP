#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3

from sqlalchemy import Column, Integer, String, DateTime, Double
from datetime import datetime
import pytz # For creating timezone-aware datetime objects
from sqlalchemy.orm import declarative_base

Base_comms8 = declarative_base()

class DatosHistoricos(Base_comms8):

    __tablename__ = 'historica'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    fechadata = Column(DateTime(timezone=False), nullable=True, default=datetime.now())
    fechasys = Column(DateTime(timezone=False), nullable=True, default=datetime.now())
    equipo = Column(String(50), nullable=True, default='DLG000')
    tag = Column(String(50), nullable=True, default='')
    valor = Column( Double, nullable=True)

    def __init__(self, fechadata,fechasys,equipo,tag, valor):
        self.fechadata = fechadata
        self.fechasys = fechasys
        self.equipo = equipo
        self.tag = tag
        self.valor = valor

    def __repr__(self):
        return f'Historico({self.fechadata}, {self.fechasys}, {self.equipo}, {self.tag}, {self.valor})'

    def __str__(self):
        return self.equipo
    