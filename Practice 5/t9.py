import re

text = input("Enter text: ")
result = re.sub(r'([A-Z])', r' \1', text).strip()
print(result)