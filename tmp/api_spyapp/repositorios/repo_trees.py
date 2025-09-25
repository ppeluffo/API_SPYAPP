#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3

from api_spyapp.repositorios.interfaces_repo_trees import TreeRepoInterface
from api_spyapp.bdatos.LOCAL.interfaces import DbLocalInterface
from api_spyapp.bdatos.GDA.interfaces import DbGDAInterface
from api_spyapp.bdatos.COMMS.interfaces import DbCOMMSInterface

class TreeRepository(TreeRepoInterface):

    def __init__(self, bd_local: DbLocalInterface, bd_gda:DbGDAInterface, bd_comms:DbCOMMSInterface):
        """
        Uso inyeccion de dependencias en el constructor.
        """
        self.bd_local = bd_local
        self.bd_gda = bd_gda
        self.bd_comms = bd_comms

    def get_instalaciones(self):
        return self.bd_gda.get_instalaciones()

    def get_dataloggers(self):
        return self.bd_comms.get_dataloggers()

    def get_tx48hs(self):
        return self.bd_comms.get_tx48hs()
    