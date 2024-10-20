import pytest
from server.lib.common.orm.database import Database
from server.lib.common.loggers import logger
from httpx import AsyncClient
import pytest_asyncio
from pytest import FixtureRequest
from pytest_mock import MockerFixture
from fastapi.testclient import TestClient


@pytest.mark.asyncio(loop_scope="session")
class BaseTest():
    """Base class for tests, integrating pytest fixtures."""

    # @pytest_asyncio.fixture(autouse=True)
    # async def setup_url(self, request:FixtureRequest, base_url:str):
        
    #     """Set up the test environment for all derived tests."""
    #     self.base_url = base_url
    
    
    @pytest_asyncio.fixture(autouse=True)
    async def setup_app(self, request:FixtureRequest, async_client:AsyncClient):
        
        """Set up the test environment for all derived tests."""
        self.client = async_client
    
    @pytest_asyncio.fixture(autouse=True)
    async def setup_db(self, request:FixtureRequest, database: Database):
        """Set up the database for tests marked with 'database'."""
        self.db = database
        
    @pytest_asyncio.fixture(autouse=True)
    async def setup_mocker(self, request:FixtureRequest, mocker:MockerFixture):
        """Set up the database for tests marked with 'database'."""
        self.mocker = mocker


    @pytest_asyncio.fixture(autouse=True)
    async def setup_test_client(self, request:FixtureRequest, test_client:TestClient):
        
        """Set up the test environment for all derived tests."""
        self.test_client = test_client
    