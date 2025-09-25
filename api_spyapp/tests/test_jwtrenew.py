#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3
"""
Genera varios requests al entrypoint de jwtrenew para probar todos los casos
"""
import jwt
import requests
from datetime import datetime, timezone, timedelta

JWT_SECRET_KEY = "MySecretKey099"

URL = URL = "http://127.0.0.1:3000/api_spyapp/jwt_renew"

def test_jwtrenew(token_valid=True):
    """
    Debo generar un token valido
    """
    username = "test@token.com.uy"
    expiration_str = (datetime.now(timezone.utc) + timedelta(hours=1)).isoformat()
    token = jwt.encode (
            {'username': username, 'expiration': expiration_str },
            JWT_SECRET_KEY, 
            algorithm="HS256")

    print(f"TOKEN GENERADO={token}")
    if not token_valid:
        token += "_INVALID"

    print(f"TOKEN UTILIZADO={token}")
    payload = {"refresh_token":token}
    r = requests.post(URL,json=payload)
    jdr = r.json()
    if jdr['rsp'] == "OK":
        return True
    else:
        print("test_jwtrenew: Response FAIL")
        return False


if __name__ == '__main__':

    tests = 0
    responses_valid = 0

    # TOKEN VALID:
    tests += 1
    print("\nJwtrenewTest_1 con token valido....")
    if test_jwtrenew(token_valid=True):
        print("Test OK")
        responses_valid += 1
    else:
        print("Test FAIL")

    # TOKEN INVALID:
    tests += 1
    print("\nJwtrenewTest_2 con usuario invalido....")
    if not test_jwtrenew(token_valid=False):
        print("Test OK")
        responses_valid += 1
    else:
        print("Test FAIL")

    #
    print("\nRESUMEN:")
    print(f"Cantidad de test realizados: {tests}")
    print(f"Respuestas correctas: {responses_valid}")