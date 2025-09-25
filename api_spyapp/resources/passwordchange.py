#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3

from flask_restful import Resource, reqparse
from dependency_injector.wiring import inject, Provide
from container import Container
from servicios.passwordchange import PasswordChangeService

class PasswordChangeResource(Resource):
    """
    Procesa los requests de solicitud de cambio de contraseña.
    Recibe las 2 contraseñas y el security code.
    """

    @inject
    def __init__(self, service: PasswordChangeService = Provide[Container.passwordchange_service]):
        self.passwordchange_service = service

    def post(self):
        """
        Solo pido el username ya que el usuario no tiene password por lo que no se
        pudo autentificar y por lo tanto no tiene un jwt valido
        """
        parser = reqparse.RequestParser()
        parser.add_argument('username',type=str,location='json',required=True)
        parser.add_argument('password1',type=str,location='json',required=True)
        parser.add_argument('password2',type=str,location='json',required=True)
        parser.add_argument('passwd_code',type=str,location='json',required=True)
        args=parser.parse_args()
        username = args['username']
        password1 = args['password1']
        password2 = args['password2']
        passwd_code = args['passwd_code']

        print(f"DEBUG: PasswordChangeResource")
        d_sresp = self.passwordchange_service.passwordchange(username,
                                                            password1,
                                                            password2,
                                                            passwd_code)

        # Preparamos la respuesta del recurso
        if d_sresp['success'] == True:
            d_jrsp = { 'rsp': 'OK' }
        else:
            d_jrsp = { 'rsp': 'ERR' }

        # Retorno la respuesta
        return d_jrsp, 200