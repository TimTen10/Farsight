import functools
import time


# simple decorator to time individual functions
def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        stop_time = time.perf_counter()
        time_needed = stop_time - start_time
        print(f"{func.__name__!r} finished in {time_needed:0.4f} seconds")
        return value
    return wrapper_timer


# simple decorator for debugging that can also be used for logging
def debug(func):
    @functools.wraps(func)
    def wrapper_logging(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} called with {signature} returned {value!r}")
        return value
    return wrapper_logging
