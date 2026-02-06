fruits = ["apple", "banana", "cherry", "date", "elderberry"]
for fruit in fruits:
  if fruit == "cherry":
    continue
  print(fruit)

print("\nSkip even numbers:")
for i in range(10):
  if i % 2 == 0:
    continue
  print(i)

text = "Programming"
for char in text:
  if char in "aeiou":
    continue
  print(char)

print("\nSkip specific items:")
shopping_cart = ["laptop", "mouse", "cable", "monitor", "keyboard"]
for item in shopping_cart:
  if item == "cable":
    print(f"Skipping {item} (out of stock)")
    continue
  print(f"Processing {item}")

print("\nContinue with nested loop:")
for i in range(3):
  for j in range(3):
    if j == 1:
      continue
    print(f"i={i}, j={j}")

numbers = [1, -2, 3, -4, 5, -6]
for num in numbers:
  if num < 0:
    print(f"Skipping negative: {num}")
    continue
  print(f"Processing positive: {num}")