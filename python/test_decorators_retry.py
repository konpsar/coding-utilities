from decorators import retry_decorator

print("Testing retry_decorator()")
@retry_decorator(tries=3)
def successful_func():
    print("Success")

successful_func()

@retry_decorator(tries=3)
def zeroDivErrorfunction():
    return 1/0

zeroDivErrorfunction()

@retry_decorator(tries=3)
def failed_func():
    raise ValueError("Failed")

failed_func()

# --------------------

print("Testing retry_decorator() with delay")
@retry_decorator(tries=3, delay=1)
def successful_func():
    print("Success")

successful_func()

@retry_decorator(tries=3, delay=1)
def zeroDivErrorfunction():
    return 1/0

zeroDivErrorfunction()

@retry_decorator(tries=3, delay=1)
def failed_func():
    raise ValueError("Failed")

failed_func()

# --------------------

print("Testing retry_decorator() with delay and backoff")
@retry_decorator(tries=3, delay=1, backoff=2)
def successful_func():
    print("Success")

successful_func()

@retry_decorator(tries=3, delay=1, backoff=2)
def zeroDivErrorfunction():
    return 1/0

zeroDivErrorfunction()

@retry_decorator(tries=3, delay=1, backoff=2)
def failed_func():
    raise ValueError("Failed")

failed_func()