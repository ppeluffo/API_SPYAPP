#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3

from servicios.utilidades import gen_passwdcode

class PasswordCodeService:
    """
    Genera un nuevo codigo que lo deja almacenado en la BD para cuando
    el usuario quiera cambiar la contraseña.

    En principio NO controlo cuantas veces solicita el cambio. Podriamos en un
    futuro agregar que no haga mas de 5 solicitudes por día.

    """

    def __init__(self, repositorio):
        self.users_repo = repositorio

    def passwordcode(self, username=None):

        print(f"DEBUG: PasswordCodeService")

        # Genero un nuevo código y fecha de emisión.
        new_code = gen_passwdcode()
        print(f"DEBUG: PasswordCodeService: code={new_code}")

        # Si el usuario existe, actualizo el registo con el codigo y mando el mail
        if self.users_repo.user_exists(username):
            if self.users_repo.update_passcode(username=username, code=new_code):
                # SEND MAIL
                # ......
                return { 'success': True }

        return { 'success': False }