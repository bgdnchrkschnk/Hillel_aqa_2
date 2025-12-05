import logging

# Налаштування конфігурації логування
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s')

# Додавання обробника для виводу в консоль
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
logging.getLogger('').addHandler(console_handler)
#
# Логування подій різного рівня
logging.debug('Це повідомлення рівня DEBUG')
logging.info('Це повідомлення рівня INFO')
logging.warning('Це повідомлення рівня WARNING')
logging.error('Це повідомлення рівня ERROR')
logging.critical('Це повідомлення рівня CRITICAL')