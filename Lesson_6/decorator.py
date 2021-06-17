import logging
import log.server_log_config
import log.client_log_config

logger = logging.getLogger('server_log')


def log(function):
    def log_call(*args, **kwargs):
        function_call = function(*args, **kwargs)
        logger.info(f'Функция {function.__name__} вызвана из функции main')
        return function_call
    return log_call
