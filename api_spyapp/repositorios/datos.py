#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3


class DatosRepo:
    """
    Repositorio que se encarga de recuperar los datos.
    Le pregunta al datasource Server8(COMMS)
    """
    
    def __init__(self, datasource ):
        self.datasource = datasource
        pass
        
    def get_datoshistoricos(self, dlgid=None):
        print(f"DEBUG:DatosRepo:datoshistoricos:IN: dlgid={dlgid}")
        return self.datasource.get_datoshistoricos(dlgid=dlgid)
        
    def get_datosonlinedlglist(self, l_dlgid=None):
        print(f"DEBUG:DatosRepo:datosonlinedlglist:IN: l_dlgid={l_dlgid}")
        return self.datasource.get_datosonlinedlglist(l_dlgid = l_dlgid)