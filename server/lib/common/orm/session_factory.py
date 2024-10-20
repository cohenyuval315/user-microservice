from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from sqlalchemy.engine import Engine
from sqlalchemy.ext.asyncio import AsyncEngine
from typing import Union,Any,Dict
import asyncio

"""
The Session is a mutable, stateful object that represents a single database transaction.
An instance of Session therefore cannot be shared among concurrent threads or asyncio tasks without careful synchronization

The Session is intended to be used in a non-concurrent fashion, that is, a particular instance of Session should be used in only one thread or task at a time.

context
for each task create sesion

Session used identity map pattern and stores objects keyed to their primary key.
it doesn’t do any kind of query caching
(it not a cache , but somewhat used as a cache)
weak reference by default. This also defeats the purpose of using the Session as a cache.

The Session is not designed to be a global object from which everyone consults as a “registry” of objects. 
That’s more the job of a second level cache. SQLAlchemy provides a pattern for implementing second level caching using dogpile.cache, via the Dogpile Caching example.

session = Session.object_session(someobject)

"""



class DatabaseSessionFactory:
    """
    Creates session makers for both synchronous and asynchronous engines.
    """

    def __init__(
        self, 
        engine: Union[Engine, AsyncEngine], 
        is_async: bool,
        autocommit:bool=False, # 
        autoflush:bool=False, # automatic flushing
        expire_on_commit:bool=False, # false = keep the object , no need to new sql query 
        info:Any=None,
        *arg:Any,
        **kwargs:Any
    ):
        self.is_async = is_async
        if self.is_async and isinstance(engine, AsyncEngine):
            self.async_session_maker = sessionmaker(
                bind=engine,
                class_=AsyncSession,
                expire_on_commit=expire_on_commit,
                autoflush=autoflush,
                autocommit=autocommit,
                info=info,
                *arg,
                **kwargs,
            )
            self.sync_session_maker = None
            
        elif not self.is_async and isinstance(engine, Engine):
            self.sync_session_maker = sessionmaker(
                bind=engine,
                expire_on_commit=expire_on_commit,
                autoflush=autoflush,
                autocommit=autocommit,
                info=info,
                *arg,
                **kwargs,
            )
            self.async_session_maker = None
        else:
            raise ValueError("Engine type does not match is_async flag.")

    def create_session(self) -> Union[Session, AsyncSession]:
        """
        Creates a new session.
        """
        if self.is_async:
            if self.async_session_maker:
                return self.async_session_maker()
        else:
            if self.sync_session_maker:
                # return await asyncio.to_thread(self.sync_session_maker)
                pass
            
        raise Exception("no session maker")
