import time
from decorators import *

print("Testing cache_decorator() without limit size")
@cache_decorator()
def test_cache_unlim_size(a, b):
    time.sleep(3)
    return a * b

result = test_cache_unlim_size(3, 4)
print(result)  # 12

result = test_cache_unlim_size(3, 4)
print(result)  # 12 (cached - no sleep)

result = test_cache_unlim_size(5, 6)
print(result)  # 30

result = test_cache_unlim_size(5, 5)
print(result)  # 25

result = test_cache_unlim_size(5, 6)
print(result)  # 30 (cached - no sleep)

print("Testing cache_decorator() with cache max size = 1")

@cache_decorator(1)
def test_cache_max_size_1(a, b):
    time.sleep(3)
    return a * b


result = test_cache_max_size_1(3, 4)
print(result)  # 12

result = test_cache_max_size_1(3, 4)
print(result)  # 12 (cached - no sleep)

result = test_cache_max_size_1(5, 6)
print(result)  # 30

result = test_cache_max_size_1(5, 6)
print(result)  # 30 (cached - no sleep)

result = test_cache_max_size_1(3, 4)
print(result)  # 12 (not cached -- deleted in prev call)

result = test_cache_max_size_1(3, 4)
print(result)  # 12 (cached - no sleep)

