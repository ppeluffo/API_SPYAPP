#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3

from api_spyapp.utilidades import logger
from api_spyapp.repositorios.repo_trees import TreeRepository
from api_spyapp.bdatos.LOCAL import api as api_local
from api_spyapp.bdatos.GDA import api as api_gda
from api_spyapp.bdatos.COMMS import api as api_comms
from api_spyapp.repositorios.repo_trees import TreeRepository

from dependency_injector import containers, providers
import pandas as pd


def test_get_instalaciones():
    df = repo.get_instalaciones()
    if isinstance(df, pd.DataFrame):
        print(f"Instalaciones shape: {df.shape}")
        print(f"{df.head()}")
    else:
        print(f"Instalaciones ERROR:")
                
def test_get_dataloggers():
    df = repo.get_dataloggers()
    if isinstance(df, pd.DataFrame):
        print(f"Dataloggers shape: {df.shape}")
        print(f"{df.head()}")
    else:
        print(f"Dataloggers ERROR:")

def test_get_tx48hs():
    df = repo.get_tx48hs()
    if isinstance(df, pd.DataFrame):
        print(f"Tx48hs shape: {df.shape}")
        print(f"{df.head()}")
    else:
        print(f"Tx48hs ERROR:")    
    
def dependencies_fabric():
    loghandler = logger.Logger.log
    bdservice_comms = api_comms.DbCOMMS(loghandler)
    bdservice_gda= api_gda.DbGDA(loghandler)
    bdservice_local = api_local.DbLocal(loghandler)
    repo = TreeRepository(bd_local= bdservice_local, bd_gda = bdservice_gda, bd_comms=bdservice_comms)
    return repo

class Container(containers.DeclarativeContainer):

    loghandler = providers.Singleton(logger.Logger.log)
    bdservice_comms = providers.Singleton(api_comms.DbCOMMS, logger=loghandler )
    bdservice_gda = providers.Singleton(api_gda.DbGDA, logger=loghandler )
    bdservice_local = providers.Singleton(api_local.DbLocal, logger=loghandler )
    repository = providers.Factory(TreeRepository, bd_local= bdservice_local, bd_gda = bdservice_gda, bd_comms=bdservice_comms)


if __name__ == "__main__":

    #repo = dependencies_fabric()
    container = Container()
    repo = container.repository()

    # Test get_instalaciones
    test_get_instalaciones()

    # Test get_dataloggers
    test_get_dataloggers()

     # Test get_tx48hs
    #test_get_tx48hs()