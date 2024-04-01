import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time} seconds")
        return result
    return wrapper


def timer_decorator_v2(output='stdout'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time
            if output == 'stdout':
                print(f"Execution time: {execution_time} seconds")
            elif output.endswith('.txt') or output.endswith('.log'):
                with open(output, 'a') as file:
                    file.write(f"Execution time: {execution_time} seconds\n")
            return result
        return wrapper
    return decorator

def cache_decorator(size=None):
    cache = {}
    def decorator(func):
        def wrapper(*args, **kwargs):
            key = args
            print(f"---> Current cache (start): {cache}")
            print(f'------> Cached value for args: {key}: {cache.get(key, 'Not cached')}')
            if key not in cache:
                if size and len(cache) >= size:
                    cache.popitem()
                cache[key] = func(*args, **kwargs)
            print(f"---------> Current cache (end): {cache}")
            return cache[key]
        return wrapper
    return decorator

def retry_decorator(tries=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(tries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Exception: {e}")
            return None
        return wrapper
    return decorator