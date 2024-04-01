import time
from decorators import *

print("Testing cache_decorator()")
@cache_decorator
def test_func3(a, b):
    time.sleep(3)
    return a * b

result = test_func3(3, 4)
print(result)  # 12

result = test_func3(3, 4)
print(result)  # 12 (cached - no sleep)

result = test_func3(5, 6)
print(result)  # 30

