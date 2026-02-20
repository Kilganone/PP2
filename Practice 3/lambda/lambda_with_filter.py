numbers = [1, 2, 3, 4, 5, 6, 7, 8]

odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
greater_than_four = list(filter(lambda x: x > 4, numbers))
less_equal_three = list(filter(lambda x: x <= 3, numbers))
divisible_by_three = list(filter(lambda x: x % 3 == 0, numbers))

print(odd_numbers)
print(even_numbers)
print(greater_than_four)
print(less_equal_three)
print(divisible_by_three)