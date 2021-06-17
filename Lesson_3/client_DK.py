from socket import *
import datetime
import pickle



def main():
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    new_socket = socket(AF_INET, SOCK_STREAM)
    new_socket.connect(('127.0.0.1', 7777))
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
    data = new_socket.recv(1024)
    print('Server response: ', pickle.loads(data))
    new_socket.close()


if __name__ == '__main__':
    main()