#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3

from api_spyapp.utilidades import logger
from api_spyapp.bdatos.LOCAL import api
from api_spyapp.repository import autentificacion
from api_spyapp.servicios import autentificacion as aut_service
from api_spyapp.servicios import notificaciones

from datetime import datetime, timezone, timedelta

def test_autenticar_user(username, password):

    res = servicehandler.autentificar(username=username, password=password)
    if res:
        jwt,rjwt = res
        print(f"autentificar:: El usuario {username} con password {password} esta autenticado")
        print(f"JWT={jwt}")
        print(f"RJWT={rjwt}")
        return jwt,rjwt

    else:
        print(f"autentificar:: El usuario {username} con password {password} NO esta autenticado")

def test_renew_tokens(rjwt=None):
    res = servicehandler.renew_tokens(refresh_token=rjwt)
    if res:
        jwt,rjwt = res
        print(f"renew_tokens:: OK")
        print(f"JWT={jwt}")
        print(f"RJWT={rjwt}")
        return jwt,rjwt

    else:
        print(f"renew_tokens:: FAIL")

def test_request_change_password_code(username=None):
    code = servicehandler.request_change_password_code(username)
    print(f"test request_change_password_code OK: code={code}")
    return code

def test_passwords_change(username=None, password1=None, password2=None, code=None):
    res = servicehandler.password_change(username, password1, password2, code)
    if res:
        print(f"password_change OK")
    else:
        print(f"password change FAIL")


if __name__ == "__main__":

    loghandler = logger.Logger.log
    bdhandler = api.DbLocal(loghandler)
    repohandler = autentificacion.AutentificacionRepo(bdhandler)
    notifierhandler = notificaciones.Notificaciones(print)
    servicehandler = aut_service.AutentificacionService(repohandler, loghandler, notifierhandler )

    # Test autentificar_user
    res = test_autenticar_user(username="ppeluffo2@spymovil.com",password="000001")
    if res:
        rjwt = res[1]
        renew_tokens = True
    else:
        renew_tokens = False
        print("No se pueden renovar tokens.")

    # Test renew_tokens
    if renew_tokens:
        test_renew_tokens(rjwt)

    # Test request password change code
    code = test_request_change_password_code("ppeluffo2@spymovil.com")

    # Test reauest password change
    test_passwords_change(username="ppeluffo2@spymovil.com", password1="Password1_", password2="Password1_", code=code)

