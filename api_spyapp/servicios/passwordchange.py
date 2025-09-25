#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3

from servicios.utilidades import verify_password

class PasswordChangeService:
    """
    No requiere repositorios ya que solo maneja JWT.
    """

    def __init__(self, repositorio):
        self.users_repo = repositorio

    def passwordchange(self, username=None, password1=None,password2=None,passwd_code=None):
        """
        Verificamos que los datos sean valido y luego cambiamos la contraseña.
        """
        print(f"DEBUG:PasswordChangeService:IN: username={username}")

        # Usuario existe ?:
        if not self.users_repo.user_exists(username):
            print(f"DEBUG:PasswordChangeService:OUT. Usuario no existe")
            return {'success':False}
        
        # Contraseñas iguales:
        if password1 != password2:
            print(f"DEBUG:PasswordChangeService:OUT. password1 <> password2")
            return {'success':False}
        
        # Contraseñas válidas:
        if not verify_password(password=password1):
            print(f"DEBUG:PasswordChangeService:OUT. password no valida")
            return {'success':False}
        
        if passwd_code is None:
            print(f"DEBUG:PasswordChangeService:OUT. code no valido")
            return {'success':False}
        
        if self.users_repo.update_password(username=username,password=password1, code=passwd_code):
            return {'success':True}
        else:
            print(f"DEBUG:PasswordChangeService:OUT. update_password error")
            return {'success':False}

        
