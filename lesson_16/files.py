from pathlib import Path
from faker import Faker
fake = Faker()

current_dir = Path.cwd()
filename_write = "temp_file_write.txt"
filename_a = "temp_file_a.txt"
file_path = current_dir / filename_write

# file = open(file_path, "w")
# ...
# file.close()

# ---------------------------- mode "w" - перезапис файлу

with open(filename_write, mode="w") as file:
    file.write(f"Current path: {Path.cwd()}\n")

    file.write(fake.text())

# ---------------------------- mode "а" - НЕ перезаписувати файл

with open(filename_a, mode="a") as file:
    file.write(f"Current path: {Path.cwd()}\n")
    file.write(fake.text())

# ---------------------------- mode "r" - зчитування файлу

with open(filename_write, mode="r") as file:
    file_text: str = file.read() # зчитування всього файлу


# ---------------------------- mode "r" - зчитування файлу

with open(filename_write, mode="r") as file:
    file_text: list[str] = file.readlines()  # построчне зчитування

lines_of_file_text: list[str] = file_text
print(lines_of_file_text)
# ---------------------------- mode "r+" - зчитування + запис

with open("writelines.txt", mode="w") as file:
    file.writelines(lines_of_file_text)  # построчне зчитування
