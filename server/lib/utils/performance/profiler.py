import cProfile
import pstats
import time
import line_profiler
import memory_profiler
import functools
import io
import asyncio
import threading
from lib.common.loggers import logger
from typing import Optional, Callable, Any,List
import sys
import os


class Profiler:
    """
    A generic profiler class using cProfile to profile Python code.

    Provides decorators for setup and profiling test functions,
    and a main method to execute profiling runs.
    """


    def __init__(self, name: str, num: int):
        """
        Initializes the Profiler.

        Args:
            name (str): The base name for profiling output files.
            num (int): The number of iterations for the tests.
            filename (Optional[str]): If provided, the profiling stats will be saved to this file.
            sort (str): The sorting method for the statistics (default: 'cumulative').
            
        """
        self.name = name
        self.num = num
        self.test_functions: List[Callable] = []
        self.setup_function: Optional[Callable] = None

    @classmethod
    def init(cls, name: str, num: int = 10000) -> 'Profiler':
        """
        Class method to initialize a Profiler instance.

        Args:
            name (str): The base name for profiling output files.
            num (int): The number of iterations for the tests.

        Returns:
            Profiler: An instance of Profiler.
        """
        return cls(name, num)

    def setup(self, func: Callable) -> Callable:
        """
        Decorator to designate a setup function.

        Args:
            func (Callable): The setup function to be profiled.

        Returns:
            Callable: The wrapped setup function.
        """
        self.setup_function = func

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Running setup: {func.__name__}")
            return func(*args, **kwargs)

        return wrapper


    def profile(self, func: Callable) -> Callable:
        """
        Decorator to profile a test function.

        Args:
            func (Callable): The test function to be profiled.

        Returns:
            Callable: The wrapped test function with profiling.
        """
        self.test_functions.append(func)

        if asyncio.iscoroutinefunction(func):
            @functools.wraps(func)
            async def async_wrapper(*args, **kwargs):
                profiler = cProfile.Profile()
                profiler.enable()
                try:
                    print(f"Profiling async function: {func.__name__}")
                    return await func(*args, **kwargs)
                finally:
                    profiler.disable()
                    self._print_stats(profiler, func.__name__)
                    self._save_stats(profiler, func.__name__)
            return async_wrapper
        else:
            @functools.wraps(func)
            def sync_wrapper(*args, **kwargs):
                profiler = cProfile.Profile()
                profiler.enable()
                try:
                    logger.info(f"Profiling function: {func.__name__}")
                    return func(*args, **kwargs)
                finally:
                    profiler.disable()
                    self._print_stats(profiler, func.__name__)
                    self._save_stats(profiler, func.__name__)
            return sync_wrapper
        
    def _print_stats(self, profiler: cProfile.Profile, func_name: str):
        """
        Prints the profiling statistics to the console.

        Args:
            profiler (cProfile.Profile): The profiler instance.
            func_name (str): The name of the profiled function.
        """
        s = io.StringIO()
        ps = pstats.Stats(profiler, stream=s).sort_stats('cumulative')
        ps.print_stats(30)  # Print top 30 lines
        logger.info(f"\nProfiling results for {func_name}:\n{s.getvalue()}")


    def _save_stats(self, profiler: cProfile.Profile, func_name: str):
        """
        Saves the profiling statistics to a file.

        Args:
            profiler (cProfile.Profile): The profiler instance.
            func_name (str): The name of the profiled function.
        """
        filename = f"{self.name}_{func_name}.prof"
        profiler.dump_stats(filename)
        logger.info(f"Profiling stats saved to {filename}\n")

    # def main(self):
    #     """
    #     Executes the setup and all test functions with profiling.
    #     """
    #     if self.setup_function is None:
    #         logger.info("No setup function defined. Exiting.")
    #         sys.exit(1)

    #     self.setup_function()
    #     for test_func in self.test_functions:
    #         if asyncio.iscoroutinefunction(test_func):
    #             asyncio.run(test_func(self.num))
    #         else:
    #             test_func(self.num)