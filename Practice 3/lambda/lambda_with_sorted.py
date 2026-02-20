students = [("Emil", 25), ("Tobias", 22), ("Linus", 28), ("Anna", 24)]
words = ["apple", "pie", "banana", "cherry", "kiwi"]

sorted_by_age = sorted(students, key=lambda x: x[1])
sorted_by_name = sorted(students, key=lambda x: x[0])
sorted_words_len = sorted(words, key=lambda x: len(x))
sorted_words_alpha = sorted(words)
sorted_by_last_char = sorted(words, key=lambda x: x[-1])

print(sorted_by_age)
print(sorted_by_name)
print(sorted_words_len)
print(sorted_words_alpha)
print(sorted_by_last_char)