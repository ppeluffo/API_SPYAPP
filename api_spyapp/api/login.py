#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3

from flask_restful import Resource, request, reqparse
from flask import Response


class Login(Resource):

    def __init__(self, **kwargs):
        self.app = kwargs['app']

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username',type=str,location='json',required=True)
        parser.add_argument('password',type=str,location='json',required=True)
        args=parser.parse_args()
        username = args['username']
        password = args['password']

        print(f"ApiAUTH DEBUG: POST Login: username={username}, password={password}")

        rsp, jwt = verify_user(username,password)
        d_rsp = { 'rsp': rsp, 'JWT': jwt }
        return d_rsp, 200
    