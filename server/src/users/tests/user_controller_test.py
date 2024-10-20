from lib.common.loggers import logger
import pytest
from fastapi import Request
from server.src.users.user_controller import create_user, get_user, update_user, delete_user, get_many_users
from server.src.users.user_schemas import UserCreateSchema, UserProfileSchema, UserUpdateSchema, UsersGetManySchema
from .user_test import UserTest
from unittest.mock import AsyncMock, patch
import json
from app.services.db import User

@pytest.mark.asyncio
@pytest.mark.run(after='TestUserRouter')
class TestUserController(UserTest):
    
    async def test_create_user(self):
        try:
            mock_create_user = self.mocker.patch(target="server.src.users.user_service.create_user",new_callable=AsyncMock)
            new_name = "user_new_name"
            user_args = {
                "first_name":new_name    
            }
            request_user_args = {
                "profile":{
                    "first_name":new_name    
                }
            }
            user = User(**user_args)
            mock_create_user.return_value = user
            response = await self.client.post("/users",json=request_user_args)
            assert response.status_code == 201
            mock_create_user.assert_awaited()
            mock_create_user.assert_awaited_once()
            mock_create_user.assert_called_once()
            mock_create_user.assert_called_once_with(UserCreateSchema(profile=UserProfileSchema(first_name=new_name)),[],{})
        except Exception as e:
            pytest.fail(f"unknown error has occured: {str(e)}")
        
    async def test_get_user(self):
        try:
            mock_get_user = self.mocker.patch(target="server.src.users.user_service.get_user",new_callable=AsyncMock)
            user_id = "1"
            new_name = "user_new_name"
            user_args = {
                "id":user_id,
                "first_name":new_name
            }
            user = User(**user_args)
            mock_get_user.return_value = user
            response = await self.client.get(f"/users/{user_id}")
            assert response.status_code == 200
            mock_get_user.assert_awaited()
            mock_get_user.assert_awaited_once()
            mock_get_user.assert_called_once()
            mock_get_user.assert_called_once_with(user_id,[],{})
        except Exception as e:
            pytest.fail(f"unknown error has occured: {str(e)}")
            
    async def test_update_user(self):
        try:
            mock_update_user = self.mocker.patch(target="server.src.users.user_service.update_user",new_callable=AsyncMock)
            new_name = "user_new_name"
            user_id = "1"
            user_args = {
                "id":user_id,
                "first_name":new_name
            }
            user = User(**user_args)
            mock_update_user.return_value = user
            response = await self.client.put(f"/users/{user_id}",json={
                "auth":{
                    "id":user_id,
                },
                "profile":{
                    "first_name":new_name
                }
            })
            assert response.status_code == 200
            mock_update_user.assert_awaited()
            mock_update_user.assert_awaited_once()
            mock_update_user.assert_called_once()
            mock_update_user.assert_called_once_with(user_id,user_args,[],{})
            
        except Exception as e:
            pytest.fail(f"unknown error has occured: {str(e)}")
            
    async def test_delete_user(self):
        try:
            mock_delete_user = self.mocker.patch(target="server.src.users.user_service.delete_user",new_callable=AsyncMock)
            new_name = "user_new_name"
            user_id = "1"
            mock_delete_user.return_value = {}
            response = await self.client.delete(f"/users/{user_id}")
            assert response.status_code == 200
            mock_delete_user.assert_awaited()
            mock_delete_user.assert_awaited_once()
            mock_delete_user.assert_called_once()
            mock_delete_user.assert_called_once_with(user_id,[],{})
            
        except Exception as e:
            pytest.fail(f"unknown error has occured: {str(e)}")

    async def test_get_many_users(self):
        try:
            mock_get_user = self.mocker.patch(target="server.src.users.user_service.get_many_users",new_callable=AsyncMock)
            users = [
                User(**{
                "id":"1",
                "first_name":"name1"
            }),
                User(**{
                "id":"2",
                "first_name":"name2"
            }),
                User(**{
                "id":"3",
                "first_name":"name3"
            })
            ]
            total = len(users)
            mock_get_user.return_value = users,total
            response = await self.client.get(f"/users")
            assert response.status_code == 200
            mock_get_user.assert_awaited()
            mock_get_user.assert_awaited_once()
            mock_get_user.assert_called_once()
            mock_get_user.assert_called_once_with(None,[],{})
        except Exception as e:
            pytest.fail(f"unknown error has occured: {str(e)}")
        
        
        
    # async def test_invalid_create_user(self):
    #     response = await self.client.post("/users",json={})
    #     assert response.status_code == 201

    # async def test_get_non_existent_user(self):
    #     response = await self.client.get("/users/1a23")
    #     assert response.status_code == 200
    
    # async def test_update_non_existent_user(self):
    #     response = await self.client.put("/users/1a23")
    #     assert response.status_code == 200
    
    # async def test_delete_non_existent_user(self):
    #     response = await self.client.delete("/users/1a23")
    #     assert response.status_code == 201

    # async def test_invalid_get_many_users(self):
    #     response = await self.client.get("/users")
    #     assert response.status_code == 200
    #     assert isinstance(response.json(),list) is True        
        # try:
            
        #     assert response is not None
        #     assert response.status_code != 404, "Expected status code not to be 404"
        #     assert response.status_code != 405, "Expected status code not to be 404"
        # except requests.exceptions.ConnectionError:
        #     pytest.fail("Connection refused or could not resolve hostname")
        # except requests.exceptions.Timeout:
        #     pytest.fail("Request timed out")
        # except Exception as e:
        #     pytest.fail(f"An unexpected error occurred: {str(e)}")

    
    

    
    # async def test_create_user_controller(self):
    #     # Mock the service method
    
    #     class Foo(object):
    #         def bar(self, v):
    #             return v * 2

    #     foo = Foo()
    #     spy = mocker.spy(foo, 'bar')
    #     assert foo.bar(21) == 42

    #     spy.assert_called_once_with(21)
    #     assert spy.spy_return == 42
        
#         monkeypatch.setattr("server.src.users.user_service.create_user", mock_create_user_service)

#         # Mock request and schema
#         mock_request = AsyncMock(Request)
#         mock_schema = UserCreateSchema(username="testuser")

#         # Call the controller
#         result = await create_user(mock_request, mock_schema)

#         # Assertions
#         assert result["id"] == "test123"
#         assert result["username"] == "testuser"

#     async def test_get_user_controller(self, monkeypatch):
#         # Mock the service method
#         async def mock_get_user_service(user_id, *args, **kwargs):
#             return {"id": "test123", "username": "testuser"}

#         monkeypatch.setattr("server.src.users.user_service.get_user", mock_get_user_service)

#         # Mock request
#         mock_request = AsyncMock(Request)

#         # Call the controller
#         result = await get_user(mock_request, "test123")

#         # Assertions
#         assert result["id"] == "test123"
#         assert result["username"] == "testuser"
