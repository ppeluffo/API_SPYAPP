#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3


class UsersRepo:
    """
    Repositorio que se encarga de ver si el usuario existe o no.
    Le pregunta al datasource bdLocal.
    """
    
    def __init__(self, datasource ):
        self.datasource = datasource
        pass
        
    def check_user(self, username = None, password = None):
        print(f"DEBUG:UsersRepo:check_user:IN: username={username},password={password}")
        return self.datasource.check_user(username=username, password=password)
        
    def user_exists(self, username = None):
        print(f"DEBUG:UsersRepo:user_exists:IN: username={username}")
        res = self.datasource.user_exists(username=username)
        return res
    
    def createuser(self, username=None, password=None):
        print(f"DEBUG:UsersRepo:createuser:IN: username={username},password={password}")
        res = self.datasource.createuser(username=username, password=password)
        return res
    
    def update_passcode(self, username=None, code=None):
        print(f"DEBUG:UsersRepo:update_passcode:IN: username={username},code={code}")
        res = self.datasource.update_passcode(username=username, code=code)
        return res
    
    def update_password(self, username=None, password=None, code=None):
        print(f"DEBUG:UsersRepo:update_password:IN: username={username},password={password}, code={code}")
        res = self.datasource.update_password(username=username, password=password, code=code)
        return res