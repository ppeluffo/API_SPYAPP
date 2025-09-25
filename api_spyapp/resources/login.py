#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3

from flask_restful import Resource, reqparse
from dependency_injector.wiring import inject, Provide
from container import Container
from servicios.login import LoginService

class LoginResource(Resource):
    """
    Implementacion del recurso API de login.
    Protocolo: POST
    Input:
        - username
        - password
    Output:
        - Status
        - jwt
        - rjwt
    Action:
        Utiliza el servicio de Login

    """
    @inject
    def __init__(self, service: LoginService = Provide[Container.login_service]):
        self.login_service = service

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username',type=str,location='json',required=True)
        parser.add_argument('password',type=str,location='json',required=True)
        args=parser.parse_args()
        username = args['username']
        password = args['password']

        print(f"DEBUG: Login Resources")
        # Solicito el servicio correspondiente. Devuelve un diccionario
        d_sresp = self.login_service.login(username,password)

        # Preparamos la respuesta del recurso
        if d_sresp['success'] == True:
            token = d_sresp['JWT']
            refresh_token = d_sresp['RJWT']
            d_jrsp = { 'rsp': 'OK', 'JWT': token, 'RJWT': refresh_token }
        else:
            d_jrsp = { 'rsp': 'ERR', 'JWT': None, 'RJWT': None }

        # Retorno la respuesta
        return d_jrsp, 200
    
    