from . import access_control_service
from fastapi import Request
from typing import Any
from .access_control_schemas import (
    RoleResponseSchema,
    RoleCreateSchema,
    RoleUpdateSchema,
    RolesGetManySchema
)

async def create_role(request:Request, role_create_schema:RoleCreateSchema, *args: Any,**kwargs: Any):
    return await access_control_service.create_role(role_create_schema, *args,**kwargs)

async def get_role(request:Request, role_id: str, *args:Any,**kwargs:Any):
    return await access_control_service.get_role(role_id,*args,**kwargs)

async def update_role(request:Request, role_id: str, role_update_schema:RoleUpdateSchema, *args:Any,**kwargs:Any):
    return await access_control_service.update_role(role_id, role_update_schema,*args,**kwargs)

async def delete_role(request:Request, role_id: str, *args:Any,**kwargs:Any):
    return await access_control_service.delete_role(role_id,*args,**kwargs)

async def get_many_roles(request:Request, roles_get_many_schema:RolesGetManySchema, *args:Any,**kwargs:Any):
    return await access_control_service.get_many_roles(roles_get_many_schema, *args,**kwargs)
