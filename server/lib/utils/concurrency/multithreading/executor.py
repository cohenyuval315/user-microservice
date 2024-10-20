from concurrent.futures import ThreadPoolExecutor
import os 
from shared.singleton import SingletonMeta

class ThreadPoolExecutorManager(metaclass=SingletonMeta):
    max_scale = 5
    num_cores = os.cpu_count()
    
    def __init__(self) -> None:
        pass
    
    @classmethod
    def get_executor(cls):
        if cls._instance is None:
            cls._instance = ThreadPoolExecutor()
        return cls._instance

    def initialize(self):
        """Initialize the ThreadPoolExecutor."""
        if self._executor is None:
            self._executor = ThreadPoolExecutor(max_workers=os.cpu_count() * 5)
            
    def shutdown(self):
        self._executor.shutdown()
        
    def shutdown(self):
        self._executor.submit()
        
