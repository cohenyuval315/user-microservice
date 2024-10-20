from lib.common.loggers import logger
import pytest
from server.src.users.user_schemas import UserCreateSchema, UserUpdateSchema, UsersGetManySchema
from server.lib.common.errors.app_error import AppError
from .user_test import UserTest
from lib.common.loggers import logger
import pytest
from fastapi import Request
from server.src.users.user_controller import create_user, get_user, update_user, delete_user, get_many_users
from server.src.users.user_schemas import UserCreateSchema, UserUpdateSchema, UsersGetManySchema
from .user_test import UserTest

@pytest.mark.asyncio
@pytest.mark.run(after='TestUserController')
class TestUserService(UserTest):
    async def test_create_user(self):
        response = await self.client.post("/users",json={})
        assert response.status_code == 201
        
    async def test_get_user(self):
        try:
            response = await self.client.post("/users",json={})
            assert response is not None
            result = response.json()
            user = result['data'] 
            user_id = user['id']
            response = await self.client.get(f"/users/{user_id}")
            result = response.json()
            assert response.status_code == 200
        except Exception as e:
            pytest.fail(f"unknown error has occured: {str(e)}")
            
    async def test_update_user(self):
        try:
            expected = "new_name"
            response = await self.client.post("/users",json={})
            assert response is not None
            result = response.json()
            user = result['data'] 
            user_id = user['id']
            response = await self.client.put(f"/users/{user_id}",json={
                "profile":{
                    "first_name":expected
                }
            })
            result = response.json()
            user = result['data'] 
            actual = user["first_name"]         
            assert response.status_code == 200
            assert actual == expected
            
        except Exception as e:
            pytest.fail(f"unknown error has occured: {str(e)}")
            
    async def test_delete_user(self):
        try:
            response = await self.client.post("/users",json={})
            assert response is not None
            result = response.json()
            user = result['data'] 
            user_id = user['id']
            response = await self.client.delete(f"/users/{user_id}")
            assert response.status_code == 200
            response = await self.client.get(f"/users/{user_id}")
            assert response.status_code == 404
            
        except Exception as e:
            pytest.fail(f"unknown error has occured: {str(e)}")

    async def test_get_many_users(self):
        response = await self.client.get("/users")
        assert response.status_code == 200
        # assert isinstance(response.json(),list) is True
        
# @pytest.mark.asyncio
# class (UserTest):
#     async def test_create_user(self, monkeypatch):
#         # Prepare test data
#         mock_user_data = UserCreateSchema(username="testuser")

#         # Mock the repository method
#         async def mock_create_user(user_data):
#             return {"id": "test123", "username": "testuser"}

#         monkeypatch.setattr("server.src.users.user_repository.UserRepository.create_user", mock_create_user)

#         # Call the service
#         new_user = await create_user(mock_user_data)

#         # Assertions
#         assert new_user["id"] == "test123"
#         assert new_user["username"] == "testuser"

#     async def test_get_user(self, monkeypatch):
#         # Mock the repository method
#         async def mock_get_user(user_id):
#             return {"id": "test123", "username": "testuser"}

#         monkeypatch.setattr("server.src.users.user_repository.UserRepository.get_user", mock_get_user)

#         # Call the service
#         user = await get_user("test123")

#         # Assertions
#         assert user["id"] == "test123"
#         assert user["username"] == "testuser"

#     async def test_update_user(self, monkeypatch):
#         # Mock the repository method
#         async def mock_update_user(user_id, update_data):
#             return {"id": "test123", "first_name": "updated_name"}

#         monkeypatch.setattr("server.src.users.user_repository.UserRepository.update_user", mock_update_user)

#         update_data = UserUpdateSchema(first_name="updated_name")

#         # Call the service
#         updated_user = await update_user("test123", update_data)

#         # Assertions
#         assert updated_user["first_name"] == "updated_name"
    
#     async def test_delete_user(self, monkeypatch):
#         # Mock the repository method
#         async def mock_delete_user(user_id):
#             return True

#         monkeypatch.setattr("server.src.users.user_repository.UserRepository.delete_user", mock_delete_user)

#         # Call the service
#         result = await delete_user("test123")

#         # Assertions
#         assert result is True

#     async def test_get_many_users(self, monkeypatch):
#         # Mock the repository method
#         async def mock_get_many_users(schema):
#             return [{"id": "test123", "username": "testuser"}]

#         monkeypatch.setattr("server.src.users.user_repository.UserRepository.get_many_users", mock_get_many_users)

#         get_many_schema = UsersGetManySchema(offset=0, limit=10)

#         # Call the service
#         users = await get_many_users(get_many_schema)

#         # Assertions
#         assert len(users) == 1
#         assert users[0]["id"] == "test123"
#         assert users[0]["username"] == "testuser"
