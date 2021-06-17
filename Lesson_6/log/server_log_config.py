import sys
import logging
import logging.handlers

# формат вывода
log_format = logging.Formatter('%(asctime)s %(levelname)s %(module)s %(message)s')

# обработчик, который выводит сообщения с уровнем CRITICAL в поток stderr
critical_handler = logging.StreamHandler(sys.stderr)
critical_handler.setLevel(logging.CRITICAL)
critical_handler.setFormatter(log_format)

# обработчик, который выводит сообщения в файл
file_log_handler = logging.FileHandler('server.log')
file_log_handler.setFormatter(log_format)

# регистратор верхнего уровня
log = logging.getLogger('server_log')
log.setLevel(logging.INFO)
log.addHandler(file_log_handler)
log.addHandler(critical_handler)

log_rotating = logging.handlers.TimedRotatingFileHandler('server_log', when='D', interval=1, backupCount=5)
log.addHandler(log_rotating)

if __name__ == '__main__':
    log.critical('Critical error')

