import random


class RockPaperScissors:

    def __init__(self):

        self.choice = None
        self.choice_list = ["paper", "rock", "scissors"]
        self.lose = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
        self.name = None

    def user_entry(self):

        print('What is your name? ')
        self.name = str(input())
        print('Hello, ' + self.name)
        rating_file = open('ratings.txt')
        print(rating_file.read())
        rating_file.close()
        read = ReadWrite(self.name)
        read.rating_lookup()

    def game_entry(self):

        approved = False
        print('Choose rock, paper, scissors, !rating, or !exit:')
        self.choice = str(input())
        for choice in self.choice_list:
            if choice == self.choice:
                approved = True
        if self.choice == '!exit':
            print('Bye!')
            quit()
        elif self.choice == '!rating':
            read = ReadWrite(self.name)
            read.rating_lookup()
        elif approved is False:
            print('Invalid input')
        else:
            shoot.jajanken()

    def jajanken(self):
        write = ReadWrite(self.name)
        comp = random.choice(self.choice_list)
        if self.choice == self.lose[comp]:
            print('Sorry, but computer chose {}'.format(comp))
            shoot.game_entry()
        elif comp == self.choice:
            print('There is a draw ({})'.format(comp))
            result = 'draw'
            write.write_score(self.name, result)
            shoot.game_entry()
        else:
            print('Well done. Computer chose {} and failed'.format(comp))
            result = 'win'
            write.write_score(self.name, result)
            shoot.game_entry()


class ReadWrite:

    def __init__(self, name):
        self.name = name

    def rating_lookup(self):
        rating_file = open('ratings.txt')
        name_list = []
        for x in rating_file:
            line = x.strip('\n')
            name_score = line.split()
            for value in name_score:
                name_list.append(value)
        name_dict = {name_list[i]: name_list[i + 1] for i in range(0, len(name_list), 2)}
        rating_file.close()
        if self.name in name_dict:
            print('Your rating: ' + name_dict[self.name])
            shoot.game_entry()
        else:
            rating_file = open('ratings.txt', 'a')
            name_dict[self.name] = '0'
            print('Your rating: ' + name_dict[self.name])
            print('\n' + self.name + ' 0', file=rating_file)
            rating_file.close()
            shoot.game_entry()

    def write_score(self, name, result):
        rating_file = open('ratings.txt')
        name_list = []
        for x in rating_file:
            line = x.strip('\n')
            name_score = line.split()
            for value in name_score:
                name_list.append(value)
        name_dict = {name_list[i]: name_list[i + 1] for i in range(0, len(name_list), 2)}
        rating_file.close()

        if result == 'win':
            x = name_dict[name]
            x = int(x) + 100
            name_dict[name] = str(x)
        elif result == 'draw':
            x = name_dict[name]
            x = int(x) + 50
            name_dict[name] = str(x)

        rating_file = open('ratings.txt', 'w')
        for key in name_dict:
            print(key, name_dict[key], file=rating_file, flush=True)
        rating_file.close()


shoot = RockPaperScissors()
shoot.user_entry()
