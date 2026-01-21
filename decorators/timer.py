import time
import functools


def performance_timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"[TIMER] {func.__name__} took {time.time() - start:.4f}s")
        return result
    return wrapper
