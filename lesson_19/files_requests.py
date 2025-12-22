import requests



# UPLOAD FILE

# Відкриття файлу для завантаження
with open('../requirements.txt', 'rb') as file:
    files = {'file': file}

    # Виконання POST-запиту з файлом
    response = requests.post('https://example.com/upload', files=files)

# # Обробка відповіді
# print(response.text)

# ---------------------------

import requests

# Виконання GET-запиту для скачування файлу
response = requests.get('https://sitechecker.pro/wp-content/uploads/2023/09/what-are-url-parameters.png')

# Запис файлу на диск
with open('test_image_download.png', 'wb') as file:
    file.write(response.content)