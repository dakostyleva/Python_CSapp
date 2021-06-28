import pickle
import threading
import time
from socket import *


def send_message(socket):
    what_to_do = input('Choose what to do [(m) - write a message; (q) - quit]: ')
    if what_to_do == 'm':
        try:
            message = input('Enter your message: ')
            msg_json = {
                'action': 'message',
                'time': time.time(),
                'message': message,
            }
            socket.send(pickle.dumps(msg_json))
        except:
            return
    else:
        return


def receive_message(socket):
    data = pickle.loads(socket.recv(1024))
    server_response = data['alert']
    print(f'Message from chat: {server_response}')
    return server_response


def main():
    with socket(AF_INET, SOCK_STREAM) as sock:
        try:
            sock.connect(('localhost', 10000))
        except:
            return
        else:
            w_thread = threading.Thread(target=send_message, args=(sock,))
            w_thread.daemon = True
            w_thread.start()
            r_thread = threading.Thread(target=receive_message, args=(sock,))
            r_thread.daemon = True
            r_thread.start()
            while True:
                time.sleep(5)
                if w_thread.is_alive() and r_thread.is_alive():
                    continue
                break


if __name__ == '__main__':
    main()
