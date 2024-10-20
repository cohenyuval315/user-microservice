import urllib
import urllib.parse
import json
import asyncio
from typing import Optional, Union, Dict, Any
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from sqlalchemy.engine import Engine
from sqlalchemy.exc import SQLAlchemyError
from lib.common.loggers import logger

class DatabaseEngine:
    """
    Manages the SQLAlchemy Engine, supporting both synchronous and asynchronous operations.
    """
    default_config = {
                'echo':True,
                'echo_pool':False,
                'enable_from_linting':True,
                # execution_options:pass,
                'hide_parameters':False,
                'insertmanyvalues_page_size':1000,
                # isolation_level="SERIALIZABLE", "REPEATABLE READ", "READ COMMITTED", "READ UNCOMMITTED" and "AUTOCOMMIT" based on backend.
                'json_deserializer':json.loads,
                'json_serializer':json.dumps,
                # label_length=
                # logging_name="sqlalchemy.engine"
                'max_identifier_length':None,
                # max_overflow=10,
                'module':None,
                # paramstyle=
                # pool=
                # poolclass=
                # pool_logging_name=
                # pool_pre_ping=
                'pool_size':5,
                'pool_recycle':1,
                'pool_reset_on_return':'rollback',
                # pool_timeout=30,
                # pool_use_lifo=False,
                'plugins':[],
                'query_cache_size':500,
                'connect_args':{},
                # convert_unicode=
                # creator=,   
    }    
    
    def __init__(self, database_url: str, **kwargs):
        self.database_url = database_url
        self.is_async = self._determine_async(database_url)
        self.config = self._get_config(kwargs)
        self.engine: Optional[Union[Engine, AsyncEngine]] = None
        self._initialized = False

    def _determine_async(self, url: str) -> bool:
        """
        Determines if the engine should be asynchronous based on the URL scheme.
        """
        async_schemes = ['postgresql+asyncpg', 'mysql+aiomysql', 'mssql+asyncpyodbc']
        return any(url.startswith(scheme) for scheme in async_schemes)

    def _get_config(self, kwargs: Dict[str, Any]) -> Dict[str, Any]:
        """
        Prepares the configuration dictionary for the engine creation.
        """
        _config = self.default_config.copy()
        _config.update(kwargs)
        return _config

    def initialize(self):
        """
        Initializes the SQLAlchemy engine based on the configuration.
        """
        if self._initialized:
            logger.warning("DatabaseEngine is already initialized.")
            return

        try:
            if self.is_async:
                self.engine = create_async_engine(self.database_url, **self.config)
                logger.info("Asynchronous SQLAlchemy engine created.")
            else:
                self.engine = create_engine(self.database_url, **self.config)
                logger.info("Synchronous SQLAlchemy engine created.")
            self._initialized = True
        except SQLAlchemyError as e:
            logger.error(f"Failed to create engine: {e}")
            raise

    def get_engine(self) -> Union[Engine, AsyncEngine]:
        """
        Returns the initialized engine.
        """
        if not self._initialized or self.engine is None:
            raise Exception("DatabaseEngine is not initialized. Call initialize() first.")
        return self.engine

    async def dispose_async(self):
        """
        Disposes of an asynchronous engine.
        """
        if self.is_async and isinstance(self.engine, AsyncEngine):
            await self.engine.dispose()
            logger.info("Asynchronous engine disposed.")

    def dispose_sync(self):
        """
        Disposes of a synchronous engine.
        """
        if not self.is_async and isinstance(self.engine, Engine):
            self.engine.dispose()
            logger.info("Synchronous engine disposed.")

    async def dispose(self):
        """
        Disposes of the engine based on its type.
        """
        if not self._initialized:
            logger.warning("Engine not initialized.")
            return

        if self.is_async:
            await self.dispose_async()
        else:
            self.dispose_sync()

    def is_async_engine(self) -> bool:
        """
        Returns whether the engine is asynchronous.
        """
        return self.is_async


    def delete_this_create_engine_string(
        self,
        dialect:str,
        driver:str,
        username:str,
        password:str,
        host:str,
        port:str,
        database:str,
    ) -> str:
        parsed_password = urllib.parse.quote_plus(password)
        return f"{dialect}+{driver}://{username}:{parsed_password}@{host}:{port}/{database}"
    

    def delete_this_get_engine_instance(sqlalchemy_database_url:str,is_async:bool) -> AsyncEngine:
        kwargs = {
                    'url':sqlalchemy_database_url,
                    'echo':True,
                    'echo_pool':False,
                    'enable_from_linting':True,
                    # execution_options:pass,
                    'hide_parameters':False,
                    'insertmanyvalues_page_size':1000,
                    # isolation_level="SERIALIZABLE", "REPEATABLE READ", "READ COMMITTED", "READ UNCOMMITTED" and "AUTOCOMMIT" based on backend.
                    'json_deserializer':json.loads,
                    'json_serializer':json.dumps,
                    # label_length=
                    # logging_name="sqlalchemy.engine"
                    'max_identifier_length':None,
                    # max_overflow=10,
                    'module':None,
                    # paramstyle=
                    # pool=
                    # poolclass=
                    # pool_logging_name=
                    # pool_pre_ping=
                    'pool_size':5,
                    'pool_recycle':1,
                    'pool_reset_on_return':'rollback',
                    # pool_timeout=30,
                    # pool_use_lifo=False,
                    'plugins':[],
                    'query_cache_size':500,
                    'connect_args':{},
                    # convert_unicode=
                    # creator=,   
        }
        if is_async:
            loop = asyncio.get_event_loop()
            engine  = loop.run_until_complete(
                create_async_engine(**kwargs)
            )
        else:
            engine = create_engine(**kwargs)   
            
        return engine