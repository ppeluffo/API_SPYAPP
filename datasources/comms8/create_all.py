#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3

from .base import Base_comms8, engine_comms8
from . import models

def create_all():
    print("Creando base comms8...")
    Base_comms8.metadata.create_all( engine_comms8 )

if __name__ == "__main__":
    create_all()
    