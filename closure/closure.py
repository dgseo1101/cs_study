# case 1
def outer_function():
    x = 10 # 지역 변수
    return x

print(outer_function()) # 여기선 더이상 x에 접근 불가.

# case 2
def make_adder(n):
    def adder(x):
        return x + n
    return adder

add_10 = make_adder(10) # 여기서 n = 10
add_20 = make_adder(20) # 여기서 n = 20

print(add_10(5)) # 15
print(add_20(5)) # 25

print(add_10.__closure__) # <cell at 0x000002026B574240: int object at 0x000002026B574240>
print(add_10.__closure__[0].cell_contents) # 10
print(add_20.__closure__[0].cell_contents) # 20


# case 3
def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

counter1 = make_counter()
counter2 = make_counter()

print(counter1()) # 1
print(counter1()) # 2
print(counter1()) # 3

print(counter2()) # 1
print(counter2()) # 2
print(counter2()) # 3

# case 4 (decorator)
import time

def timing(fn):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = fn(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken: {end_time - start_time} seconds")
        return result
    return wrapper

@timing
def slow_function():
    time.sleep(1)
    print("Slow function executed")

slow_function()

print(slow_function.__name__) # wrapper
print(slow_function.__doc__) # None
print(slow_function.__module__) # __main__
print(slow_function.__dict__) # {}
print(slow_function.__closure__) # (<cell at 0x000001B8F17577C0: function object at 0x000001B8F177BF60>,)
print(slow_function.__closure__[0].cell_contents) # <function slow_function at 0x000001B8F177BF60>

# case 5
funcs = []

for i in range(3):
    def f():
        print(i)
    funcs.append(f)

# 기대: 0, 1, 2
# 실제:
funcs[0]()  # 2
funcs[1]()  # 2
funcs[2]()  # 2

# case 6
class Counter:
    def __init__(self):
        self.count = 0

    def inc(self):
        self.count += 1
        return self.count

c1 = Counter()
c2 = Counter()

print(c1.inc())  # 1
print(c1.inc())  # 2
print(c2.inc())  # 1
