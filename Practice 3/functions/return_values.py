def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def sub(a, b):
    return a - b

def div(a, b):
    return a / b

def powr(a, b):
    return a ** b

print(add(2, 3))
print(mul(5, 4))
print(sub(10, 6))
print(div(20, 5))
print(powr(2, 3))


def no_ret(x):
    print(x)

def no_ret2(x):
    print(x * 2)

print(no_ret(5))
print(no_ret2(10))


def multi_values():
    return 1, 2, 3

a, b, c = multi_values()
print(a, b, c)


def return_list():
    return [1, 2, 3, 4, 5]

print(return_list())


def return_dict():
    return {"name": "Emil", "age": 25}

print(return_dict())


x = 10

def local_scope():
    x = 5
    print("Local x:", x)

def global_scope():
    global x
    x = 20
    print("Global x changed to:", x)

def nonlocal_scope():
    y = 2
    def inner():
        nonlocal y
        y += 3
        print("Inner y:", y)
    inner()
    print("Outer y:", y)

local_scope()
global_scope()
print("Global x now:", x)
nonlocal_scope()


def decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()


f1 = lambda x: x + 1
f2 = lambda x, y: x * y
f3 = lambda s: s.upper()

print(f1(5))
print(f2(3, 4))
print(f3("hello"))


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(factorial(5))
print(fibonacci(6))


def gen_numbers():
    for i in range(5):
        yield i

def gen_squares(n):
    for i in range(n):
        yield i ** 2

print(list(gen_numbers()))
print(list(gen_squares(5)))