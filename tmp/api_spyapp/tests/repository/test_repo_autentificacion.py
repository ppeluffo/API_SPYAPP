#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3

from api_spyapp.utilidades import logger
from api_spyapp.bdatos.LOCAL import api
from api_spyapp.repositorios import repo_autentificacion
from dependency_injector import containers, providers
from datetime import datetime, timezone, timedelta

def test_autenticar_user(username, password):
    res = repohandler.autentificar(username=username, password=password)
    if res:
        print(f"autentificar:: El usuario {username} con password {password} esta en la BD")
    else:
        print(f"autentificar:: El usuario {username} con password {password} NO esta en la BD")

def test_check_user_exists(username):
    res =  repohandler.check_if_user_exists(username=username)
    if res:
        print(f"check_if_user_exists:: El usuario {username} ya existe en la BD.")
    else:
        print(f"check_if_user_exists:: El usuario {username} NO existe en la BD.")

def test_update_password_code(username=None, code=None, fecha_emision_code=None):
    repohandler.update_password_code(username=username, code=code, fecha_emision_code=fecha_emision_code)
    print(f"update_password_code")

def test_get_passwd_code(username=None):
    code, fecha_expiracion = repohandler.get_passwd_code(username=username)
    print(f"get_passwd_code: El usuario {username} tiene code={code}, expiracion={fecha_expiracion}")

def test_update_password(username=None, password=None):
    res =  repohandler.update_password(username=username, password=password)
    if res:
        print(f"update_password:: Result OK")
    else:
        print(f"update_password:: Result ERR.")

def dependencies_fabric():
    loghandler = logger.Logger.log
    bdservice = api.DbLocal(loghandler)
    reposervice = repo_autentificacion.AutentificacionRepo(bdservice)
    return reposervice

class Container(containers.DeclarativeContainer):

    logger = providers.Singleton(logger.Logger.log)
    database = providers.Singleton(api.DbLocal, logger=logger )
    repository = providers.Factory(repo_autentificacion.AutentificacionRepo, api_db=database)

if __name__ == "__main__":

    #repohandler = dependencies_fabric()
    container = Container()
    repohandler = container.repository()

    # Test autentificar_user
    test_update_password(username="ppeluffo2@spymovil.com",password="PABLO123")
    test_autenticar_user(username="ppeluffo2@spymovil.com", password="PABLO123")
    test_autenticar_user(username="ppeluffoX@spymovil.com", password="PABLO123")
    test_autenticar_user(username="ppeluffo2@spymovil.com", password="PABLO123X")

    # Check user exists
    test_check_user_exists(username="ppeluffo2@spymovil.com")
    test_check_user_exists(username="ppeluffoX@spymovil.com")

    # Update password code
    test_update_password_code(username="ppeluffo2@spymovil.com", code="123456", fecha_emision_code=datetime.now(timezone.utc) + timedelta(hours=2))

    # Get_passwd_code
    test_get_passwd_code(username="ppeluffo2@spymovil.com")

    # Update_password
    test_update_password(username="ppeluffo2@spymovil.com",password="000001")
    test_autenticar_user(username="ppeluffo2@spymovil.com", password="PABLO123X")
    



