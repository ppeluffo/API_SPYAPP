#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3

from api_spyapp.repository.interfaces import AutentificacionRepoInterface
from api_spyapp.bdatos.LOCAL.interfaces import DbLocalInterface

class AutentificacionRepo(AutentificacionRepoInterface):

    def __init__(self, api_db:DbLocalInterface):
        """
        Uso inyeccion de dependencias en el constructor.
        """
        self.api_bd = api_db

    def autentificar(self, username=None, password=None):
        """
        La autentificacion de usuario la hacemos siempre sobre la base local.
        """
        return self.api_bd.autentificar(username, password)

    def check_if_user_exists(self, username=None):
        """
        Solo verifica si en la BD existe el username
        """
        return self.api_bd.check_if_user_exists(username)
    
    def update_password_code(self, username=None, code=None, fecha_emision_code=None):
        """
        Actualiza en la BD el registro del usuario con el password code y la fecha de emisión
        """
        return self.api_bd.update_password_code(username, code, fecha_emision_code)

    def get_passwd_code(self, username=None):
        """
        Solicita al BD el codigo de cambio de contraseña y su fecha de expiración
        """
        return self.api_bd.get_passwd_code(username)

    def update_password(self, username=None, password=None):
        """
        Actualiza el campo password en la tabla Usuarios de la BD.
        """
        return self.api_bd.update_password(username, password)
