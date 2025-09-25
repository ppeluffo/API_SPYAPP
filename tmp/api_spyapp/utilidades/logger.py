#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3

from api_spyapp.utilidades.interfaces import LoggerInterface

class Logger(LoggerInterface):

    def log(source_function=None, message=None):
        print(f"ERROR: {source_function}: {message}")