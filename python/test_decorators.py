from decorators import timer_decorator
import time

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