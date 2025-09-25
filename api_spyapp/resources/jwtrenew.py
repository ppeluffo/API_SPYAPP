#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3

from flask_restful import Resource, reqparse
from dependency_injector.wiring import inject, Provide
from container import Container
from servicios.jwtrenew import JwtRenewService

class JWTRenewResource(Resource):

    @inject
    def __init__(self, service: JwtRenewService = Provide[Container.jwtrenew_service]):
        self.jwtrenew_service = service
        print(f"DEBUG:JWTRenewResource:__init__")

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('refresh_token',type=str,location='json',required=True)
        args=parser.parse_args()
        refresh_token = args['refresh_token']
        print(f"DEBUG:JWTRenewResource:IN: refresh_token={refresh_token}")

        # Servicio
        d_sresp = self.jwtrenew_service.jwtrenew(refresh_token=refresh_token)
        
        # Preparamos la respuesta del recurso
        if d_sresp['success'] == True:
            token = d_sresp['JWT']
            refresh_token = d_sresp['RJWT']
            d_jrsp = { 'rsp': 'OK', 'JWT': token, 'RJWT': refresh_token }
        else:
            d_jrsp = { 'rsp': 'ERR' }

        # Retorno la respuesta
        return d_jrsp, 200

    