from fastapi import APIRouter,Request
from . import access_control_controller
from typing import Any,List
from .access_control_schemas import (
    RoleResponseSchema,
    RoleCreateSchema,
    RoleUpdateSchema,
    RolesGetManySchema
)


access_control_router = APIRouter()

@access_control_router.post("", response_model=RoleResponseSchema)
async def create_role(
    request: Request,
    role_create_schema: RoleCreateSchema, 
    *args: Any, 
    **kwargs: Any
):
    """
    Create a new role with multiple options.
    """
    # request.body
    # request.path_params.items
    # request.query_params.items
    # request.headers
    # request.cookies
    # request.form
    # request.session
    # request.stream
    
    return await access_control_controller.create_role(request, role_create_schema, *args, **kwargs)

@access_control_router.get("{role_id}", response_model=RoleResponseSchema)
async def get_role(
    request: Request,
    role_id: int, 
    *args: Any, 
    **kwargs: Any
):
    """
    Retrieve a role by their ID.
    """
    user = await access_control_controller.get_role(request, role_id, *args, **kwargs)
    return user

    
@access_control_router.put("{role_id}", response_model=RoleResponseSchema)
async def update_role(
    request: Request,
    role_id: int, 
    role: RoleUpdateSchema, 
    *args: Any, 
    **kwargs: Any
):
    """
    Update a role's information.
    """
    updated_role = await access_control_controller.update_role(request, role_id, role, *args, **kwargs)
    return updated_role
    

@access_control_router.delete("{role_id}", status_code=204)
async def delete_role(
    request: Request,
    role_id: int, 
    *args: Any, 
    **kwargs: Any
):
    """
    
    """
    await access_control_controller.delete_role(request, role_id, *args, **kwargs)
    


@access_control_router.get("", response_model=List[RoleResponseSchema])
async def get_many_roles(
    request: Request,
    roles_get_many_schema: RolesGetManySchema, 
    *args: Any, 
    **kwargs: Any
):
    """
    Retrieve a list of roles with pagination.
    """
    roles = await access_control_controller.get_many_roles(request,roles_get_many_schema, *args, **kwargs)
    
    # return UsersResponseSchema(users=users)
