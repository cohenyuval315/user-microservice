import threading
from functools import wraps

def thread_safe(fn):
    lock = threading.Lock()  # Create a lock

    @wraps(fn)
    def wrapper(*args, **kwargs):
        with lock:  # Acquire the lock before calling the function
            return fn(*args, **kwargs)

    return wrapper


