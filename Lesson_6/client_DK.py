import datetime
import logging
import pickle
from socket import *
import log.client_log_config

logger = logging.getLogger('client_log')


def main():
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    new_socket = socket(AF_INET, SOCK_STREAM)
    new_socket.connect(('', 7777))
    msg = {
        "action": "presence",
        "time": current_time,
        "type": "status",
        "user": {
            "account_name": "John Doe",
            "status": "Online"
        }
    }
    new_socket.send(pickle.dumps(msg))
    logger.info('Message to server sent')
    data = new_socket.recv(1024)
    server_response = pickle.loads(data)
    logger.info(f'Server response: {server_response}')
    new_socket.close()


if __name__ == '__main__':
    main()
