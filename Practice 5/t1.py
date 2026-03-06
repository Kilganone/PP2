import re

text = input("Enter text: ")
pattern = r'ab*'
matches = re.findall(pattern, text)
print(matches)