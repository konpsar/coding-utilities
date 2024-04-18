from decorators import retry

print("Testing retry()")
@retry(tries=3)
def successful_func():
    print("Success")

successful_func()

@retry(tries=3)
def zero_div_error_function():
    return 1/0

zero_div_error_function()

@retry(tries=3)
def failed_func():
    raise ValueError("Failed")

failed_func()

# --------------------

print("Testing retry() with delay")
@retry(tries=3, delay=1)
def successful_func():
    print("Success")

successful_func()

@retry(tries=3, delay=1)
def zeroDivErrorfunction():
    return 1/0

zeroDivErrorfunction()

@retry(tries=3, delay=1)
def failed_func():
    raise ValueError("Failed")

failed_func()

# --------------------

print("Testing retry() with delay and backoff")
@retry(tries=3, delay=1, backoff=2)
def successful_func():
    print("Success")

successful_func()

@retry(tries=3, delay=1, backoff=2)
def zeroDivErrorfunction():
    return 1/0

zeroDivErrorfunction()

@retry(tries=3, delay=1, backoff=2)
def failed_func():
    raise ValueError("Failed")

failed_func()