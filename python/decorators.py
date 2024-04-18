import time
from typing import Protocol
import sys

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        try:
            result = func(*args, **kwargs)
        except Exception:
            raise 
        else:
            return result # if not exception is raised
        finally:                       
            end_time = time.perf_counter()
            execution_time = end_time - start_time
            print(f"Execution time: {execution_time} seconds")
    return wrapper


def timer_v2(output: str = 'stdout'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            execution_time = end_time - start_time
            if output == 'stdout':
                print(f"Execution time: {execution_time} seconds")
            elif output.endswith('.txt') or output.endswith('.log'):
                with open(output, 'a') as file:
                    file.write(f"Execution time: {execution_time} seconds\n")
            return result
        return wrapper
    return decorator

class Writable(Protocol):
    def write(self, s: str) -> None: 
        '''Implement write method'''

def timer_v3(_func=None, *, output: Writable = sys.stdout):
    if _func is None: # guard clause
        return lambda func: timer_v3(func, output=output)

    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = _func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        output.write(f"Execution time: {execution_time} seconds\n")
        return result
    return wrapper

def cache(size: int = None):
    cache = {}
    def decorator(func):
        def wrapper(*args, **kwargs):
            key = tuple(args)
            if kwargs:
                key += tuple(kwargs.items())
            print(f"---> Current cache (start): {cache}")
            print(f"------> Cached value for args: {key}: {cache.get(key, 'Not cached')}")
            if key not in cache:
                if size and len(cache) >= size:
                    cache.popitem()
                cache[key] = func(*args, **kwargs)
            print(f"---------> Current cache (end): {cache}")
            return cache[key]
        return wrapper
    return decorator

def retry(tries: int, delay: int = 0, backoff: int = 1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for t in range(max(tries-1, 0)):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Exception: {e}")
                    actual_delay = delay * max(backoff * t, 1)
                    print(f"Attempt {t+1} failed. Retrying in {actual_delay} seconds.")
                    time.sleep(actual_delay)
            return func(*args, **kwargs) # last attempt -- No exception handling
        return wrapper
    return decorator