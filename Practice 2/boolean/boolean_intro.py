print(15 > 10)
print(5 == 7)
print(3 < 1)

age = 19
print(age >= 18)
print(age < 16)

score = 88
print(score >= 90)
print(score >= 80)

temp = 82
if temp > 80:
  print("Hot day")
else:
  print("Mild day")

logged_in = True
if logged_in:
  print("Access granted")
else:
  print("Login required")

balance = 0
if balance > 0:
  print("Funds available")
else:
  print("Account empty")

print(bool("Code"))
print(bool(""))
print(bool("0"))

print(bool(100))
print(bool(-5))
print(bool(0))

items = ["pen", "notebook"]
empty = []
print(bool(items))
print(bool(empty))

print(bool("text"))
print(bool(42))
print(bool([1, 2]))
print(bool({"a": 1}))

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool([]))
print(bool({}))
print(bool(()))

def is_even(n):
  return n % 2 == 0

def is_valid(email):
  return "@" in email

print(is_even(4))
print(is_even(7))

if is_valid("user@test.com"):
  print("Valid email")
else:
  print("Invalid email")

x = 100
print(isinstance(x, int))
print(isinstance(x, str))

y = "hello"
print(isinstance(y, str))
print(isinstance(y, int))