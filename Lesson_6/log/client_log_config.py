import logging
import sys
import os

# формат вывода
log_format = logging.Formatter('%(asctime)s %(levelname)s %(module)s %(message)s')

# обработчик, который выводит сообщения с уровнем CRITICAL в поток stderr
critical_handler = logging.StreamHandler(sys.stderr)
critical_handler.setLevel(logging.CRITICAL)
critical_handler.setFormatter(log_format)

# обработчик, который выводит сообщения в файл
file_log_handler = logging.FileHandler('client.log')
file_log_handler.setFormatter(log_format)

# регистратор верхнего уровня
log = logging.getLogger('client_log')
log.setLevel(logging.INFO)
log.addHandler(file_log_handler)
log.addHandler(critical_handler)

if __name__ == '__main__':
    log.critical('Critical error')
    log.info('info')
