import logging

# Налаштування конфігурації логування
logging.basicConfig(filename="logs.log", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Логування подій різного рівня (DEBUG, INFO, WARNING, ERROR, CRITICAL)



logging.debug('Це повідомлення рівня DEBUG') # 1
logging.info('Це повідомлення рівня INFO') # 2
logging.warning('Це повідомлення рівня WARNING') # 3
logging.error('Це повідомлення рівня ERROR') # 4
logging.critical('Це повідомлення рівня CRITICAL') # 5