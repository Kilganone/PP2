import shutil
import os

# Копирование
shutil.copy("sample.txt", "backup.txt")

# Удаление (безопасно)
if os.path.exists("backup.txt"):
    os.remove("backup.txt")
    print("File deleted")
else:
    print("File not found")