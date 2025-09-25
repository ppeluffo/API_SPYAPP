#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3
"""
REFS:
Autentificacion: https://www.geeksforgeeks.org/python/using-jwt-for-user-authentication-in-flask/

"""
from .base import session_local
from .models import Usuarios
from api_spyapp.bdatos.LOCAL.interfaces import DbLocalInterface
from werkzeug.security import generate_password_hash, check_password_hash

class DbLocal(DbLocalInterface):

    def __init__(self, logger):
        """
        Uso inyeccion de dependencias en el constructor.
        """
        self.logger = logger

    def register_new_user(self, username=None, password=None):
        """
        Ingresa un nuevo usuario a la BD si ya no esta.
        Return: True/False
        """
        # Verify integridad de datos.
        if (username is None) or (password is None):
            return False
        try:
            existing_user = session_local.query(Usuarios).filter(Usuarios.username == username).first()
        except Exception as e:
            self.logger(__name__, f"ERROR: {e}")
            return False
        
        if existing_user:
            return False

        hashed_password = generate_password_hash(password)
        try:
            new_user = Usuarios( username=username, password=hashed_password)
            session_local.add(new_user)
            session_local.commit()
        except Exception as e:
            self.logger(__name__, f"ERROR: {e}")
            return False
        
        return True

    def autentificar(self, username=None, password=None):
        """
        Verifica que exista una entrada con el username/password proporcionadas en la BD
        Return: True/False
        """
        # Verify integridad de datos.
        if (username is None) or (password is None):
            return False

        try:
            user = session_local.query(Usuarios).filter(Usuarios.username == username).first()
        except Exception as e:
            self.logger(__name__, f"ERROR: {e}")
            return False
        
        if user is None:
            return False
        
        if not check_password_hash(user.password, password):
            return False
        
        return True
    
    def check_if_user_exists(self, username=None):
        """
        Verifica solo si existe el usuario.
        """
        if (username is None) :
            return False

        try:
            rcd = session_local.query(Usuarios).filter(Usuarios.username == username).first()
        except Exception as e:
            self.logger(__name__, f"ERROR: {e}")
            return False
        
        if rcd is None:
            return False
        
        return True

    def update_password_code(self, username=None, code=None, fecha_emision_code=None):
        """
        Actualizo el registro del usuario con el codigo y la fecha de emision
        """
        try:
            user = session_local.query(Usuarios).filter(Usuarios.username == username).first()
            user.code = code
            user.fecha_emision_code = fecha_emision_code
            session_local.commit()
        except Exception as e:
            self.logger(__name__, f"ERROR: {e}")
        
    def get_passwd_code(self, username=None):
        """
        Retorna el password code y la fecha de expiracion para el usuario dado
        """
        code = None
        fecha_emision_code = None
        try:
            user = session_local.query(Usuarios).filter(Usuarios.username == username).first()
            code = user.code
            fecha_emision_code = user.fecha_emision_code
        except Exception as e:
            self.logger(__name__, f"ERROR: {e}")
    
        return code, fecha_emision_code

    def update_password(self, username=None, password=None):
        """
        Actualiza la contraseña del usuario: borra el codigo y la fecha de emision
        """
        hashed_password = generate_password_hash(password)
        try:
            user = session_local.query(Usuarios).filter(Usuarios.username == username).first()
            user.password = hashed_password
            user.code = None
            user.fecha_emision_code = None
            session_local.commit()
        except Exception as e:
            self.logger(__name__, f"ERROR: {e}")
            return False
        return True
