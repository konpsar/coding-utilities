import time
from typing import Protocol
import sys
from collections import deque

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
        msg = f"Execution time: {execution_time:2.3f} seconds"
        try:
            output.write(msg+'\n')
        except AttributeError:
            print("Given output does not have a write method.")
            print(msg)
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
        wrapper.clear_cache = cache.clear
        return wrapper
    return decorator


def cache_deque(size: int = None):
    cache_keys = deque()
    cache_values = deque()
    def decorator(func):
        def wrapper(*args, **kwargs):
            key = tuple(args)
            if kwargs:
                key += tuple(kwargs.items())
            print(f"---> Current cache (start): {list(zip(cache_keys, cache_values))}")
            if key in cache_keys:
                index = cache_keys.index(key)
                value = cache_values[index]
                cache_keys.remove(key)
                cache_keys.append(key)
                cache_values.remove(value)
                cache_values.append(value)
            else:
                if size and len(cache_keys) >= size:
                    cache_keys.popleft()
                    cache_values.popleft()
                value = func(*args, **kwargs)
                cache_keys.append(key)
                cache_values.append(value)
            return value

        def clear_cache():
            cache_keys.clear()
            cache_values.clear()

        wrapper.clear_cache = clear_cache

        return wrapper
    return decorator



def cache_deque_cyclical(_func = None, *, size: int = None):
    if not _func:
        return lambda func: cache_deque_cyclical(func, size=size)
    
    cache = deque(maxlen=size)
    def wrapper(*args, **kwargs):
        key = tuple(args)
        if kwargs:
            key += tuple(kwargs.items())
        print(f"---> Current cache (start): {cache}")
        for (k,v) in cache:
            if k == key:
                cache.remove((k,v))
                cache.append((k,v))
                return v
        value = _func(*args, **kwargs)
        cache.append((key, value))
        return value
    
    wrapper.clear = cache.clear

    return wrapper

def retry_draft(tries: int, delay: int = 0, backoff: int = 1):
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

def retry(_func=None, *, tries: int, delay: int = 0, backoff: int = 1):
    if _func is None:
        return lambda func: retry(func, tries=tries, delay=delay, backoff=backoff)
    
    def wrapper(*args, **kwargs):
        for t in range(max(tries-1, 0)):
            try:
                print(f"Run {t}")
                return _func(*args, **kwargs)
            except Exception as e:
                print(f"Exception: {e}")
                actual_delay = delay * max(backoff * t, 1)
                print(f"Attempt {t+1} failed. Retrying in {actual_delay} seconds.")
                time.sleep(actual_delay)
        return _func(*args, **kwargs) # last attempt -- No exception handling
    return wrapper