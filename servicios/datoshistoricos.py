#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3

import pandas as pd

from servicios.utilidades import df_to_json

class DatosHistoricosService:
    """
    Servicio de datos historicos:
    Recibe un dlgid y pide al repositorio de datos, los datos historicos (48 hs)
    """
    def __init__(self, repositorio):
        self.datos_repo = repositorio

    def datoshistoricos(self,dlgid = None):
        """
        Solo pido los datos al repositorio. En caso de error devuelve None
        Si no hay datos la lista es vacia
        El repositorio devuelve un pandas dataframe
        """
        
        print(f"DEBUG: DatosHistoricos Services")
        l_objects = self.datos_repo.get_datoshistoricos(dlgid)
        if l_objects is None:
            return { 'success': False }
        else:
            """
            results es una lista de objetos orm de la tabla historica
            1. Convierto la lista de objetos ORM a un pd.Dataframe
            2. Elimino esta columna que la agrega Sqlalchemy como atributo interno
            3. El problema es que un dataframe no es serializable json o sea que asi no lo
               podemos enviar como respuesta.
               Usamos un helper para convertirlo a json
            """
            df = pd.DataFrame([r.__dict__ for r in l_objects])  
            df = df.drop(["_sa_instance_state","id","fechasys","equipo"], axis=1)
            jdf = df_to_json(df)
            # 
            return { 'success': True, 'jdf': jdf}
        
    
    