#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3

from flask_restful import Resource, reqparse
from dependency_injector.wiring import inject, Provide
from container import Container
from servicios.passwordcode import PasswordCodeService

class PasswordCodeResource(Resource):
    """
    Solicita un código para cambio de contraseña.
    Si el usuario existe, se genera un código que se manda por email al usuario.
    No retorna nada ya que no se verifica si el usuario existe o no.
    Si existe se manda: si no existe no se manda.

    El username lo extraemos del jwt
    
    """

    @inject
    def __init__(self, service: PasswordCodeService = Provide[Container.passwordcode_service]):
        self.passwordcode_service = service

    def post(self):
        """
        Solo pido el username ya que el usuario no tiene password por lo que no se
        pudo autentificar y por lo tanto no tiene un jwt valido
        """
        parser = reqparse.RequestParser()
        parser.add_argument('username',type=str,location='json',required=True)
        args=parser.parse_args()
        username = args['username']

        print(f"DEBUG: PasswordCodeResource")
        d_sresp = self.passwordcode_service.passwordcode(username=username)

        # Preparamos la respuesta del recurso
        # El codigo se envia por email al username. Siempre devuelvo OK
        #if d_sresp['success'] == True:
        #    d_jrsp = { 'rsp': 'OK' }
        #else:
        #    d_jrsp = { 'rsp': 'ERR' }

        d_jrsp = { 'rsp': 'OK' }
        # Retorno la respuesta
        return d_jrsp, 200