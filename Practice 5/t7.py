import re

text = input("Enter snake_case string: ")
result = re.sub(r'_([a-z])', lambda m: m.group(1).upper(), text)
print(result)