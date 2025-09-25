#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3

from api_spyapp.utilidades import logger
from api_spyapp.bdatos.GDA import api
from dependency_injector import containers, providers
import pandas as pd

def test_get_instalaciones():
    df = dbh.get_instalaciones()
    if isinstance(df, pd.DataFrame):
        print(f"Instalaciones shape: {df.shape}")
        print(f"{df.head()}")
    else:
        print(f"Instalaciones ERROR:")

def dependencies_fabric():
    loghandler = logger.Logger.log
    bdservice = api.DbGDA(loghandler)
    return bdservice

class Container(containers.DeclarativeContainer):

    logger = providers.Singleton(logger.Logger.log)
    database = providers.Singleton( api.DbGDA, logger=logger )


if __name__ == "__main__":


    #dbh = dependencies_fabric()
    container = Container()
    dbh = container.database()

    # Test get_instalaciones
    test_get_instalaciones()
    