#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3

from api_spyapp.bdatos.GDA.interfaces import DbGDAInterface
from api_spyapp.bdatos.GDA import base
import pandas as pd

class DbGDA(DbGDAInterface):

    def __init__(self, logger):
        """
        Uso inyeccion de dependencias en el constructor.
        """
        self.logger = logger

    def get_instalaciones(self):
        sql_query = """
                SELECT DISTINCT(spx_unidades.dlgid),
                spx_ubicacion.direccion,  
                spx_unidades.id AS unidades_id, 
                spx_instalacion.id AS instalacion_id, 
                spx_ubicacion.id AS ubicacion_id
                FROM spx_unidades
                INNER JOIN spx_instalacion ON spx_unidades.id = spx_instalacion.unidad_id
                INNER JOIN spx_ubicacion ON spx_instalacion.ubicacion_id = spx_ubicacion.id
                ORDER BY dlgid
                """
        try:
            df_instalaciones = pd.read_sql_query(sql_query, con=base.engine_gda)
            return df_instalaciones
        except Exception as e:
            self.logger( __name__, f"ERROR {e}")
            return None
        