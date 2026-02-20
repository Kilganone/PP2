numbers = [1, 2, 3, 4, 5]

doubled = list(map(lambda x: x * 2, numbers))
squared = list(map(lambda x: x ** 2, numbers))
plus_three = list(map(lambda x: x + 3, numbers))
negated = list(map(lambda x: -x, numbers))
half = list(map(lambda x: x / 2, numbers))

print(doubled)
print(squared)
print(plus_three)
print(negated)
print(half)