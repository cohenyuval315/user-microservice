
# threading.py
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
import queue

_executor = ThreadPoolExecutor()

# Pure functions for thread management
def run_in_thread(func, *args, **kwargs):
    """Runs a function in a separate thread."""
    thread = threading.Thread(target=func, args=args, kwargs=kwargs)
    thread.start()
    return thread

def run_in_thread_with_callback(func, callback, *args, **kwargs):
    """Runs a function in a separate thread and invokes a callback on completion."""
    def wrapper():
        result = func(*args, **kwargs)
        if callback:
            callback(result)
    thread = threading.Thread(target=wrapper)
    thread.start()
    return thread

def run_tasks_concurrently(tasks, max_workers=None):
    """Run multiple CPU-bound tasks concurrently using a thread pool."""
    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_tasks = {executor.submit(task): task for task in tasks}
        for future in as_completed(future_tasks):
            try:
                results.append(future.result())
            except Exception as e:
                results.append(e)
    return results

def run_cpu_heavy_task(task_func, *args, **kwargs):
    """Run a CPU-bound task in a separate thread pool."""
    return _executor.submit(task_func, *args, **kwargs)

# Task Queue Implementation as Functions
_task_queue = queue.Queue()
_workers = []
_worker_count = 4

def start_workers(worker_count=_worker_count):
    """Starts worker threads to process the queue."""
    global _workers
    for _ in range(worker_count):
        worker = threading.Thread(target=worker_loop)
        worker.daemon = True
        worker.start()
        _workers.append(worker)

def worker_loop():
    """Loop that workers run, executing tasks."""
    while True:
        func, args, kwargs = _task_queue.get()
        try:
            func(*args, **kwargs)
        except Exception as e:
            print(f"Error in task execution: {e}")
        _task_queue.task_done()

def add_task(func, *args, **kwargs):
    """Add a new task to the queue."""
    _task_queue.put((func, args, kwargs))

def wait_for_completion():
    """Wait for all tasks to complete."""
    _task_queue.join()

# Initialize workers on module load
start_workers()
