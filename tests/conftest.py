from fastapi import FastAPI
from fastapi.testclient import TestClient
from server.main import create_app
from server.app.services.db import db,User
from httpx import AsyncClient,ASGITransport
import pytest
import pytest_asyncio
# from server.lib.shared.performance import profiler
import asyncio
import uvloop # replacing event loop fixure with custom implementation is deprecated 
# from server.lib.common.loggers import logger
from server.lib.common.loggers import logger
from _pytest.logging import LogCaptureFixture
import logging
import typing
import cProfile
from line_profiler import LineProfiler
from memory_profiler import memory_usage
import io
import pstats
import re
from pytest import FixtureRequest
from typing import Callable
# from anyio import 

pytestmark = pytest.mark.anyio

BASE_URL = "http://testserver"

class PropagateHandler(logging.Handler):
    def emit(self,record):
        logger = logging.getLogger(record.name)
        if logger.isEnabledFor(record.levelno):
            logger.handle(record)


@pytest.fixture(autouse=True,scope="session")
def cleanup_loguru():
    logger.remove()
    
    
@pytest.fixture(autouse=True,scope="session")
def propegate_loguru(cleanup_loguru):
    handler_id = logger.add(PropagateHandler(),format="{message}")
    yield
    logger.remove(handler_id)
    

@pytest_asyncio.fixture(autouse=True) #ignore
async def caplog(caplog: LogCaptureFixture):
    """
        Make pytest work with loguru. See:https://loguru.readthedocs.io/en/stable/resources/migration.html#making-things-work-with-pytest-and-caplog
    """
    handler_id = logger.add(
        caplog.handler,
        format="{message}",
        level=0,
        filter=lambda record: record["level"].no >= caplog.handler.level,
        enqueue=False,  # Set to 'True' if your test is spawning child processes.
    )
    yield caplog
    logger.remove(handler_id)
    
    
def pytest_collection_modifyitems(items):
    pytest_asyncio_tests = (item for item in items if pytest_asyncio.is_async_test(item))
    session_scope_marker = pytest.mark.asyncio(loop_scope="session")
    for async_test in pytest_asyncio_tests:
        async_test.add_marker(session_scope_marker, append=False)


@pytest.fixture(params=[
    pytest.param(('asyncio', {'use_uvloop': True}), id='asyncio+uvloop'),
    # pytest.param(('asyncio', {'use_uvloop': False}), id='asyncio'),
    # pytest.param(('trio', {'restrict_keyboard_interrupt_to_checkpoints': True}), id='trio')
])
def anyio_backend(request):
    return request.param


# @pytest.fixture(scope='session')
# def event_loop(request):
#     """Create an instance of the default event loop for each test case."""
#     loop = asyncio.get_event_loop_policy().new_event_loop()
#     yield loop
#     loop.close()

@pytest_asyncio.fixture(loop_scope="session")
async def app(anyio_backend):
    app = create_app()
    yield app
    # shutdown app.
    

@pytest_asyncio.fixture(loop_scope="session")
async def test_client(app:FastAPI):
    client = TestClient(app=app)
    yield client
    client.close()
    

@pytest_asyncio.fixture(loop_scope="session")
async def database(request:FixtureRequest,anyio_backend):
    # async with db.get_session_factory().create_session() as session:
    if request.__module__ and not "router" in request.node.fspath.basename:
        await db.drop_all()
        await db.create_all()
    # await session.commit()
    

@pytest_asyncio.fixture(loop_scope="session",scope="function")
async def async_client(app: FastAPI):
    transport:ASGITransport = ASGITransport(
        app=app,
        raise_app_exceptions=False,
        # client=("1.2.3.4",123),
        # root_path="/submount"
    )
    async with AsyncClient(
        transport=transport, 
        base_url=BASE_URL,
        headers={
            "Accept": "application/json",  # Indicating that the client expects JSON responses
            "Content-Type": "application/json",  # Indicating the content type of the request   
        },
        
        
    ) as ac:
        yield ac
        




# @pytest_asyncio.fixture()


# profiler = profiler.Profiler.init("pytest_profiling", num=1000)

# @pytest_asyncio.fixture(scope="function")
# def apply_profiler():
#     """
#     Pytest fixture to apply profiling to a test function.
#     Can be used as a decorator.
#     """
#     return profiler.profile

# @pytest_asyncio.fixture(autouse=True, loop_scope="session", scope="function")
# async def apply_profiler(request):
#     """Fixture to apply profiling for each test function."""
#     # if request.node.get_closest_marker("profile"):
#     prof = cProfile.Profile()
#     line_profiler = LineProfiler()
    
#     # line_profiler.add_function(func)
#     # mem_usage = memory_usage(func,max_usage=True)
#     # @line_profiler.pro
#     # async def run_test():
#     #     # Call the test function and await it
#     #     func

#     # Capture memory usage while running the test function
#     # mem_usage = memory_usage(asyncio.get_event_loop().run_in_executor(None,run_test,1), max_usage=True, interval=0.1)  # Monitor memory usage
#     mem_usage = []
#     prof.enable()
#     yield
#     prof.disable()
#     logger.info("\n=== Profiling Summary ===")

#     stats_stream = io.StringIO()
#     ps = pstats.Stats(prof, stream=stats_stream).sort_stats('cumulative')
#     regex_pattern = r'^(?!.*(builtins|<module>|__main__)).*'  # Adjust this regex as needed
#     # filtered_stats = []
#     # regex = re.compile(regex_pattern)
#     # for filename, lineno, name in ps.stats.keys():
#     #     if regex.search(name):
#     #         filtered_stats.append((filename, lineno, name))

#     # for filename, lineno, name in filtered_stats:
#     #     ps.print_stats([name])

#     ps.strip_dirs()
#     ps.sort_stats('cumtime')
#     ps.print_stats(10)
    
#     line_stats_stream = io.StringIO()
#     line_profiler.print_stats(stream=line_stats_stream) 
    
#     usage = []
#     for mem in mem_usage:
#         usage.append(f"{mem:.2f} MB")
#     memory_stats = '\n'.join(usage)

#     logger.info(f"\n\nStats Summary:\n {stats_stream.getvalue()}")
#     logger.info(f"\n\nLine Profiler Results:\n\n{line_stats_stream.getvalue()}")
#     logger.info(f"\n\nMemory Usage (in MB):\n{memory_stats}")
#     logger.info()



def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """
    Hook to display a summary of profiling after tests run.
    """
    # if len([1]) > 0:
    #     print("\n=== Profiling Summary ===")
    # else:
    #     print("\n=== Profiling Summary (None) ===")
    pass    
    
