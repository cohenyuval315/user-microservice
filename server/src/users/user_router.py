from fastapi import APIRouter,Request,Query

from server.lib.shared.schemas import MetaSchema, PaginationSchema
from . import user_controller
from typing import Any,List,Annotated,Optional
from .user_schemas import (
    UserCreateSchema,
    UserUpdateSchema,
    UserResponseSchema,
    UsersResponseSchema,
    UsersDeleteManySchema,
    UsersGetManySchema,
    UsersUpdateManySchema
)
from fastapi.responses import JSONResponse
import json
from server.lib.common.loggers import logger



user_router = APIRouter()

@user_router.post("", response_model=UserResponseSchema,status_code=201)
async def create_user(
    request: Request,
    user_create_schema: Optional[UserCreateSchema] = None
)-> Any:
    """
    Create a new user with multiple options.
    """
    user = await user_controller.create_user(request, user_create_schema, [] ,{})
    logger.info(user)
    return UserResponseSchema(
        data=user.as_dict(),
        status_code=201,
    )

@user_router.get("/{user_id}", response_model=UserResponseSchema,status_code=200)
async def get_user(
    request: Request,
    user_id: str
)-> Any:
    """
    Retrieve a user by their ID.
    """
    user = await user_controller.get_user(request, user_id,[],{})
    return UserResponseSchema(
        data=user.as_dict(),
        status_code=200,
    )    

    
@user_router.put("/{user_id}", response_model=UserResponseSchema, status_code=200)
async def update_user(
    request: Request,
    user_id: str, 
    user_update_schema: UserUpdateSchema
)-> Any:
    """
    Update a user's information.
    """
    user = await user_controller.update_user(request, user_id, user_update_schema, [] ,{})
    return UserResponseSchema(
        data=user.as_dict(),
        status_code=200,
    )    
    

@user_router.delete("/{user_id}", status_code=200)
async def delete_user(
    request: Request,
    user_id: str
)-> Any:
    """
    Delete a user by their ID.
    """
    await user_controller.delete_user(request, user_id, [] ,{})
    return UserResponseSchema(
        status_code=200,
        message="User Deleted Successfuly!"
    )       
    


@user_router.get("", response_model=UsersResponseSchema,status_code=200)
async def get_many_users(
    request: Request,
    users_get_many_schema:Optional[Annotated[UsersGetManySchema, Query()]]=None
)-> Any:
    """
    Retrieve a list of users with pagination.
    """
    users,total = await user_controller.get_many_users(request,users_get_many_schema, [] ,{})
    meta = None
    if users_get_many_schema and users_get_many_schema.model_dump().get("limit") and users_get_many_schema.model_dump().get("offset"):
        page_size = users_get_many_schema.limit
        page = (users_get_many_schema.offset // users_get_many_schema.limit) + 1   
        meta=MetaSchema(
            pagination=PaginationSchema(
                total=total,
                page=page,
                page_size=page_size                
            )
        )         
        
    return UsersResponseSchema(
            data=[user.as_dict() for user in users],
            status_code=200,
            meta=meta
    )
        

# @user_router.put("", response_model=UsersResponseSchema)
# async def update_many_users(
#     request: Request,
#     users_update_many_schema:UsersUpdateManySchema, 
# ):
#     """
#     Update multiple users.
#     """
#     updated_users = await user_controller.update_many_users(request, users_update_many_schema, [] ,{})
#     return UsersResponseSchema(users=updated_users)


# @user_router.delete("", status_code=204)
# async def delete_many_users(
#     request: Request,
#     users_delete_many_schema:UsersDeleteManySchema,
# ):
#     """
#     Delete multiple users by their IDs.
#     """
#     await user_controller.delete_many_users(request,users_delete_many_schema, [] ,{})

