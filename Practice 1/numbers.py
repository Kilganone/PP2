x = 42.9
print(type(x))
y = int(x)
print(type(y))

z = 10j
print(type(z))

x = 7
y = 98765432123456789
z = -123456

print(type(x))
print(type(y))
print(type(z))

x = 3.14
y = 0.5
z = -99.99

print(type(x))
print(type(y))
print(type(z))

x = 9e2
y = 4E3
z = -12.5e50

print(type(x))
print(type(y))
print(type(z))

x = 2+8j
y = 12j
z = -3j

print(type(x))
print(type(y))
print(type(z))

x = 5     # int
y = 6.7   # float
z = 2j    # complex

# convert from int to float:
a = float(x)

# convert from float to int:
b = int(y)

# convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

import random

print(random.randrange(5, 15))
print(random.randrange(10, 201))  # from 10 to 200
