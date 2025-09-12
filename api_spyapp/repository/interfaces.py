#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3

from abc import ABC, abstractmethod

class AutentificacionRepoInterface(ABC):
    @abstractmethod
    def autentificar(self, username=None, password=None):
        pass

    @abstractmethod
    def check_if_user_exists(self, username=None):
        pass

    @abstractmethod
    def update_password_code(self, username=None, code=None, fecha_emision_code=None):
        pass

    @abstractmethod
    def get_passwd_code(self, username=None):
        pass
    
    @abstractmethod
    def update_password(self, username=None, password=None):
        pass
