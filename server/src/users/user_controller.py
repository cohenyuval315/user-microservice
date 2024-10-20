from . import user_service
from fastapi import Request
from typing import Any
from .user_schemas import (
    UserCreateSchema, 
    UserUpdateSchema, 
    UsersGetManySchema, 
    UsersUpdateManySchema, 
    UsersDeleteManySchema
)
from server.lib.common.loggers import logger
from typing import List

async def create_user(request:Request, user_create_schema:UserCreateSchema, *args: Any,**kwargs: Any):
    create_data = {}
    if  user_create_schema.model_dump():
        # create_data = {value: value for key,value in user_create_schema.model_dump().items() for key, value in subdict.items()}    
        for field in user_create_schema.model_dump().values():
            if field is not None:
                create_data.update(field)        
    return await user_service.create_user(create_data, *args,**kwargs)

async def get_user(request:Request, user_id: str, *args:Any,**kwargs:Any):
    return await user_service.get_user(user_id,*args,**kwargs)

async def update_user(request:Request, user_id: str, user_update_schema:UserUpdateSchema, *args:Any,**kwargs:Any):
    update_data = {}
    if  user_update_schema.model_dump():
        update_data = {key: value for subdict in user_update_schema.model_dump().values() for key, value in subdict.items()}
    return await user_service.update_user(user_id, update_data,*args,**kwargs)

async def delete_user(request:Request, user_id: str, *args:Any,**kwargs:Any):
    return await user_service.delete_user(user_id,*args,**kwargs)

async def get_many_users(request:Request, users_get_many_schema:UsersGetManySchema, *args:Any,**kwargs:Any):
    return await user_service.get_many_users(users_get_many_schema, *args,**kwargs)

# async def update_many_users(request:Request, users_update_many_schema:UsersUpdateManySchema, *args:Any,**kwargs:Any):
#     return await user_service.update_many_users(users_update_many_schema,*args,**kwargs)

# async def delete_many_users(request:Request, users_delete_many_schema:UsersDeleteManySchema, *args:Any,**kwargs:Any):
#     return await user_service.delete_many_users(users_delete_many_schema,*args,**kwargs)
