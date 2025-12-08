from pathlib import Path


# current_dir: Path = Path("/Users/milanstar/PycharmProjects/Hillel_aqa_2/lesson_16/")
current_dir = Path.cwd() # динамічно ініціалізує шлях до директорії файла
home_dir = Path.home()




repository_path: Path = current_dir.parent # на директорію вище
repository_name: str = repository_path.name # name of directory


# for path_obj in repository_path.iterdir():
#     if path_obj.is_file(): # чи це файл?
#         print(path_obj)
#
#
# for path_obj in repository_path.iterdir():
#     if path_obj.is_dir(): # чи це файл?
#         print(path_obj)


repository_files: list[Path] = [path_obj for path_obj in repository_path.iterdir() if path_obj.is_file()]
repository_directory: list[Path] = [path_obj for path_obj in repository_path.iterdir() if path_obj.is_dir()]

# --------------------------------------------------------------

lesson_11_path: Path = repository_path / "lesson_11"
temp_file_path: Path = lesson_11_path / "temp" / "temp2" / "temp_files"

# print(lesson_11_path)
# print(temp_file_path)


temp_file_path.mkdir(parents=True, # якщо не існує всіх директорій - то створити їх
                     exist_ok=True) # якщо існує - то не видавати помилку


custom_exceptions_11: Path = lesson_11_path / "custom_exceptions.py"
# print(custom_exceptions_11.exists())


all_python_files_in_repo: list[Path] = [obj for obj in repository_path.iterdir() if obj.is_file() and obj.suffix == ".py"]
# suffix - розширення файлу

for python_file in all_python_files_in_repo:
    print(python_file)












