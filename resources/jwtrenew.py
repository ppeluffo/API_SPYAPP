#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3

from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from dependency_injector.wiring import inject, Provide
from container import Container
from servicios.jwtrenew import JwtRenewService

class JWTRenewResource(Resource):

    @inject
    def __init__(self, service: JwtRenewService = Provide[Container.jwtrenew_service]):
        self.jwtrenew_service = service
        print(f"DEBUG:JWTRenewResource:__init__")

    @jwt_required()
    def post(self):
        """
        No recibimos parámetros. Solo el RJWT que viene en el header de autorizacion
        """

        print(f"DEBUG:JWTRenewResource:IN:")
        # Servicio
        d_sresp = self.jwtrenew_service.jwtrenew()

        # Preparamos la respuesta del recurso
        if d_sresp['success'] == True:
            token = d_sresp['JWT']
            refresh_token = d_sresp['RJWT']
            d_jrsp = { 'rsp': 'OK', 'JWT': token, 'RJWT': refresh_token }
        else:
            d_jrsp = { 'rsp': 'ERR' }

        # Retorno la respuesta
        return d_jrsp, 200

    