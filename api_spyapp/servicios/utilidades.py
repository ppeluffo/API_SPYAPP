#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3

import jwt
from datetime import datetime, timezone, timedelta
from config import settings
import re
import random
import pandas as pd

def df_to_json(df: pd.DataFrame, orient: str = "records") -> list[dict]:
    """
    Convierte un DataFrame a una lista de dicts JSON-serializable.
    Todas las columnas datetime se convierten a strings ISO 8601.
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("El argumento debe ser un DataFrame de pandas")

    # Convertir todas las columnas datetime ( hago un df.info() y veo que tipo de columnas tiene )
    for col in df.select_dtypes(include=["datetime64[ns]"]):
        df[col] = df[col].dt.strftime("%Y-%m-%d %H:%M:%S")

    return df.to_dict(orient=orient)

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
        print(f"DEBUG:token_is_valid: Token valid")
        return True
    
    print(f"DEBUG:token_is_valid: Token invalid")
    return False

def token_get_payload(token):
    """
    Dado un JWT, extrae el diccionario del payload y lo retorna
    """
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=["HS256"])
        print(f"DEBUG:token_get_payload: payload={payload}")
        return payload
    except Exception as e:
        print(f"ERROR:token_get_payload: token invalid, {e}")
        return None

def verify_username(username):
    """
    Verifica que sea una direccion de email.
    Debe tener un @ y un .
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, username) is None:
        print(f"DEBUG:verify_username: username not valid")
        return False
    else:
        print(f"DEBUG:verify_username: OK")
        return True

def verify_password(password):

    #if password1 != password2:
    #    print(f"ERROR: {password1} <> {password2}")
    #    return False

    if len(password) < settings.MIN_LENGTH_PASSWORD:    
        print(f"DEBUG:verify_password: length < min")
        return False
    
    if not re.search(r"[A-Z]", password):
        print(f"DEBUG:verify_password: password {password} no tiene mayusculas")
        return False
    
    if not re.search(r"[a-z]", password):
        print(f"DEBUG:verify_password: password {password} no tiene minusculas")
        return False
    
    if not re.search(r"\d", password):
        print(f"DEBUG:verify_password: password {password} no tiene digitos")
        return False

    if not re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", password):
        print(f"DEBUG:verify_password: password {password} no tiene char especiales")
        return False
    
    print(f"DEBUG:verify_password: OK")
    return True

def verify_code(repo, username=None, code=None):
    """
    Verifica que el código de cambio de contraseñas provisto sea el correcto
    con el que está en la BD y que sea válido.
    En la BD el code es un str pero aqui es un int.!!!
    """
    bd_code, bd_fecha_emision_code = repo.get_passwd_code(username)
    bd_code = int(bd_code)
    if (bd_code != code):
        print(f"DEBUG:verify_code: password bd_code != code")
        return False

    if ( datetime.now(timezone.utc) > bd_fecha_emision_code + timedelta(hours=1)):
        print(f"DEBUG:verify_code: now > bd_fecha + 1h")
        return False
    
    print(f"DEBUG:verify_code: OK")
    return True

def gen_passwdcode():
    """
    Genera un codigo de 6 dígitos aleatorios y lo guarda en la BD
    junto al timestamp en formato pickle: core.timestamp
    Envia un email al usuario con el código. 
    Si el usuario no existe, lo ingnoro.
    """
    code = random.randint(100000, 999999)
    #now = datetime.datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
    #print(f"DEBUG:gen_passwdcode code={code},dt={now}")
    print(f"DEBUG:gen_passwdcode code={code}")
    return code


