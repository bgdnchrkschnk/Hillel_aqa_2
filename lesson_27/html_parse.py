from bs4 import BeautifulSoup
import requests

# Завантаження HTML-сторінки
url = 'https://demo.automationtesting.in/Index.html'
response = requests.get(url)
html_content = response.content

# Аналіз HTML-документу з використанням BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Вилучення тексту з тегу <title> за допомогою CSS-локатора
title = soup.select_one('#btn1').text
print("Button text:", title, "\n")

# Вилучення тексту з усіх тегів <a> за допомогою CSS-локатора
links: list = soup.select('a')
for link in links:
    print("Посилання:", link.get('href'))