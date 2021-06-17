from socket import *
import pickle
import sys
import argparse

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-p', default='7777')
    parser.add_argument ('-a', default='')
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
        print('Client message: ', pickle.loads(data))
        msg = {
                  "response": 200,
        }
        client.send(pickle.dumps(msg))
        client.close()


if __name__ == '__main__':
    main()