#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3
"""
Esta api implementa entrypoints(resources) que se implementan en clases
individuales en Resources.
Cada uno de estos tiene un correspondiente Servicio
Luego, los servicios si requieren acceder a una base de datos u otro datasource
lo hacen a travéz de un Repositorio
Este Repositorio es el que decide de que datasource brinda la información

RESOURCES:
Implemento el entrypoint.
Leo los parámetros del request, los proceso enviandoselos al servicio correspondiente
y luego devuelvo la respuesta.

SERVICIOS:
Realiza el negocio.
Si necesita datos de una fuente, lo solicita a travéz del repositorio.

Todos deben devolver siempre un diccionario donde el primer campo es 'success' que es True/False

"""
# Paso 1: Importo los módulos necesarios
import logging
from config import settings

from resources import tests
from resources import login
from resources import createuser
from resources import jwtrenew
from resources import passwordcode
from resources import passwordchange
from resources import datoshistoricos
from resources import datosonlinedlglist

from container import Container

from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__)

    # Setup the Flask-JWT-Extended extension
    app.config["JWT_SECRET_KEY"] = settings.JWT_SECRET_KEY
    jwt = JWTManager(app)

    api = Api(app)

    container = Container()
    container.init_resources()
    container.wire(modules=[__name__])
    #container.init_database_local()

    api.add_resource( tests.TestNoParams, '/api_spyapp/testnoparams')
    api.add_resource( tests.TestWithParams, '/api_spyapp/testwithparams')
    api.add_resource( tests.TestTokensGenToken, '/api_spyapp/test_gentokens')
    api.add_resource( tests.TestTokensValidateToken, '/api_spyapp/test_validatetokens')

    api.add_resource( login.LoginResource, '/api_spyapp/login')
    api.add_resource( createuser.CreateUserResource, '/api_spyapp/create_user')
    api.add_resource( jwtrenew.JWTRenewResource, '/api_spyapp/jwt_renew') 
    api.add_resource( passwordcode.PasswordCodeResource, '/api_spyapp/gen_password_code')
    api.add_resource( passwordchange.PasswordChangeResource, '/api_spyapp/password_change')
    api.add_resource( datoshistoricos.DatosHistoricosResource, '/api_spyapp/datos_historicos')
    api.add_resource( datosonlinedlglist.DatosOnlineDlgListResource, '/api_spyapp/datos_online_dlglist')
#    api.add_resource( datosonline.DatosOnlineTreeResource, '/api_spyapp/datos_online_tree')

    # Lineas para que cuando corre desde gunicorn utilize el log handle de este
    # https://trstringer.com/logging-flask-gunicorn-the-manageable-way/

    return app

if __name__ != '__main__':
    # SOLO PARA TESTING !!!
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app = create_app()
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
    app.logger.info('Starting Spy APP api...')


# Lineas para cuando corre en modo independiente
if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=3000, debug=True)

