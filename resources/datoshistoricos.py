#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3

from flask_restful import Resource, reqparse
from flask_jwt_extended import get_jwt_identity, jwt_required
from dependency_injector.wiring import inject, Provide
from container import Container
from servicios.datoshistoricos import DatosHistoricosService

class DatosHistoricosResource(Resource):
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
    def __init__(self, service: DatosHistoricosService = Provide[Container.datoshistoricos_service]):
        self.datoshistoricos_service = service

    @jwt_required()
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('dlgid',type=str,location='json',required=True)
        args=parser.parse_args()
        dlgid = args['dlgid']

        print(f"DEBUG: DatosHistoricos Resources:IN ")
        # Solicito el servicio correspondiente. Devuelve un dataframe
        d_sresp = self.datoshistoricos_service.datoshistoricos(dlgid)
        
        if d_sresp['success'] == True:
            jdf = d_sresp['jdf']
            # devuelve una lista de dicts, que es lo que esperan las APIs REST
            d_jrsp = { 'rsp': 'OK', 'datos': jdf }
        else:
            d_jrsp = { 'rsp': 'ERR' }

        # Retorno la respuesta
        return d_jrsp, 200
    
    