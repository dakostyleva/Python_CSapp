import pickle
import select
from socket import socket, AF_INET, SOCK_STREAM


def read_messages(r_clients, all_clients):
    messages = {}
    for sock in r_clients:
        try:
            data = pickle.loads(sock.recv(1024))
            messages[sock] = data['message']
        except:
            print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
            all_clients.remove(sock)

    return messages


def write_responses(requests, w_clients, all_clients):
    for i in w_clients:
        for sock in requests:
            try:
                response = requests[sock]
                msg_json = {
                    "response": 200,
                    "alert": response,
                }
                sock.send(pickle.dumps(msg_json))
            except:
                print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
            sock.close()
            all_clients.remove(sock)


def mainloop():
    address = ('', 10000)
    clients = []

    s = socket(AF_INET, SOCK_STREAM)
    s.bind(address)
    s.listen(5)
    s.settimeout(0.2)
    while True:
        try:
            conn, addr = s.accept()
        except:
            pass
        else:
            clients.append(conn)
        finally:
            wait = 10
            r = []
            w = []
            try:
                r, w, e = select.select(clients, clients, [], wait)
            except:
                pass
            requests = read_messages(r, clients)
            if requests:
                write_responses(requests, w, clients)


if __name__ == '__main__':
    mainloop()
    print('Эхо-сервер запущен!')
