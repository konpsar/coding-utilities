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