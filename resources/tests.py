#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3

import datetime
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, get_jwt
from datetime import datetime, timezone, timedelta

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
    
class TestTokensGenToken(Resource):
    """
    Genero un token con campos adicionales usando la api de flask-jwt-extended
    """
    def __init__(self):
        pass

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username',type=str,location='json',required=True)
        args = parser.parse_args()

        username = args.get('username',None)
        expiration_str = (datetime.now(timezone.utc) + timedelta(hours=1)).isoformat()
        additional_claims = {"expiration": expiration_str}

        #access_token = create_access_token(identity=username) 
        access_token = create_access_token(username, additional_claims=additional_claims)

        return {'access_token': access_token }, 200

class TestTokensValidateToken(Resource):
    """
    Recupero del un token los datos usando la api flask-jwt-extended
    """
    def __init__(self):
        pass

    @jwt_required()
    def post(self):
        #parser = reqparse.RequestParser()
        #parser.add_argument('access_token',type=str,location='json',required=True)
        #args = parser.parse_args()

        #access_token = args.get('access_token',None)
        # Esta funcion requiere que use el decorador !!
        current_user = get_jwt_identity()
        claims = get_jwt()

        print(f"current_user={current_user}")
        #print(f"claim_user:{claims['username']}")
        print(f"claim_expdate: {claims.get('expiration','ERROR')}")

        return {'status': 'OK' }, 200

