#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3
"""
Genera varios requests al entrypoint de password_change para probar todos los casos
"""
import requests

URL = URL = "http://127.0.0.1:3000/api_spyapp/password_change"

def test_password_change(username=None, password1=None, password2=None, passwd_code=None):
    payload = {"username":username, 
               "password1":password1,
               "password2":password2,
               "passwd_code":passwd_code}
    r = requests.post(URL,json=payload)
    jdr = r.json()
    if jdr['rsp'] == "OK":
        print("test_password_change: Response OK")
        return True
    else:
        print("test_password_change: Response FAIL")
        return False


if __name__ == '__main__':

    tests = 0
    responses_valid = 0

    # USER INVALID:
    tests += 1
    username = "pablo@spymovil.com.123"
    password1 = "Pexco123$"
    password2 = "Pexco123$"
    passwd_code = "123456"
    print("\nPasswordChangeTest_1 con usuario invalido....")
    if not test_password_change(username, password1, password2, passwd_code):
        print("Test OK")
        responses_valid += 1
    else:
        print("Test FAIL")

    # PASSWD DIFERENTES:
    tests += 1
    username = "pablo@spymovil.com"
    password1 = "Pexco123$"
    password2 = "Pexco123"
    passwd_code = "123456"
    print("\nPasswordChangeTest_2 con passwds diferentes....")
    if not test_password_change(username, password1, password2, passwd_code):
        print("Test OK")
        responses_valid += 1
    else:
        print("Test FAIL")
    #

    # PASSWD NO VALIDAS:
    tests += 1
    username = "pablo@spymovil.com"
    password1 = "Pexco123"
    password2 = "Pexco123"
    passwd_code = "123456"
    print("\nPasswordChangeTest_3 con passwds no validas....")
    if not test_password_change(username, password1, password2, passwd_code):
        print("Test OK")
        responses_valid += 1
    else:
        print("Test FAIL")
    #

    # DATOS CORRECTOS:
    # Solicitar primero un passwd code correcto !!!
    tests += 1
    username = "pablo@spymovil.com"
    password1 = "Pexco123@"
    password2 = "Pexco123@"
    passwd_code = "123456"
    print("\nPasswordChangeTest_4 con datos correctos. Solicitar un passwd code correcto !!!!....")
    if test_password_change(username, password1, password2, passwd_code):
        print("Test OK")
        responses_valid += 1
    else:
        print("Test FAIL")
    #

    print("\nRESUMEN:")
    print(f"Cantidad de test realizados: {tests}")
    print(f"Respuestas correctas: {responses_valid}")