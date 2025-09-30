#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3
"""
Genera varios requests al entrypoint de password_code para probar todos los casos
"""
import requests

URL = URL = "http://127.0.0.1:3000/api_spyapp/gen_password_code"

def test_gen_password_code(username=None):
    payload = {"username":username}
    r = requests.post(URL,json=payload)
    jdr = r.json()
    if jdr['rsp'] == "OK":
        print("test_password_code: Response OK")
        return True
    else:
        print("test_password_code: Response FAIL")
        return False


if __name__ == '__main__':

    tests = 0
    responses_valid = 0

    # USER VALID:
    tests += 1
    username = "pablo@spymovil.com"
    print("\nPasswordCodeTest_1 con usuario valido....")
    if test_gen_password_code(username=username):
        print("Test OK")
        responses_valid += 1
    else:
        print("Test FAIL")

    # USER INVALID:
    tests += 1
    username = "pablo@spymovil.com23"
    print("\nPasswordCodeTest_2 con usuario invalido....")
    if test_gen_password_code(username=username):
        print("Test OK")
        responses_valid += 1
    else:
        print("Test FAIL")
    #
    print("\nRESUMEN:")
    print(f"Cantidad de test realizados: {tests}")
    print(f"Respuestas correctas: {responses_valid}")