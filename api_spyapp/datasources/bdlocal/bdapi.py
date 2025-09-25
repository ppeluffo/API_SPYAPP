#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3
"""
REFS:
Autentificacion: https://www.geeksforgeeks.org/python/using-jwt-for-user-authentication-in-flask/

"""
from .models import Usuarios
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timezone, timedelta
import pytz

class DbLocal:

    def __init__(self, session_factory):
        """
        Uso inyeccion de dependencias en el constructor.
        """
        self.session_factory = session_factory
        print(f"DEBUG:DbLocal:__init__")

    def user_exists(self, username=None):
        """
        Verifica que exista una entrada con el username proporcionado en la BD
        Return: True/False
        """
        print(f"DEBUG:DbLocal:user_exists:IN: username={username}")
        # Verify integridad de datos.
        if username is None:
            print(f"DEBUG:DbLocal:user_exists:OUT: username=None")
            return False

        try:
            with self.session_factory() as session:
                user = session.query(Usuarios).filter(Usuarios.username == username).first()

        except Exception as e:
            print(f"ERROR:DbLocal:user_exists, Error={e}")
            return False
        
        if user is None:
            print(f"DEBUG:DbLocal:user_exists:OUT: bduser=None")
            return False
        
        print(f"DEBUG:DbLocal:user_exists:OUT")
        return True

    def check_user(self, username=None, password=None):
        """
        Verifica que exista una entrada con el username/password proporcionadas en la BD
        Return: True/False
        """
        print(f"DEBUG:DbLocal:check_user:IN: username={username}, password={password}")
        # Verify integridad de datos.
        if username is None:
            print(f"DEBUG:DbLocal:check_user:OUT: username=None")
            return False
        
        if password is None:
            print(f"DEBUG:DbLocal:check_user:OUT: password=None")
            return False

        try:
            with self.session_factory() as session:
                user = session.query(Usuarios).filter(Usuarios.username == username).first()
        except Exception as e:
            print(f"ERROR:DbLocal:check_user, Error={e}")
            return False
        
        if user is None:
            print(f"DEBUG:DbLocal:check_user:OUT: bduser=None")
            return False
        
        if not check_password_hash(user.password, password):
            print(f"DEBUG:DbLocal:check_user:OUT: check_password_hash ERR")
            return False
        
        print(f"DEBUG:DbLocal:check_user:OUT")
        return True
    
    def createuser(self, username=None, password=None):
        """
        Ingresa un nuevo usuario a la BD si ya no esta.
        Return: True/False
        """
        print(f"DEBUG:DbLocal:createuser:IN: username={username}, password={password}")
        
        # Verify integridad de datos.
        if username is None:
            print(f"DEBUG:DbLocal:createuser:OUT: username=None")
            return False
        
        if password is None:
            print(f"DEBUG:DbLocal:createuser:OUT: password=None")
            return False
        
        try:
            with self.session_factory() as session:
                existing_user = session.query(Usuarios).filter(Usuarios.username == username).first()
        except Exception as e:
            print(f"ERROR:DbLocal:createuser, Error1={e}")
            return False
        
        if existing_user:
            print(f"DEBUG:DbLocal:createuser:OUT: user exists")
            return False

        # El usuario no esta: lo creo
        hashed_password = generate_password_hash(password)
        try:
            with self.session_factory() as session:
                new_user = Usuarios( username=username, password=hashed_password)
                session.add(new_user)
                session.commit()

        except Exception as e:
            print(f"ERROR:DbLocal:createuser, Error2={e}")
            return False
        
        print(f"DEBUG:DbLocal:createuser:OUT")
        return True

    def update_passcode(self, username=None, code=None):

        print(f"DEBUG:DbLocal:update_passcode:IN: username={username}, code={code}")
        
        # Verify integridad de datos.
        if username is None:
            print(f"DEBUG:DbLocal:update_passcode:OUT: username=None")
            return False
        
        if code is None:
            print(f"DEBUG:DbLocal:update_passcode:OUT: code=None")
            return False
        
        now = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
        # Actualizo el registro:
        try:
            with self.session_factory() as session:
                user = session.query(Usuarios).filter(Usuarios.username == username).first()
                user.code = code
                user.fecha_emision_code = datetime.now(timezone.utc)
                session.commit()
        except Exception as e:
            print(f"ERROR:DbLocal:update_passcode, Error1={e}")
            return False
        
        print(f"DEBUG:DbLocal:update_passcode:OUT")
        return True
        
    def update_password(self, username=None, password=None, code=None):
        """
        El username,password,code ya estan chequeados del servicio que son válidos
        """
        # Actualizo el registro:
        print(f"DEBUG:DbLocal:update_password:IN")
        try:
            with self.session_factory() as session:
                user = session.query(Usuarios).filter(Usuarios.username == username, Usuarios.code == code).first()
                print(f"DEBUG:DbLocal: user={user}")
                if user:
                    # Verifico que el code no haya expirado( menos 1 hora)
                    fecha_expira_code = user.fecha_emision_code + timedelta(hours=1)
                    now = datetime.now(timezone.utc)
                    if fecha_expira_code < now:
                        return False
                    #
                    # Actualizo la passwd
                    hashed_password = generate_password_hash(password)
                    user.password = hashed_password
                    user.code = "000000"
                    #user.fecha_emision_code = datetime.now(pytz.utc)
                    user.fecha_emision_code = datetime.now(pytz.utc)
                    session.commit()
                else:
                    print(f"DEBUG:DbLocal:update_password: user|code not exists")
                    return False

        except Exception as e:
            print(f"ERROR:DbLocal:update_password, Error1={e}")
            return False
        
        print(f"DEBUG:DbLocal:update_password:OUT")
        return True
  



        
