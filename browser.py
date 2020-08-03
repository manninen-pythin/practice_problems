import sys
import os

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.'''

sites = {'bloomberg.com': bloomberg_com, 'nytimes.com': nytimes_com}


class TabOptions:

    def __init__(self, directory):
        self.pages = []
        self.page_index = -1
        self.dir = directory

    def operate(self):
        while True:
            command = input()
            print(self.pages)
            print(self.page_index)
            if command == 'exit':
                exit()
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
        if "." in command:
            if command in sites:
                print(sites[command])
                page_name = ''.join(command.split(".")[:-1])
                if page_name not in self.pages:
                    self.pages.append(page_name)
                    self.page_index += 1
                with open(f"{self.dir}\\{page_name}", "w") as opened_tab:
                    opened_tab.write(sites[command])
                return
        if command in self.pages:
            with open(f"{self.dir}\\{command}", "r") as opened_tab:
                for line in opened_tab.readlines():
                    print(line)
            if self.pages[-1] != command:
                self.pages.append(command)
                self.page_index += 1
            return
        print("Error: Incorrect URL")

    def refresh(self):
        if self.page_index == -1:
            self.operate()
        else:
            self.open_page(self.pages[self.page_index])


dir_name = 'tb_tabs'
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
tab = TabOptions(dir_name)
tab.operate()
