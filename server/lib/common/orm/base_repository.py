from typing import Type, TypeVar, Generic, List, Optional, Callable, Awaitable, Any,Dict
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.future import select
from sqlalchemy import func

from server.lib.shared.schemas import BaseManySchema, SortOrder
from server.lib.common.errors import AppError
from . import db
import functools
from server.lib.utils.concurrency.asynchronization.asynchronous import async_wrap,async_class_wrap,async_instance_wrap
from server.lib.common.loggers import logger

T = TypeVar('T')


class BaseRepository(Generic[T]):
    def __init__(self, model: Type[T],models: Optional[Dict[Type[T],Any]]=None):
        self.model = model
        self.factory = db.get_session_factory()

    def get_session(self):
        return self.factory.create_session()
    
    def get_new_session(self):
        return db.get_session_factory().create_session()
        

    async def get_many(self, schema: BaseManySchema) -> List[Type[T]]:
        async with self.get_session() as session:
            try:
                query = select(self.model)
                if schema:
                    data = schema
                    if data.get('filters') is not None:
                        for key, value in data.get('filters').items():
                            query = query.where(getattr(self.model, key) == value)
                    

                subquery = query.subquery()
                count_query = select(func.count()).select_from(subquery) # noqa
                total_result = await session.execute(count_query)
                total = total_result.scalar()
                
                if schema:
                    data = schema
                    if data.get('sort_by') is not None:
                        if data.get('sort_by') == SortOrder.asc:
                            query = query.order_by(getattr(self.model, data.get('sort_by')).asc())
                        else:
                            query = query.order_by(getattr(self.model, data.get('sort_by')).desc())

                    if data.get('offset') is not None:
                        query = query.offset(data.get('offset'))
                        
                    if  data.get('limit') is not None:
                        query = query.limit(data.get('limit'))
                    
                result = await session.execute(query)
                
                return result.scalars().all() ,total

            except SQLAlchemyError as e:
                raise AppError()
                raise e  