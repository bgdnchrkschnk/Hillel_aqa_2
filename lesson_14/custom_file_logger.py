import logging



# # Створення логера
logger = logging.getLogger("custom_file_logger")

# Налаштування рівня логування
logger.setLevel(logging.DEBUG)


# --------------------------------------
# Створення обробника для запису в файл
file_handler = logging.FileHandler('custom_file_logs.log')
# Налаштування рівня логування для обробника
file_handler.setLevel(logging.DEBUG)
# Створення форматера для обробника
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s - %(name)s - %(filename)s - %(lineno)d - %(funcName)s')
file_handler.setFormatter(file_formatter)



# --------------------------------------
# Створення обробника для виводу в stdout
console_handler = logging.StreamHandler()
# Налаштування рівня логування для обробника
console_handler.setLevel(logging.INFO)
# Створення форматера для обробника
console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)



# --------------------------------------
# Додавання обробника до логера
logger.addHandler(console_handler)
# Додавання обробника до логера
logger.addHandler(file_handler)
