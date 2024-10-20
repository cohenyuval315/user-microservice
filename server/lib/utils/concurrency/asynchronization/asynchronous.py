# asyncozing.py

# from concurrent.futures import ThreadPoolExecutor
from functools import wraps, partial
import asyncio

# _executor = ThreadPoolExecutor()

def async_wrap(func):
    @wraps(func)
    async def run(*args, loop=None, executor=None, **kwargs):
        if loop is None:
            loop = asyncio.get_event_loop()
        pfunc = partial(func, *args, **kwargs)
        return await loop.run_in_executor(executor, pfunc)
    return run 

def async_class_wrap(cls):
    """
    Wrap all methods of a class to be run asynchronously if they are not async.
    """
    # Iterate over all attributes of the class
    for attr_name in dir(cls):
        # Get the attribute (method or function)
        attr = getattr(cls, attr_name)
        # Skip dunder methods (like __init__)
        if attr_name.startswith('__'):
            continue
        # Check if it's a method and not already async
        if callable(attr) and not asyncio.iscoroutinefunction(attr):
            # Wrap it in async_wrap
            wrapped_attr = async_wrap(attr)
            # Set the wrapped method back on the class
            setattr(cls, attr_name, wrapped_attr)
    
    return cls

def async_instance_wrap(instance):
    """
    Wrap all methods of an instance to run asynchronously if they are not already async.
    """
    # Iterate over all attributes of the instance
    for attr_name in dir(instance):
        # Get the attribute (method or function)
        try:
            attr = getattr(instance, attr_name)
            # Skip dunder methods (like __init__)
            
            if attr_name.startswith('__'):
                continue
            # Check if it's a method and not already async
            if callable(attr) and not asyncio.iscoroutinefunction(attr):
                # Wrap it in async_wrap
                wrapped_attr = async_wrap(attr)
                # Set the wrapped method back on the instance
                setattr(instance, attr_name, wrapped_attr)
        except:
            continue
    
    return instance


# # Pure async utility functions
# async def run_in_executor(func, *args, **kwargs):
#     """Run a CPU-bound function in a separate thread using async."""
#     loop = asyncio.get_running_loop()
#     return await loop.run_in_executor(_executor, func, *args, **kwargs)

# async def gather_with_concurrency(n, *tasks):
#     """Run tasks with a limit on concurrent execution."""
#     semaphore = asyncio.Semaphore(n)

#     async def sem_task(task):
#         async with semaphore:
#             return await task

#     return await asyncio.gather(*(sem_task(task) for task in tasks))

# async def async_retry(func, retries=3, delay=1, *args, **kwargs):
#     """Retries an async function on failure."""
#     for i in range(retries):
#         try:
#             return await func(*args, **kwargs)
#         except Exception as e:
#             if i == retries - 1:
#                 raise e
#             await asyncio.sleep(delay)

# def schedule_task(task_func, *args, delay=0, loop=None, **kwargs):
#     """Schedule a task to run after a delay."""
#     loop = loop or asyncio.get_event_loop()
#     return loop.call_later(delay, lambda: asyncio.create_task(task_func(*args, **kwargs)))

# async def run_async_with_threads(func, *args, **kwargs):
#     """Runs a CPU-bound task in a thread, from within an async context."""
#     loop = asyncio.get_running_loop()
#     return await loop.run_in_executor(_executor, func, *args, **kwargs)

# async def run_async_io_task(task_func, *args, **kwargs):
#     """Run an I/O-bound task asynchronously."""
#     return asyncio.create_task(task_func(*args, **kwargs))

# async def async_sleep_task(seconds):
#     """An example I/O-bound task simulating sleep."""
#     await asyncio.sleep(seconds)

# # Async Task Manager as Functions
# _tasks = []

# def add_task(coro):
#     """Add a new async task to the manager."""
#     task = asyncio.create_task(coro)
#     _tasks.append(task)

# async def await_all():
#     """Await all tasks managed by this instance."""
#     if _tasks:
#         await asyncio.gather(*_tasks)

# def cancel_all():
#     """Cancel all running tasks."""
#     for task in _tasks:
#         task.cancel()
