from decorators import *
import time

print("Testing timer_decorator()")
@timer_decorator
def test_func1():
    time.sleep(1)

test_func1()  # Exec time: ~1 second

@timer_decorator
def test_func2(a, b):
    time.sleep(2)
    return a + b

result = test_func2(3, 4)
print(result)  # Result: 7 Exec time: ~2 seconds

print("Testing timer_decorator_v2() with stdout")
@timer_decorator_v2()
def test_func1():
    time.sleep(1)

test_func1()  # Exec time: ~1 second

@timer_decorator_v2()
def test_func2(a, b):
    time.sleep(2)
    return a + b

result = test_func2(3, 4)
print(result)  # Result: 7 Exec time: ~2 seconds

print("Testing timer_decorator_v2() with file")
@timer_decorator_v2(output='test_out.txt')
def test_func1():
    time.sleep(1)

test_func1()  # Exec time: ~1 second

@timer_decorator_v2('test_out.log')
def test_func2(a, b):
    time.sleep(2)
    return a + b

result = test_func2(3, 4)
print(result)  # Result: 7 Exec time: ~2 seconds
