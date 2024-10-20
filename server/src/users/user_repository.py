from typing import List,Optional,Dict,Any,Tuple

from server.lib.shared.schemas import BaseManySchema, SortOrder
from server.app.services.db import User 
from lib.common.orm.base_repository import BaseRepository
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import select
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from server.lib.common.loggers import logger
from server.lib.common.errors import AppError
from server.lib.common.constants.http_status_code import HTTPStatusCode



class UserRepository(BaseRepository[User]):
    
    def __init__(self):
        super().__init__(User)

    async def create_user(self,user_data):
        user = User(**user_data)
        async with self.get_session() as session:
            try:
                await session.begin()
                session.add(user)
                await session.commit()
                await session.flush()
                await session.refresh(user)
                return user
            except SQLAlchemyError as e:
                await session.rollback()
                # raise e
                raise AppError()
    
        
    async def get_user(self, user_id: str) -> Optional[User]:
        user = None
        async with self.get_session() as session:
            try:
                await session.begin()
                result = await session.execute(select(User).where(User.id == user_id)) 
                user = result.scalars().one_or_none()
                if not user:
                    raise AppError(http_status_code=HTTPStatusCode.NOT_FOUND)
                return user
            except SQLAlchemyError as e:
                await session.rollback()

    async def update_user(self, user_id: str, update_data: Dict[str, Any]) -> Optional[User]:
        async with self.get_session() as session:
            try:
                await session.begin()
                result = await session.execute(select(User).where(User.id == user_id)) 
                user = result.scalars().one_or_none()
                if user:
                    for key, value in update_data.items():
                        setattr(user, key, value)  # Update attributes
                    # user = await session.merge(user) # make sure user is in the current session
                    await session.commit()  # Commit the transaction
                    await session.refresh(user)  # Refresh the user
                    return user
                else:
                    raise AppError(http_status_code=HTTPStatusCode.NOT_FOUND)
                
            except SQLAlchemyError as e:
                await session.rollback()
                raise AppError()
                # raise e 


    async def delete_user(self, user_id: str) -> bool:
        async with self.get_session() as session:
            try:
                await session.begin()
                result = await session.execute(select(User).where(User.id == user_id)) 
                user = result.scalars().one_or_none()
                if user:
                    await session.delete(user)  # Delete the user
                    await session.commit()  # Commit the transaction
                    return user_id
                else:
                    raise AppError(http_status_code=HTTPStatusCode.NOT_FOUND)
            except SQLAlchemyError as e:
                await session.rollback()  # Rollback in case of error
                raise AppError()
                # raise e  # Raise the exception
    
    async def get_many_users(self, schema:BaseManySchema) -> Tuple[List[User], int]:
        users,total = await self.get_many(schema=schema)
        return users,total
    
    async def delete_all_users(self):
        """Delete all users directly from the database."""
        async with self.get_session() as session:  
            await session.begin()
            await session.execute("DELETE FROM users") 
            await session.commit()