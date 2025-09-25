#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3

import datetime
from flask_restful import Resource, reqparse

class TestNoParams(Resource):
    '''
    Clase para probar nuevos equipos ( SPQ)
    '''
    def __init__(self):
        pass

    def get(self):
        now=datetime.datetime.now().strftime('%y%m%d%H%M%S')
        response = f'<html>GetTEST: CLOCK={now};</html>'
        return response, 200

    def post(self):
        now=datetime.datetime.now().strftime('%y%m%d%H%M%S')
        response = f'<html>PostTEST: CLOCK={now};</html>'
        d_rsp = {'status':'OK', 'name':'Post Test','data':f"localtime={now}"}
        #return response, 200
        return d_rsp, 200
    
class TestWithParams(Resource):
    '''
    Clase para probar nuevos equipos ( SPQ)
    '''
    def __init__(self):
        pass

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('USER', type=str ,location='args', required=True)
        args = parser.parse_args()
        user = args.get('USER',None)

        now=datetime.datetime.now().strftime('%y%m%d%H%M%S')
        response = f'<html>GetTEST: CLOCK={now};USER={user}</html>'
        return response, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('USER',type=str,location='json',required=True)
        args = parser.parse_args()
        user = args.get('USER',None)

        now=datetime.datetime.now().strftime('%y%m%d%H%M%S')
        response = f'<html>PostTEST: CLOCK={now};</html>'
        d_rsp = {'status':'OK', 'name':'Post Test','data':f"localtime={now}",'user':user}
        #return response, 200
        return d_rsp, 200
    



