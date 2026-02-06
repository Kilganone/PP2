x = 5
y = 3
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

a = 10
b = 20
print(a < b and b > 15)
print(a > b or b == 20)
print(not(a == b))

temp = 75
print(temp > 70 and temp < 80)
print(temp < 60 or temp > 90)

score = 85
if score >= 90:
  print("A")
elif score >= 80:
  print("B")
else:
  print("C")

list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]
print(list1 is list2)
print(list1 is list3)
print(list1 == list3)

user = None
print(user is None)
print(user is not None)

name = "Python"
print(name is "Python")

fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)
print("mango" not in fruits)

text = "Hello World"
print("Hello" in text)
print("Python" not in text)

numbers = [1, 2, 3, 4, 5]
print(3 in numbers)
print(10 not in numbers)

allowed = "abc123"
print("a" in allowed)
print("z" not in allowed)

age = 25
print(age >= 18 and age <= 65)
print(not(age < 18))