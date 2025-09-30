#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3

from servicios.utilidades import gen_new_token, token_is_valid
from flask_jwt_extended import get_jwt_identity


class JwtRenewService:
    """
    No requiere repositorios ya que solo maneja JWT.
    """

    def __init__(self, repositorio):
        self.users_repo = repositorio
        print(f"DEBUG:JwtRenewService:__init__")

    def jwtrenew(self):

        print(f"DEBUG:JwtRenewService:IN:")

        # Valido el token de acceso
        if token_is_valid(repo=self.users_repo):
            # Genero un JWT nuevo de acceso y otro de refresh
            current_user = get_jwt_identity()
            token = gen_new_token(username=current_user, exp_hours=1)            
            refresh_token = gen_new_token(username=current_user, exp_hours=24)   
            return {'success': True, 'JWT': token, 'RJWT': refresh_token}
        else:
            return {'success': False }
        
