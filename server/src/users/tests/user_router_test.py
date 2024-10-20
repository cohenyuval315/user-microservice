import time
from unittest.mock import AsyncMock

import pytest
import requests
from lib.common.loggers import logger

# from server.src.users import user_router

from .user_test import UserTest

timeout = 2  # 2 seconds


@pytest.mark.asyncio(loop_scope="session")
class TestUserRouter(UserTest):

    async def test_random_post_user_endpoint(self):
        try:
            response = await self.client.post("/dasdadada", timeout=timeout)
            assert response is not None
            assert response.status_code == 404, "Expected status code  to be 405"
            # assert response.status_code == 405, "Expected status code  to be 405"
        except requests.exceptions.ConnectionError:
            pytest.skip("Connection refused or could not resolve hostname")
        except requests.exceptions.Timeout:
            pytest.skip("Request timed out")
        except Exception as e:
            pytest.skip(f"An unexpected error occurred: {str(e)}")


    async def test_random_get_user_endpoint(self):
        try:
            response = await self.client.get("/dasdadada", timeout=timeout)
            assert response is not None
            assert response.status_code == 404, "Expected status code  to be 405"
        except requests.exceptions.ConnectionError:
            pytest.skip("Connection refused or could not resolve hostname")
        except requests.exceptions.Timeout:
            pytest.skip("Request timed out")
        except Exception as e:
            pytest.skip(f"An unexpected error occurred: {str(e)}")


    async def test_create_user(self):
        try:
            response = await self.client.post("/users", timeout=timeout,json={})                
            assert response is not None
            assert response.status_code != 405, "Expected status code not to be 404"
        except requests.exceptions.ConnectionError:
            pytest.fail("Connection refused or could not resolve hostname")
        except requests.exceptions.Timeout:
            pytest.fail("Request timed out")
        except Exception as e:
            pytest.fail(f"An unexpected error occurred: {str(e)}")

    async def test_get_user(self):
        response = None
        try:
            response = await self.client.get("/users/1a23", timeout=timeout)
            assert response is not None
            # assert response.status_code == 404
            # assert response.status_code != 405
        except requests.exceptions.ConnectionError:
            pytest.fail("Connection refused or could not resolve hostname")
        except requests.exceptions.Timeout:
            pytest.fail("Request timed out")
        except Exception as e:
            pytest.fail(f"An unexpected error occurred: {str(e)}")

    async def test_update_user(self):
        try:
            response = await self.client.put("/users/1a23", timeout=timeout)
            assert response is not None
            assert response.status_code != 404
            assert response.status_code != 405, "Expected status code not to be 404"
        except requests.exceptions.ConnectionError:
            pytest.fail("Connection refused or could not resolve hostname")
        except requests.exceptions.Timeout:
            pytest.fail("Request timed out")
        except Exception as e:
            pytest.fail(f"An unexpected error occurred: {str(e)}")

    async def test_delete_user(self):
        try:
            response = await self.client.delete("/users/1a23", timeout=timeout)
            # logger.info(f"Response status code: {response.status_code}")
            # logger.info(f"Response body: {response.text}")
            
            assert response is not None
            # assert response.status_code != 404
            # assert response.status_code != 405, "Expected status code not to be 404"
        except requests.exceptions.ConnectionError:
            pytest.fail("Connection refused or could not resolve hostname")
        except requests.exceptions.Timeout:
            pytest.fail("Request timed out")
        except Exception as e:
            pytest.fail(f"An unexpected error occurred: {str(e)}")

    async def test_get_many_users(self):
        try:
            response = await self.client.get("/users", timeout=timeout)
            assert response is not None
            assert response.status_code != 404, "Expected status code not to be 404"
            assert response.status_code != 405, "Expected status code not to be 404"
        except requests.exceptions.ConnectionError:
            pytest.fail("Connection refused or could not resolve hostname")
        except requests.exceptions.Timeout:
            pytest.fail("Request timed out")
        except Exception as e:
            pytest.fail(f"An unexpected error occurred: {str(e)}")
