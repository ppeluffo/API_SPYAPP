#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3

from abc import ABC, abstractmethod

class LoggerInterface(ABC):
    @abstractmethod
    def log(source_function=None, message=None):
        pass
    