#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3
"""
Probamos los entrypoints que requieren autenticacion con jwt
Primero hago un login para obtener el jwt y el rjwt.
Luego accedo a datoshistoricos con el jwt.
Luego accedo al jwtrefresh con el rjwt y renuevo los 2 tokens
Accedo finalmente a datoshistoricos con el nuevo jwt.
"""
import requests

BASE_URL = "http://127.0.0.1:3000/api_spyapp/"

class Tests:

    def __init__(self):
        self.jwt = None
        self.rjwt = None
        self.test_count = 0
        self.responses_valid = 0

    def test_login(self, username="user", password="passwd"):

        print("\nLogin Test...")
        self.test_count += 1
        payload = {"username":username, "password":password}
        r = requests.post(BASE_URL + "login",json=payload)
        jdr = r.json()
        if jdr['rsp'] == "OK":
            self.jwt = jdr['JWT']
            self.rjwt = jdr['RJWT']
            print("test_login: Response OK")
            print(f"JWT={self.jwt}")
            print(f"RJWT={self.rjwt}")
            self.responses_valid += 1
            return True
        else:
            print("test_login: Response FAIL")
            return False

    def test_datoshistoricos(self, dlgid=None):

        print("\nDatosHistoricos Test...")
        self.test_count += 1

        # Construct the headers dictionary
        headers = {
            "Authorization": f"Bearer {self.jwt}",
            "Content-Type": "application/json"  # Optional: if you are sending JSON data
        }
        payload = { "dlgid": dlgid }
        r = requests.post(BASE_URL + "datos_historicos",json=payload,  headers=headers)
        jdr = r.json()
        if jdr['rsp'] == "OK":
            print("test_DatosHistoricos: Response OK")
            data = jdr['datos']
            print(data)
            self.responses_valid += 1
            return True
        else:
            print("test_DatosHistoricos: Response FAIL")
            return False

    def test_renewjwt(self):
        """
        Envio el rjwt y solicito uno nuevo
        """
        print("\nRenewjwt Test...")
        self.test_count += 1

        # Construct the headers dictionary
        headers = {
            "Authorization": f"Bearer {self.rjwt}",
            "Content-Type": "application/json"  # Optional: if you are sending JSON data
        }
        r = requests.post(BASE_URL + "jwt_renew",headers=headers)
        jdr = r.json()
        if jdr['rsp'] == "OK":
            print("test_Renewjwt: Response OK")
            self.jwt = jdr['JWT']
            self.rjwt = jdr['RJWT']
            print(f"JWT={self.jwt}")
            print(f"RJWT={self.rjwt}")
            self.responses_valid += 1
            return True
        else:
            print("test_Renewjwt: Response FAIL")
            return False

if __name__ == '__main__':

    tests = Tests()
    username = "pablo@spymovil.com"
    password = "Pexco599@"
    tests.test_login(username=username, password=password)
    #
    tests.test_datoshistoricos(dlgid="UYRIV114")
    #
    tests.test_renewjwt()
    #
    #
    print("\nRESUMEN:")
    print(f"Cantidad de test realizados: {tests.test_count}")
    print(f"Respuestas correctas: {tests.responses_valid}")

