import re

text = input("Enter text: ")
pattern = r'a.*b$'
matches = re.findall(pattern, text)
print(matches)