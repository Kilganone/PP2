a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

number = 7
if number % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")

temperature = 22
if temperature > 30:
  print("It's hot outside!")
elif temperature > 20:
  print("It's warm outside")
else:
  print("It's cool or cold outside")

username = ""
if len(username) > 0:
  print(f"Welcome, {username}!")
else:
  print("Error: Username cannot be empty")

age = 16
if age >= 18:
  print("You can vote")
else:
  print("You cannot vote yet")

score = 65
if score >= 90:
  print("A")
elif score >= 80:
  print("B")
elif score >= 70:
  print("C")
else:
  print("F")

is_member = False
if is_member:
  print("Access granted")
else:
  print("Membership required")

balance = 0
if balance > 0:
  print("Withdraw funds")
else:
  print("Insufficient funds")