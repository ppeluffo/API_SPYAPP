#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3

from api_spyapp.utilidades import logger
from api_spyapp.bdatos.COMMS import api
from dependency_injector import containers, providers
import pandas as pd

def test_get_dataloggers():
    df = dbh.get_dataloggers()
    if isinstance(df, pd.DataFrame):
        print(f"Dataloggers shape: {df.shape}")
        print(f"{df.head()}")
    else:
        print(f"Dataloggers ERROR:")

def test_get_tx48hs():
    df = dbh.get_tx48hs()
    if isinstance(df, pd.DataFrame):
        print(f"Tx48hs shape: {df.shape}")
        print(f"{df.head()}")
    else:
        print(f"Tx48hs ERROR:")    
    
class Container(containers.DeclarativeContainer):

    logger = providers.Singleton(logger.Logger.log)
    database = providers.Singleton(api.DbCOMMS, logger=logger )

if __name__ == "__main__":

    container = Container()
    dbh = container.database()
    # Test get_dataloggers
    test_get_dataloggers()

     # Test get_tx48hs
    test_get_tx48hs()