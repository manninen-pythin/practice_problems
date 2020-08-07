import socket
import sys


class Connect:
    def __init__(self, ip, pt, d):
        self.address = (ip, int(pt))
        self.data = d.encode()

    def open_socket(self):
        with socket.socket() as client_socket:
            client_socket.connect(self.address)

            client_socket.send(self.data)

            response = client_socket.recv(1024)

            response = response.decode()
            print(response)


def main():
    args = sys.argv
    hostname = args[1]
    port = args[2]
    data = args[3]
    Connect(hostname, port, data).open_socket()


if __name__ == '__main__':
    main()

