from typing import List,Optional,Dict,Any
from server.lib.shared.schemas import BaseManySchema, SortOrder
from server.app.services.db import Role
from lib.common.orm.base_repository import BaseRepository
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import select


class AccessControlRepository(BaseRepository[Role]):
    
    def __init__(self):
        super().__init__(Role)

    async def create_role(self,user_data):
        role = Role(**user_data)
        async with self.session as session:
            try:
                async with session.begin():
                    await session.add(role)
                    
                await session.flush()
                await session.commit()
                await session.refresh(role)
                
            except SQLAlchemyError as e:
                await session.rollback()
                raise e
        
        return role # refreshed from the refresh(user)
    
    async def get_role(self, role_id: str) -> Optional[Role]:
        async with self.session as session:
            try:
                result = await session.execute(select(Role).where(Role.id == role_id)) 
                return result.scalars().one_or_none()
            except SQLAlchemyError as e:
                raise e 
            
            
    async def update_role(self, role_id: str, role_update_data: Dict[str, Any]) -> Optional[Role]:
        async with self.session as session:
            try:
                role = await self.get_role(role_id) 
                if role:
                    for key, value in role_update_data.items():
                        setattr(role, key, value)  # Update attributes
                    await session.commit()  # Commit the transaction
                    await session.refresh(role)  # Refresh the user
                    return role
                else:
                    return None  
            except SQLAlchemyError as e:
                await session.rollback()
                raise e 


    async def delete_role(self, role_id: str) -> bool:
        async with self.session as session:
            try:
                role = await self.get_role(role_id)  # Retrieve the user first
                if role:
                    await session.delete(role)  # Delete the user
                    await session.commit()  # Commit the transaction
                    return True  # User deleted
                else:
                    return False  # User not found
            except SQLAlchemyError as e:
                await session.rollback()  # Rollback in case of error
                raise e  # Raise the exception
    
    async def get_many_roles(self, schema:BaseManySchema) -> List[Role]:
        return await self.get_many(schema=schema)
        
