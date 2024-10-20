from sqlalchemy import create_engine,MetaData
import os
from sqlalchemy.engine import Engine
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy import pool
import json
from .base import Base
# from lib.shared.performance.profiler import Profiler
from typing import Optional,Union,Dict,Any
from .session_factory import DatabaseSessionFactory
from .engine import DatabaseEngine
from lib.common.loggers import logger



# IS_ASYNC = False if "sqlite" in SQLALCHEMY_DATABASE_URL else True
# engine = get_engine(sqlalchemy_database_url=SQLALCHEMY_DATABASE_URL,is_async=IS_ASYNC)

class Database:
    is_async:bool=False
    _db_engine: Optional[DatabaseEngine] = None
    _session_factory: Optional[DatabaseSessionFactory] = None
    base = Base
    metadata:Optional[MetaData] = None
    registry:Optional[Any] = None

    @classmethod
    def initialize(cls, sqlalchemy_database_url: str, **kwargs):
        """
        Initializes the DatabaseEngine and DatabaseSessionFactory.
        """
        if cls._db_engine is not None:
            logger.warning("Database is already initialized.")
            return
        cls._db_engine = DatabaseEngine(sqlalchemy_database_url, **kwargs)
        cls._db_engine.initialize()
        engine = cls._db_engine.get_engine()
        cls.is_async = cls._db_engine.is_async_engine()
        cls._session_factory = DatabaseSessionFactory(engine, cls.is_async)
        cls.registry = Base.registry
        cls.metadata = Base.metadata
        logger.info("Database initialized with session factory.")

    @classmethod
    def get_engine(cls) -> Union[Engine, AsyncEngine]:
        """
        Retrieves the initialized engine.
        """
        if cls._db_engine is None or not cls._db_engine._initialized:
            raise Exception("Database is not initialized. Call initialize() first.")
        return cls._db_engine.get_engine()

    @classmethod
    def get_session_factory(cls) -> DatabaseSessionFactory:
        """
        Retrieves the session factory.
        """
        if cls._session_factory is None:
            raise Exception("Session factory is not initialized.")
        return cls._session_factory
    
    @classmethod
    async def dispose(cls):
        """
        Disposes of the DatabaseEngine and cleans up resources.
        """
        if cls._db_engine:
            await cls._db_engine.dispose()
            cls._db_engine = None
            cls._session_factory = None
            logger.info("Database disposed.")
                    
    @classmethod
    async def drop_all(cls):
        if cls._db_engine:
            if cls.is_async:
                async with cls._db_engine.get_engine().begin() as conn:
                    await conn.run_sync(cls.metadata.drop_all)
            else:
                cls.metadata.drop_all(bind=cls._db_engine.get_engine(),checkfirst=True)
                    
                    
    @classmethod
    async def create_all(cls):
        if cls._db_engine:
            if cls.is_async:
                async with cls._db_engine.get_engine().begin() as conn:
                    await conn.run_sync(cls.metadata.create_all)
            else:
                cls.metadata.create_all(bind=cls._db_engine.get_engine(),checkfirst=True)
                    
                
                
# def setup_database():
#     if engine.dialect.name == "sqlite":
#         engine.pool = pool.StaticPool(creator=engine.pool._creator)
    