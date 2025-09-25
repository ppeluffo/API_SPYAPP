#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3

from abc import ABC, abstractmethod

class DbGDAInterface(ABC):
    @abstractmethod
    def get_instalaciones(self):
        pass