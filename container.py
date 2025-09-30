#!/home/pablo/Spymovil/python/proyectos/API_SPYAPP/.venv/bin/python3

from dependency_injector import containers, providers
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from utils.logger import f_logger

from repositorios.users import UsersRepo
from repositorios.datos import DatosRepo

from servicios.login import LoginService
from servicios.createuser import CreateUserService
from servicios.jwtrenew import JwtRenewService
from servicios.passwordcode import PasswordCodeService
from servicios.passwordchange import PasswordChangeService
from servicios.datoshistoricos import DatosHistoricosService
from servicios.datosonlinedlglist import DatosOnlineDlgListService

from config import settings
from datasources.bdlocal.models import Base_local
from datasources.bdlocal.bdapi import DbLocal
from datasources.comms8.models import Base_comms8
from datasources.comms8.bdapi import Dbcomms8

class Container(containers.DeclarativeContainer):
    
    wiring_config = containers.WiringConfiguration(
        modules=["resources.login", 
                 "resources.createuser", 
                 "resources.jwtrenew",
                 "resources.passwordcode",
                 "resources.passwordchange", 
                 "resources.datoshistoricos",
                 "resources.datosonlinedlglist"
                 ]
    )

    config = providers.Configuration()

    # Engine y session factory BDLOCAL
    engine_local = providers.Singleton(
        create_engine,
        url=settings.URL_LOCAL, 
        echo=False, 
        isolation_level="AUTOCOMMIT", 
        connect_args={'connect_timeout': 5}
    )

    session_factory_bdlocal = providers.Singleton(
        sessionmaker,
        bind = engine_local
    )
    
    # Engine y session factory BDCOMMS8
    engine_comms8 = providers.Singleton(
        create_engine,
        url=settings.URL_COMMS8, 
        echo=True, 
        isolation_level="AUTOCOMMIT", 
        connect_args={'connect_timeout': 5}
    )

    session_factory_comms8 = providers.Singleton(
        sessionmaker,
        bind = engine_comms8
    )
    
    logger = providers.Singleton(f_logger)

    # Repositorios y servicios
    login_datasource = providers.Factory(DbLocal, session_factory = session_factory_bdlocal)
    datos_datasource = providers.Factory(Dbcomms8, session_factory = session_factory_comms8)

    users_repo = providers.Factory(UsersRepo, datasource = login_datasource)
    datos_repo = providers.Factory(DatosRepo, datasource = datos_datasource)

    login_service = providers.Factory(LoginService, repositorio = users_repo)
    createuser_service = providers.Factory(CreateUserService, repositorio = users_repo)
    jwtrenew_service = providers.Factory(JwtRenewService, repositorio = users_repo)
    passwordcode_service = providers.Factory(PasswordCodeService, repositorio = users_repo)
    passwordchange_service = providers.Factory(PasswordChangeService, repositorio = users_repo)

    datoshistoricos_service = providers.Factory(DatosHistoricosService, repositorio = datos_repo)
    datosonlinedlglist_service = providers.Factory(DatosOnlineDlgListService, repositorio = datos_repo)

    # Crear las tablas si no existen
    def init_database_local(self):
        Base_local.metadata.create_all(self.engine_local())

    def init_database_comms8(self):
        Base_comms8.metadata.create_all(self.engine_comms8())