#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3
"""
Logea los mensajes recibidos
"""

import datetime

def f_logger(fname=None, msg=None, level="INFO"):

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{now}: {level} {fname}:{msg}")

