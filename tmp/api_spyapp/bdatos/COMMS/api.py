#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3

from api_spyapp.bdatos.COMMS.interfaces import DbCOMMSInterface
from api_spyapp.bdatos.COMMS import base
import pandas as pd


class DbCOMMS(DbCOMMSInterface):

    def __init__(self, logger):
        """
        Uso inyeccion de dependencias en el constructor.
        """
        self.logger = logger

    def get_dataloggers(self):
        sql_query = "SELECT unit_id FROM configuraciones WHERE jconfig ->> 'BASE' LIKE '%%TDIAL%%'"
        try:
            df_dataloggers = pd.read_sql_query(sql_query, con=base.engine_comms)
            return df_dataloggers
        except Exception as e:
            self.logger( __name__, f"ERROR {e}")
            return None
        pass

    def get_tx48hs(self):
        sql_query = """
                SELECT DISTINCT(equipo) FROM public.historica WHERE fechasys > NOW() - INTERVAL '48 hours' ORDER BY equipo
                """
        try:
            x48hs = pd.read_sql_query(sql_query, con=base.engine_comms)
            return x48hs
        except Exception as e:
            self.logger( __name__, f"ERROR {e}")
            return None
        pass