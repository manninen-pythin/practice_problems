import sys
import os
import requests
from bs4 import BeautifulSoup
from colorama import init, Fore


class TabOptions:

    def __init__(self, directory):
        self.pages = []
        self.page_index = -1
        self.dir = directory
        self.sites = {}

    def operate(self):
        while True:  # takes commands/ search terms and passes them to open page
            command = input()
            if command == 'exit':
                quit()
            if command == 'back':
                if self.page_index <= 0:
                    self.refresh()
                    continue
                else:
                    self.page_index -= 1
                    self.refresh()
                    continue
            if command == 'forward':
                if self.pages[self.page_index] != self.pages[-1]:
                    self.page_index += 1
                self.refresh()
                continue
            if command == 'refresh':
                self.refresh()
                continue
            self.open_page(command)

    def open_page(self, command):
        if "." in command:  # checks to see if program needs process a new search
            site_info = FetchData(command).parse_text()  # passes command to fetch data
            page_name = ''.join(command.rsplit(".", 1)[:-1])
            if site_info != 'Error':
                self.sites[page_name] = site_info  # if no error stores result in memory
                print(self.sites[page_name])
                if page_name not in self.pages:  # tab control
                    self.pages.append(page_name)
                    self.page_index += 1
                with open(f"{self.dir}\\{page_name}", "w") as opened_tab:
                    opened_tab.write(self.sites[page_name])
            return
        elif command in self.pages:
            with open(f"{self.dir}\\{command}", "r") as opened_tab:
                for line in opened_tab.readlines():
                    print(line)
            if self.pages[-1] != command:  # tab control
                self.pages.append(command)
                self.page_index += 1
            return
        print("Error: Incorrect URL")

    def refresh(self):
        if self.page_index == -1:
            self.operate()
        else:
            self.open_page(self.pages[self.page_index])


class FetchData:

    def __init__(self, request):
        self.request = request
        self.url = ''
        if not self.request.startswith('https://'):
            self.url = self.url.join(('https://', self.request))

    def parse_text(self):
        r = requests.get(self.url)
        if r.status_code == 200:
            soup = BeautifulSoup(r.content, 'html.parser')
            tags = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'ul', 'ol', 'li', 'a']
            page_info = soup.find_all(tags)
            parsed_text = ''
            for p in page_info:
                line = p.text
                if p.name == 'a':
                    line = Fore.BLUE + p.text
                parsed_text += line + '\n'
            return parsed_text
        else:
            return 'Error'


def main():
    init()
    dir_name = sys.argv[1]
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    tab = TabOptions(dir_name)
    tab.operate()


if __name__ == '__main__':
    main()
