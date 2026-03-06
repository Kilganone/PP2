import re

text = input("Enter text: ")
pattern = r'ab{2,3}'
matches = re.findall(pattern, text)
print(matches)