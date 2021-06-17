from socket import *
import pickle
import sys
import argparse
import logging
import log.server_log_config
from decorator import log

logger = logging.getLogger('server_log')

@log
def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', default='7777')
    parser.add_argument('-a', default='')
    return parser


def main():
    parser = createParser()
    port = parser.parse_args(sys.argv[1:])
    new_socket = socket(AF_INET, SOCK_STREAM)
    new_socket.bind((str(port.a), int(port.p)))
    new_socket.listen(3)

    while True:
        client, address = new_socket.accept()
        data = client.recv(1024)
        logger.info('data received')
        client_message = pickle.loads(data)
        logger.info(f'Server response: {client_message}')
        msg = {
            "response": 200,
        }
        client.send(pickle.dumps(msg))
        client.close()


if __name__ == '__main__':
    main()
