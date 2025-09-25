#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3
"""
REFS:
Autentificacion: https://www.geeksforgeeks.org/python/using-jwt-for-user-authentication-in-flask/

"""
from .models import DatosHistoricos
from datetime import datetime, timezone, timedelta
from sqlalchemy import distinct

class Dbcomms8:

    def __init__(self, session_factory):
        """
        Uso inyeccion de dependencias en el constructor.
        """
        self.session_factory = session_factory
        print(f"DEBUG:Dbcomms8:__init__")

    def get_datoshistoricos(self, dlgid=None):
        """
        """
        print(f"DEBUG:Dbcomms8:get_datoshistoricos:IN: dlgid={dlgid}")

        data_from = (datetime.now(timezone.utc) - timedelta(hours=48))
        try:
            # This gives you a list of ORM objects (DatosHistoricos instances), not rows.
            with self.session_factory() as session:
                result = session.query(DatosHistoricos).filter(DatosHistoricos.equipo == dlgid, DatosHistoricos.fechadata > '2025-09-24').all()
                return result
        except Exception as e:
            print(f"ERROR:Dbcomms8: Error={e}")
            return None
        
        return result

    def get_datosonlinedlglist(self, l_dlgid=None):
        """
        La consulta SQL si la hacemos en la tabla historica sería:
        SELECT DISTINCT ON (equipo, tag) 
            id, fechadata, equipo, tag, valor
            FROM public.historica
            WHERE equipo IN ('UYTAC051', 'UYTAC049', 'UYTAC047', 'UYSJO104')
            ORDER BY equipo, tag, fechadata DESC;

        El problema es que demora 2 minutos.
        Una opcion es tener una tabla online que la mantengamos acotada.
        
        La base es POSTGRES por lo tanto vamos a usar funcionalidades de sqlalchemy que
        andan solo en Postgres !!!!

        result es una lista de sqlalchemy row
        """
        try:
            # This gives you a list of ORM objects (DatosHistoricos instances), not rows.
            with self.session_factory() as session:
                query = ( session.query( DatosHistoricos.id, 
                                        DatosHistoricos.fechadata,
                                        DatosHistoricos.equipo,
                                        DatosHistoricos.tag,
                                        DatosHistoricos.valor 
                                        )
                                        .filter(DatosHistoricos.equipo.in_(l_dlgid))
                                        .distinct(DatosHistoricos.equipo, DatosHistoricos.tag)
                                        .order_by(DatosHistoricos.equipo, 
                                                  DatosHistoricos.tag, 
                                                  DatosHistoricos.fechadata.desc()
                                                )
                        )
                
                result = query.all()
                return result
        except Exception as e:
            print(f"ERROR:Dbcomms8: Error={e}")
            return None

    
