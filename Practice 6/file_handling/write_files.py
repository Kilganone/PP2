with open("sample.txt", "w") as f:
    f.write("Hello, world!\n")
    f.write("This is a test file.\n")

with open("sample.txt", "a") as f:
    f.write("Appended line.\n")