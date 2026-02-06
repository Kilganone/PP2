fruits = ["apple", "banana", "cherry", "mango", "orange"]
for fruit in fruits:
  print(fruit)
  if fruit == "cherry":
    break

print("\nBreak before print:")
for fruit in fruits:
  if fruit == "cherry":
    break
  print(fruit)

for i in range(10):
  print(i)
  if i == 6:
    break

users = ["alice", "bob", "admin", "charlie"]
for user in users:
  print(f"Checking {user}")
  if user == "admin":
    print("Admin found - stopping search")
    break

for i in range(1, 11):
  if i * i > 50:
    print(f"Stopping at {i} because {i}² = {i*i} > 50")
    break
  print(i)

print("\nBreak with else (else won't execute):")
for i in range(5):
  print(i)
  if i == 3:
    break
else:
  print("This won't print because of break")