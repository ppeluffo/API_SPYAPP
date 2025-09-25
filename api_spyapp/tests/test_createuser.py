#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3
"""
Genera varios requests al entrypoint de createuser para probar todos los casos
"""
import requests

URL = URL = "http://127.0.0.1:3000/api_spyapp/create_user"

def test_createuser(username="user", password="passwd"):
    payload = {"username":username, "password":password}
    r = requests.post(URL,json=payload)
    jdr = r.json()
    if jdr['rsp'] == "OK":
        print("test_login: Response OK")
        return True
    else:
        print("test_login: Response FAIL")
        return False

if __name__ == '__main__':

    tests = 0
    responses_valid = 0

    # USERNAME NOT VALID:
    tests += 1
    username = "pablo@spymovil"
    password = "Pexco599@"
    print("\nCreateuserTest_1 con username invalido....")
    if not test_createuser(username=username, password=password):
        print("Test OK")
        responses_valid += 1
    else:
        print("Test FAIL")

    # PASSWD INVALID 1:
    tests += 1
    username = "pablo@spymovil.com"
    password = "Pex1@"
    print("\nCreateuserTest_1 con passwd corta....")
    if not test_createuser(username=username, password=password):
        print("Test OK")
        responses_valid += 1
    else:
        print("Test FAIL")

    # PASSWD INVALID 2:
    tests += 1
    username = "pablo@spymovil.com"
    password = "pexco"
    print("\nCreateuserTest_2 con passwd sin mayusculas....")
    if not test_createuser(username=username, password=password):
        print("Test OK")
        responses_valid += 1
    else:
        print("Test FAIL")

    # PASSWD INVALID 3:
    tests += 1
    username = "pablo@spymovil.com"
    password = "PEXCO"
    print("\nCreateuserTest_3 con passwd sin minusculas....")
    if not test_createuser(username=username, password=password):
        print("Test OK")
        responses_valid += 1
    else:
        print("Test FAIL")

    # PASSWD INVALID 4:
    tests += 1
    username = "pablo@spymovil.com"
    password = "Pexco"
    print("\nCreateuserTest_4 con passwd sin digitos....")
    if not test_createuser(username=username, password=password):
        print("Test OK")
        responses_valid += 1
    else:
        print("Test FAIL")

    # PASSWD INVALID 5:
    tests += 1
    username = "pablo@spymovil.com"
    password = "Pexco5"
    print("\nCreateuserTest_5 con passwd sin caracteres especiales....")
    if not test_createuser(username=username, password=password):
        print("Test OK")
        responses_valid += 1
    else:
        print("Test FAIL")


    # USUARIO EXISTE
    # Asegurarse en la BD que exista
    tests += 1
    username = "testuser@spymovil.com"
    password = "Pexco1234@"
    print("\nCreateuserTest_6 usuario ya existe....")
    if not test_createuser(username=username, password=password):
        print("Test OK")
        responses_valid += 1
    else:
        print("Test FAIL")

    # USUARIO NO EXISTE: Lo crea
    # (Asegurarse que no exista y luego borrarlo !!!)
    tests += 1
    username = "newuser@spymovil.com"
    password = "Pexco1234@"
    print("\nCreateuserTest_7 usuario nuevo....")
    if test_createuser(username=username, password=password):
        print("Test OK")
        responses_valid += 1
    else:
        print("Test FAIL ( verigique que el usuario no exista el la BD y si existe borrelo !!)")

    #
    print("\nRESUMEN:")
    print(f"Cantidad de test realizados: {tests}")
    print(f"Respuestas correctas: {responses_valid}")