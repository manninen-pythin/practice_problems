import socket
import sys
import itertools
import string


class Connect:
    def __init__(self, ip, pt):
        self.address = (ip, int(pt))
        self.items = string.ascii_letters + string.digits

    def open_socket(self):
        with socket.socket() as client_socket:
            client_socket.connect(self.address)
            passwords = self.gen_password()
            for password in passwords:
                client_socket.send(password.encode())
                response = client_socket.recv(1024).decode()
                if response == 'Connection success!':
                    print('Found!')
                    print(password)
                    break
                if response == 'Too many attempts':
                    print('Too many attempts!')
                    break

    def gen_password(self):
        for i in itertools.count(1):
            for c in itertools.product(self.items, repeat=i):
                yield ''.join(c)


def main():
    args = sys.argv
    hostname = args[1]
    port = args[2]
    Connect(hostname, port).open_socket()


if __name__ == '__main__':
    main()


