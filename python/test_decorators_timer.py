from decorators import *
import time
import sys

print("Testing timer()")
@timer
def test_func1():
    time.sleep(1)

test_func1()  # Exec time: ~1 second

@timer
def test_func2(a, b):
    time.sleep(2)
    return a + b

result = test_func2(3, 4)
print(result)  # Result: 7 Exec time: ~2 seconds

print("Testing timer_v2() with stdout")
@timer_v2()
def test_func1():
    time.sleep(1)

test_func1()  # Exec time: ~1 second

@timer_v2()
def test_func2(a, b):
    time.sleep(2)
    return a + b

result = test_func2(3, 4)
print(result)  # Result: 7 Exec time: ~2 seconds

print("Testing timer_v2() with file")
@timer_v2(output='test_out.txt')
def test_func1():
    time.sleep(1)

test_func1()  # Exec time: ~1 second

@timer_v2('test_out.log')
def test_func2(a, b):
    time.sleep(2)
    return a + b

result = test_func2(3, 4)
print(result)  # Result: 7 Exec time: ~2 seconds

@timer_v3(output = sys.stderr)
def foo_stderr(a, b):
    time.sleep(2)
    return a + b

result = foo_stderr(3, 4)
print("foo_stderr", result)  # Result: 7 Exec time: ~2 seconds

@timer_v3(output = sys.stdout)
def foo_stdout(a, b):
    time.sleep(2)
    return a + b

result = foo_stdout(3, 4)
print("foo_stdout", result)  # Result: 7 Exec time: ~2 seconds

@timer_v3(output = open('test_foo_file_out.txt', 'a'))
def foo_file(a, b):
    time.sleep(2)
    return a + b

result = foo_file(3, 4)
print("foo_file", result)  # Result: 7 Exec time: ~2 seconds


@timer_v3
def foo2(a, b):
    time.sleep(2)
    return a + b


result = foo2(3, 4)
print("foo2", result)  # Result: 7 Exec time: ~2 seconds
