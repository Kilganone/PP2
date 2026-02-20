x1 = lambda a: a + 5
x2 = lambda a, b: a * b
x3 = lambda a, b, c: a + b - c
x4 = lambda s: s.upper()
x5 = lambda s: s[::-1]

print(x1(10))
print(x2(4, 5))
print(x3(10, 5, 3))
print(x4("hello"))
print(x5("Python"))