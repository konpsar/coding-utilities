import time
from decorators import cache, cache_deque, cache_deque_cyclical

print("Testing cache() without limit size")
@cache()
def test_cache_unlim_size(a, b):
    time.sleep(1)
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

print("Testing cache() with cache max size = 1")

@cache(1)
def test_cache_max_size_1(a, b):
    time.sleep(1)
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


print("Testing cache() args, kwars")
@cache(5)
def foo(x: float, y: float) -> float:
    return x + y

foo(1, y=1)   # not cached --> result: 2
foo(1, y=9)   # not cached --> result: 10
foo(x=1, y=9) # not cached --> result: 10
foo(1, 1)   # not cached --> result: 2
foo(1, y=1)   # cached --> result: 2
foo.clear_cache()
foo(1, y=1)   # not cached --> result: 2


print("Testing cache_deque() args, kwars")
@cache_deque(5)
def foo(x: float, y: float) -> float:
    return x + y

foo(1, y=1)   # not cached --> result: 2
foo(1, y=9)   # not cached --> result: 10
foo(x=1, y=9) # not cached --> result: 10
foo(1, 1)   # not cached --> result: 2
foo(1, y=1)   # cached --> result: 2
foo.clear_cache()
foo(1, y=1)   # not cached --> result: 2


print("Testing cache_deque_cyclical() args, kwars")
@cache_deque_cyclical(size=3)
def foo(x: float, y: float) -> float:
    return x + y

foo(1, y=1)   # not cached --> result: 2
foo(1, y=9)   # not cached --> result: 10
foo(x=1, y=9) # not cached --> result: 10
foo(1, 1)   # not cached --> result: 2
foo(1, y=1)   # cached --> result: 2
foo(2, y=1)   # cached --> result: 2
foo.clear()
foo(1, y=1)   # not cached --> result: 2
foo(1, y=1)   # not cached --> result: 2
