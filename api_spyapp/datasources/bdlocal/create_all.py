#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3

from .base import Base_local, engine_local
from . import models

def create_all():
    print("Creando base...")
    Base_local.metadata.create_all( engine_local )

if __name__ == "__main__":
    create_all()
    