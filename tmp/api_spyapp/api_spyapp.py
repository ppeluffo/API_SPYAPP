#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3

# Paso 1: Importo los módulos necesarios
import logging

from api_spyapp.resources import tests

from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
# Paso 2: Inicializo la API y app

app = Flask(__name__)
api = Api(app)

# Paso 3: Defino las clases que implementan los recursos


# Paso 4: Asocio los Recursos con los URL
#api.add_resource( CreateUser, '/spyapi/auten/create_user', resource_class_kwargs={ 'app': app })
#api.add_resource( Login, '/spyapi/auten/login', resource_class_kwargs={ 'app': app })
#api.add_resource( JwtRenew, '/spyapi/auten/jwt_renew')
#api.add_resource( GenPasswordCode, '/spyapi/auten/gen_password_code')
api.add_resource( tests.TestNoParams, '/api_spyapp/testnoparams')
api.add_resource( tests.TestWithParams, '/api_spyapp/testwithparams')

# Lineas para que cuando corre desde gunicorn utilize el log handle de este
# https://trstringer.com/logging-flask-gunicorn-the-manageable-way/

if __name__ != '__main__':
    # SOLO PARA TESTING !!!
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
    app.logger.info('Starting Spy APP api...')


# Lineas para cuando corre en modo independiente
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)

