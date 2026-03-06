import re

text = input("Enter text: ")
pattern = r'[a-z]+_[a-z]+'
matches = re.findall(pattern, text)
print(matches)