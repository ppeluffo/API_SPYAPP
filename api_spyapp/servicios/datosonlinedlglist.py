#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3

import pandas as pd

from servicios.utilidades import df_to_json

class DatosOnlineDlgListService:
    """
    Servicio de datos historicos:
    Recibe un dlgid y pide al repositorio de datos, los datos historicos (48 hs)
    """
    def __init__(self, repositorio):
        self.datos_repo = repositorio

    def datosonlinedlglist(self,l_dlgid = None):
        """
        Solo pido los datos al repositorio. En caso de error devuelve None
        Si no hay datos la lista es vacia
        El repositorio devuelve una lista de rows de sqlalchemy
        """
        
        print(f"DEBUG: DatosHistoricos Services")
        l_rows = self.datos_repo.get_datosonlinedlglist(l_dlgid)
        if l_rows is None:
            return { 'success': False }
        else:
            """
            result es una lista de sqlalchemy row
            1. Convierto la lista de objetos a un pd.Dataframe
            2. El problema es que un dataframe no es serializable json o sea que asi no lo
               podemos enviar como respuesta.
               Usamos un helper para convertirlo a json
            """
            df = pd.DataFrame(l_rows)  
            df = df.drop(["id"], axis=1)
            jdf = df_to_json(df)
            # 
            return { 'success': True, 'jdf': jdf}
        
    
    