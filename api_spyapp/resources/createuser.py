#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3

from flask_restful import Resource, reqparse
from dependency_injector.wiring import inject, Provide
from container import Container
from servicios.createuser import CreateUserService

class CreateUserResource(Resource):

    @inject
    def __init__(self, service: CreateUserService = Provide[Container.createuser_service]):
        self.createUser_service = service
        print(f"DEBUG:CreateUserResource:__init__")

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username',type=str,location='json',required=True)
        parser.add_argument('password',type=str,location='json',required=True)
        args=parser.parse_args()
        username = args['username']
        password = args['password']
        print(f"DEBUG:CreateUserResource:IN: username={username},password={password}")

        if self.createUser_service.createuser(username,password):
            d_rsp = { 'rsp': 'OK'}
        else:
            d_rsp = { 'rsp': 'FAIL'}
            
        print(f"DEBUG:CreateUserResource:OUT")
        return d_rsp, 200
    