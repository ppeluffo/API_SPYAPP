#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3

import jwt
from datetime import datetime, timezone, timedelta
from api_spyapp.config import settings
import re

def gen_new_token(username, exp_hours):
    """
    Los datetime no son serializables JSON. Los convierto a string con isoformat()
    """
    expiration_str = (datetime.now(timezone.utc) + timedelta(hours=exp_hours)).isoformat()
    token = jwt.encode(
                {'username': username, 'expiration': expiration_str },
                settings.JWT_SECRET_KEY, 
                algorithm="HS256")
    return token

def token_is_valid(repo, token):
    """
    Para verificar que sea valido chequeamos que el usuario exista
    y que el token no haya expirado
    La fecha que trae el JWT es tipo str asi que la pasamos a datetime.
    """
    payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=["HS256"])
    username = payload['username']
    expiration = payload['expiration']
    dt_expiracion = datetime.fromisoformat(expiration)
        
    if repo.check_if_user_exists(username) and ( datetime.now(timezone.utc) < dt_expiracion ):
        return True
    return False

def token_get_payload(token):
    """
    Dado un JWT, extrae el diccionario del payload y lo retorna
    """
    payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=["HS256"])
    return payload

def verify_passwords(logger, password1, password2):

    if password1 != password2:
        logger(__name__, f"ERROR: {password1} <> {password2}")
        return False

    if len(password1) < settings.MIN_LENGTH_PASSWORD:    
        logger(__name__, f"ERROR: length < min")
        return False
    
    if not re.search(r"[A-Z]", password1):
        logger(__name__, f"ERROR: password {password1} no tiene mayusculas")
        return False
    
    if not re.search(r"[a-z]", password1):
        logger(__name__, f"ERROR: password {password1} no tiene minusculas")
        return False
    
    if not re.search(r"\d", password1):
        logger(__name__, f"ERROR: password {password1} no tiene digitos")
        return False

    if not re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", password1):
        logger(__name__, f"ERROR: password {password1} no tiene caracteres especiales")
        return False
    
    return True

def verify_code(repo, username=None, code=None):
    """
    Verifica que el código de cambio de contraseñas provisto sea el correcto
    con el que está en la BD y que sea válido.
    En la BD el code es un str pero aqui es un int.!!!
    """
    bd_code, bd_fecha_emision_code = repo.get_passwd_code(username)
    bd_code = int(bd_code)
    if (bd_code == code) and ( datetime.now(timezone.utc) < bd_fecha_emision_code + timedelta(hours=1)):
        return True
    return False




