#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3

from flask_restful import Resource, reqparse
from flask_jwt_extended import get_jwt_identity, jwt_required
import ast
from dependency_injector.wiring import inject, Provide
from container import Container
from servicios.datosonlinedlglist import DatosOnlineDlgListService

class DatosOnlineDlgListResource(Resource):
    """
    Recurso de leer datos online habiendo recibido una lista de dataloggers
    """
    @inject
    def __init__(self, service: DatosOnlineDlgListService = Provide[Container.datosonlinedlglist_service]):
        self.datosonlinedlglist_service = service

    @jwt_required()
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('l_dlgid',type=str,location='json',required=True)
        args=parser.parse_args()
        # La lista que recibo del json es un string asi que la debo convertir !!!
        l_dlgid_str = args['l_dlgid']
        l_dlgid = ast.literal_eval(l_dlgid_str)

        print(f"DEBUG: DatosOnlineDlgList Resources:IN")

        # Solicito el servicio correspondiente. Devuelve un dataframe
        d_sresp = self.datosonlinedlglist_service.datosonlinedlglist(l_dlgid)
        
        if d_sresp['success'] == True:
            jdf = d_sresp['jdf']
            # devuelve una lista de dicts, que es lo que esperan las APIs REST
            d_jrsp = { 'rsp': 'OK', 'datos': jdf }
        else:
            d_jrsp = { 'rsp': 'ERR' }

        # Retorno la respuesta
        return d_jrsp, 200
    
    