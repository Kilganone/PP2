a = 5
b = 2
if a > b: print("a is greater than b")

a = 2
b = 330
print("A") if a > b else print("B")

a = 10
b = 20
bigger = a if a > b else b
print(bigger)

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

x = 15
y = 20
max_value = x if x > y else y
print(max_value)

username = ""
display_name = username if username else "Guest"
print(display_name)

age = 17
status = "adult" if age >= 18 else "minor"
print(status)

score = 85
grade = "Pass" if score >= 60 else "Fail"
print(grade)

temp = 25
weather = "hot" if temp > 30 else "warm" if temp > 20 else "cool"
print(weather)

is_member = True
price = 10 if is_member else 20
print(price)

count = 0
message = "items" if count != 1 else "item"
print(message)

x = 7
result = "even" if x % 2 == 0 else "odd"
print(result)

balance = 50
action = "withdraw" if balance > 0 else "deposit"
print(action)