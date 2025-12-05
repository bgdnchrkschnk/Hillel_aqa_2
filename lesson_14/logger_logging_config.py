import logging
import logging.config

logging.config.fileConfig('logging_config.ini')

# Використання логера
sample_logger = logging.getLogger('sampleLogger')

sample_logger.debug('Це повідомлення рівня DEBUG')
sample_logger.info('Це повідомлення рівня INFO')