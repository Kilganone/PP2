class MyClass1:
    x = 5

p1 = MyClass1()
print(p1.x)

class MyClass2:
    y = 10

p2 = MyClass2()
print(p2.y)

class MyClass3:
    z = 15

p3 = MyClass3()
print(p3.z)

class EmptyClass:
    pass

obj = EmptyClass()
print(obj)

class Person:
    name = "Alice"
    age = 25

p1 = Person()
p2 = Person()
p3 = Person()

print(p1.name, p1.age)
print(p2.name, p2.age)
print(p3.name, p3.age)