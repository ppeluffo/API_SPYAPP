#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3

from servicios.utilidades import gen_new_token

class LoginService:
    """
    Servicio de login:
    Recibe un usuario y contraseña y verifica con el repositorio si existe y la password es 
    valida.
    En este caso genera los tokens y los devuelve
    """
    def __init__(self, repositorio):
        self.users_repo = repositorio

    def login(self, username = None, password = None):

        print(f"DEBUG: Login Services")

        if self.users_repo.check_user(username,password):
            # Genero los tokens.
            token = gen_new_token(username=username, exp_hours=1)
            refresh_token = gen_new_token(username=username, exp_hours=24)
            return { 'success': True, 'JWT':token, 'RJWT':refresh_token}
        else:
            return { 'success': False}
