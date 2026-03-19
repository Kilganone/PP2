with open("sample.txt", "r") as f:
    content = f.read()
    print(content)

with open("sample.txt", "r") as f:
    for line in f:
        print(line.strip())