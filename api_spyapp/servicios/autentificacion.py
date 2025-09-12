#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3

"""
Definimos las funciones que implementan los servicios que consume la API
"""

from api_spyapp.repository.interfaces import AutentificacionRepoInterface
from api_spyapp.servicios.notificaciones import NotificacionesInterface
from api_spyapp.utilidades.interfaces import LoggerInterface

from api_spyapp.utilidades.auxfunctions import gen_new_token, token_is_valid, token_get_payload, verify_passwords, verify_code
import random
from datetime import datetime, timezone

class AutentificacionService:

    def __init__(self, 
                 autentification_repo: AutentificacionRepoInterface, 
                 logger: LoggerInterface,
                 notifier: NotificacionesInterface
                 ):
        """
        Uso inyeccion de dependencias en el constructor.
        """
        self.repo = autentification_repo
        self.logger = logger
        self.notifier = notifier

    def autentificar(self, username=None, password=None):
        """
        Mandamos al repositorio la consulta.
        Si es positiva, generamos el jwt.
        Si no retornamos None

        Return: (jwt,rjwt)
                None
        """
        if self.repo.autentificar(username, password):
            # Genero un JWT nuevo de acceso y otro de refresh
            token_acceso = gen_new_token(username=username, exp_hours=1)            
            token_refresh = gen_new_token(username=username, exp_hours=24)   
            return token_acceso, token_refresh
        
        else:
            self.logger( __name__, f"{username} no autenticado.")
            return None
        
    def renew_tokens(self, refresh_token=None):
        """
        Si el refresh_token es válido, genera 2 nuevos tokens y los envia.

        Return: (jwt,rjwt)
                None
        """
        if token_is_valid(self.repo, refresh_token):
            payload = token_get_payload(refresh_token)
            username = payload['username']
            # Genero un JWT nuevo de acceso y otro de refresh
            token_acceso = gen_new_token(username=username, exp_hours=1)            
            token_refresh = gen_new_token(username=username, exp_hours=24)   
            return token_acceso, token_refresh
        
        else:
            self.logger( __name__, f"token no valido [{refresh_token}]")
            return None

    def request_change_password_code(self, username=None):
        """
        Solicita un código para cambio de contraseña.
        Si el usuario existe, se genera un código que se manda por email al usuario.
        No retorna nada ya que no se verifica si el usuario existe o no.
        Si existe se manda: si no existe no se manda.

        Return: code
        """
        code = None
        if self.repo.check_if_user_exists(username):
            code = random.randint(100000, 999999)
            fecha_emision_code = datetime.now(timezone.utc)
            self.repo.update_password_code(username, code, fecha_emision_code)

            msg = f"""
                El código de autorizacion para cambio de contraseña es: {code}\r
                El mismo expira en 1h. 
                Luego de este tiempo debera solicitar uno nuevo.
                Spymovil SRL.
                """
            self.notifier.sendEmail(username, msg)
        return code

    def password_change(self, username=None, password1=None, password2=None, code=None):
        """
        Si luego de verificar los datos, estos son correctos, cambia la password.

        Return: True
                False
        """
        if verify_passwords(self.logger, password1, password2) and verify_code(self.repo, username, code):
            self.repo.update_password(username, password1)
            return True
        return False
    
