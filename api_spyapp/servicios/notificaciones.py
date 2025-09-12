#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3

from abc import ABC, abstractmethod

class NotificacionesInterface(ABC):
    @abstractmethod
    def sendEmail(self, email_address=None, message=None):
        pass


class Notificaciones(NotificacionesInterface):

    def __init__(self, email_service):
        self.email_service = email_service

    def sendEmail(self, email_address=None, message=None):
        self.email_service(__name__, message)
        
