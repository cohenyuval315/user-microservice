from .user_repository import UserRepository
from typing import Any,Dict,List
from .user_schemas import (
    UserCreateSchema, 
    UserUpdateSchema, 
    UsersGetManySchema, 
    UsersUpdateManySchema, 
    UsersDeleteManySchema
)
from lib.common.errors.app_error import AppError

async def create_user(user_create_schema: UserCreateSchema, *args: Any,**kwargs: Any):
    user_repo = UserRepository()
    # if (getattr(user_create_schema.auth,))
    new_user = await user_repo.create_user(user_create_schema.model_dump())
    return new_user

async def get_user(user_id: str, *args: Any,**kwargs: Any):
    user_repo = UserRepository()
    user = await user_repo.get_user(user_id)
    if not user:
        raise AppError()
    return user

async def update_user(user_id: str, user_update_data: Dict[str,Any], *args: Any,**kwargs: Any):
    user_repo = UserRepository()
    user = await user_repo.update_user(user_id,user_update_data)
    return user

async def delete_user(user_id: str, *args: Any,**kwargs: Any):
    user_repo = UserRepository()
    is_deleted = await user_repo.delete_user(user_id)
    return is_deleted

async def get_many_users(users_get_many_schema: UsersGetManySchema, *args: Any,**kwargs: Any):
    user_repo = UserRepository()
    users,total = await user_repo.get_many_users(schema=users_get_many_schema)
    return users,total
    

# async def update_many_users(users_update_many_schema: UsersUpdateManySchema, *args: Any,**kwargs: Any):
#     return await user_repository.update_many_users(users_update_many_schema)

# async def delete_many_users(users_delete_many_schema: UsersDeleteManySchema, *args: Any,**kwargs: Any):
#     return await user_repository.delete_many_users(users_delete_many_schema)
