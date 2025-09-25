#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3

from servicios.utilidades import token_get_payload, gen_new_token

class JwtRenewService:
    """
    No requiere repositorios ya que solo maneja JWT.
    """

    def __init__(self):
        print(f"DEBUG:JwtRenewService:__init__")

    def jwtrenew(self, refresh_token=None):

        print(f"DEBUG:JwtRenewService:IN: refresh_token={refresh_token}")
        payload = token_get_payload(refresh_token)
        if payload is None:
            print(f"ERROR:JwtRenewService: token invalid")
            return {'success': False}
        
        username = payload['username']
        print(f"DEBUG:JwtRenewService:IN: username={username}")

        # Genero un JWT nuevo de acceso y otro de refresh
        token = gen_new_token(username=username, exp_hours=1)            
        refresh_token = gen_new_token(username=username, exp_hours=24)   
        
        return {'success': True, 'JWT': token, 'RJWT': refresh_token}