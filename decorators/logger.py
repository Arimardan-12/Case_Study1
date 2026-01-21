import functools
import datetime


def log_execution(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] {func.__name__} executed at {datetime.datetime.now()}")


        return func(*args, **kwargs)
    return wrapper
