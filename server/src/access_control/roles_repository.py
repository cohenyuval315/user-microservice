from typing import List,Optional,Dict,Any
from server.lib.shared.schemas import BaseManySchema, SortOrder
from server.src.access_control.role import Role
from server.src.access_control.user_role import UserRole
from lib.common.orm.base_repository import BaseRepository
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import select


class AccessControlRepository(BaseRepository[Role]):
    
    def __init__(self):
        super().__init__(Role)

    async def create_user(self,user_data):
        user = User(**user_data)
        async with self.session as session:
            try:
                async with session.begin():
                    await session.add(user)
                    
                await session.flush()
                await session.commit()
                await session.refresh(user)
                
            except SQLAlchemyError as e:
                await session.rollback()
                raise e
        
        return user # refreshed from the refresh(user)
    
    async def get_user(self, user_id: str) -> Optional[User]:
        async with self.session as session:
            try:
                result = await session.execute(select(User).where(User.id == user_id)) 
                return result.scalars().one_or_none()
            except SQLAlchemyError as e:
                raise e 
            
            
    async def update_user(self, user_id: str, update_data: Dict[str, Any]) -> Optional[User]:
        async with self.session as session:
            try:
                user = await self.get_user(user_id) 
                if user:
                    for key, value in update_data.items():
                        setattr(user, key, value)  # Update attributes
                    await session.commit()  # Commit the transaction
                    await session.refresh(user)  # Refresh the user
                    return user
                else:
                    return None  
            except SQLAlchemyError as e:
                await session.rollback()
                raise e 


    async def delete_user(self, user_id: str) -> bool:
        async with self.session as session:
            try:
                user = await self.get_user(user_id)  # Retrieve the user first
                if user:
                    await session.delete(user)  # Delete the user
                    await session.commit()  # Commit the transaction
                    return True  # User deleted
                else:
                    return False  # User not found
            except SQLAlchemyError as e:
                await session.rollback()  # Rollback in case of error
                raise e  # Raise the exception
    
    async def get_many_users(self, schema:BaseManySchema) -> List[User]:
        return await self.get_many(schema=schema)
        
