import re

text = input("Enter text: ")
pattern = r'[A-Z][a-z]+'
matches = re.findall(pattern, text)
print(matches)