#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3
"""
Genera varios requests al entrypoint de login para probar todos los casos
"""
import requests

URL = URL = "http://127.0.0.1:3000/api_spyapp/login"

def test_login(username="user", password="passwd"):
    payload = {"username":username, "password":password}
    r = requests.post(URL,json=payload)
    jdr = r.json()
    if jdr['rsp'] == "OK":
        print("test_login: Response OK")
        print(f"JWT={jdr['JWT']}")
        print(f"RJWT={jdr['RJWT']}")
        return True
    else:
        print("test_login: Response FAIL")
        return False


if __name__ == '__main__':

    tests = 0
    responses_valid = 0

    # USER VALID:
    tests += 1
    username = "pablo@spymovil.com"
    password = "Pexco599@"
    print("\nLoginTest_1 con usuario valido....")
    if test_login(username=username, password=password):
        print("Test OK")
        responses_valid += 1
    else:
        print("Test FAIL")

    # USER INVALID:
    tests += 1
    username = "pablo@spymovil.com1"
    password = "Pexco599@"
    print("\nLoginTest_2 con usuario invalido....")
    if not test_login(username=username, password=password):
        print("Test OK")
        responses_valid += 1
    else:
        print("Test FAIL")

    # PASSWD VALID:
    tests += 1
    username = "pablo@spymovil.com"
    password = "Pexco599@1"
    print("\nLoginTest_3 con passwd invalido....")
    if not test_login(username=username, password=password):
        print("Test OK")
        responses_valid += 1
    else:
        print("Test FAIL")

    #
    print("\nRESUMEN:")
    print(f"Cantidad de test realizados: {tests}")
    print(f"Respuestas correctas: {responses_valid}")