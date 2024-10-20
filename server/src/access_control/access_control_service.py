from .access_control_repository import AccessControlRepository
from typing import Any
from .access_control_schemas import (
    RoleCreateSchema,
    RoleResponseSchema,
    RolesGetManySchema,
    RoleUpdateSchema 
)

async def create_role(role_create_schema: RoleCreateSchema, *args: Any,**kwargs: Any):
    ac_repo = AccessControlRepository()
    new_role = await ac_repo.create_role(role_create_schema.model_dump())
    return new_role

async def get_role(role_id: str, *args: Any,**kwargs: Any):
    ac_repo = AccessControlRepository()
    user = await ac_repo.get_role(role_id)
    return user

async def update_role(role_id: str, role_update_data: RoleUpdateSchema, *args: Any,**kwargs: Any):
    ac_repo = AccessControlRepository()
    role = await ac_repo.update_role(role_id,role_update_data)
    return role

async def delete_role(role_id: str, *args: Any,**kwargs: Any):
    ac_repo = AccessControlRepository()
    is_deleted = await ac_repo.delete_role(role_id)
    return is_deleted

async def get_many_roles(roles_get_many_schema: RolesGetManySchema, *args: Any,**kwargs: Any):
    ac_repo = AccessControlRepository()
    users = await ac_repo.get_many_roles(schema=roles_get_many_schema)
    return users
    
