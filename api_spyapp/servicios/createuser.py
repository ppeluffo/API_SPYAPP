#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3

from servicios.utilidades import verify_username, verify_password

class CreateUserService:
    """
    Servicio de crear un usuario nuevo.
    Verifica que no exista en la BDlocal.
    Si existe devuelve un error.
    Si no existe, lo crea.
    """
    def __init__(self, repositorio):
        self.users_repo = repositorio
        print(f"DEBUG:CreateUserService:__init__")
        
    def createuser(self, username = None, password = None):
        print(f"DEBUG:CreateUserService:IN: username={username},password={password}")

        # Si el usuario existe, salgo
        if self.users_repo.user_exists(username):
            print(f"DEBUG:CreateUserService:OUT>>user_exists")
            return False
        
        # Verifico el username y password
        if not verify_username(username):
            print(f"DEBUG:CreateUserService:OUT>>verify_username")
            return False
        
        if not verify_password(password):
            print(f"DEBUG:CreateUserService:OUT>>verify_password")
            return False

        if self.users_repo.createuser(username,password):
            print(f"DEBUG:CreateUserService:OUT>>createuser")
            return True
        else:
            print(f"DEBUG:CreateUserService:OUT>>createuser Err")
            return False

        

    