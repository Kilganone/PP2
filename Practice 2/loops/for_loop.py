fruits = ["apple", "banana", "cherry", "date", "elderberry"]
for fruit in fruits:
  print(fruit)

message = "Hello World"
for char in message:
  print(char)

for i in range(5):
  print(i)

for i in range(3, 8):
  print(i)

for i in range(0, 15, 3):
  print(i)

numbers = [2, 4, 6, 8, 10]
for num in numbers:
  print(f"{num} squared is {num * num}")

colors = ["red", "green", "blue"]
sizes = ["small", "medium", "large"]
for color in colors:
  for size in sizes:
    print(f"{color} {size}")

for i in range(4):
  print(f"Iteration {i}")
else:
  print("Loop finished successfully")

total = 0
for i in range(1, 6):
  total += i
print(f"Sum of 1 to 5: {total}")