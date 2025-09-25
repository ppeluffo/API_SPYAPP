#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3

from abc import ABC, abstractmethod

class DbCOMMSInterface(ABC):

    @abstractmethod
    def get_dataloggers(self):
        pass
    
    @abstractmethod
    def get_tx48hs(self):
        pass