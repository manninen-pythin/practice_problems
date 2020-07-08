contents = [400, 540, 120, 9]
money = 550
have_enough = True


def display():
    global contents
    print("The coffee machine has: ")
    print(str(contents[0]) + " of water")
    print(str(contents[1]) + " of milk")
    print(str(contents[2]) + " of coffee beans")
    print(str(contents[3]) + " of disposable cups")
    print(str(money) + " of money")


def check():
    global have_enough
    if decision == "1":
        if int(contents[0]) < 250 or int(contents[2]) < 16 or int(contents[3] < 1):
            print("Sorry Dave, I can't do that, please fill machine")
            have_enough = False
        else:
            have_enough = True
    elif decision == "2":
        if int(contents[0]) < 350 or int(contents[1]) < 75 or int(contents[2]) < 20 or int(contents[3] < 1):
            print("Sorry Dave, I can't do that, please fill machine")
            have_enough = False
        else:
            have_enough = True
    elif decision == "3":
        if int(contents[0]) < 200 or int(contents[1]) < 100 or int(contents[2]) < 12 or int(contents[3] < 1):
            print("Sorry Dave, I can't do that, please fill machine")
            have_enough = False
        else:
            have_enough = True


def buy():
    global contents
    global decision
    global money
    if decision == "1":
        contents[0] -= 250
        contents[2] -= 16
        contents[3] -= 1
        money += 4
        print("I have enough resources, making you a coffee!")
    elif decision == "2":
        contents[0] -= 350
        contents[1] -= 75
        contents[2] -= 20
        contents[3] -= 1
        money += 7
        print("I have enough resources, making you a coffee!")
    elif decision == "3":
        contents[0] -= 200
        contents[1] -= 100
        contents[2] -= 12
        contents[3] -= 1
        money += 6
        print("I have enough resources, making you a coffee!")


def fill():
    global contents
    print("Write how many ml of water do you want to add: ")
    contents[0] = int(contents[0]) + int(input())
    print("Write how many ml of milk do you want to add: ")
    contents[1] = int(contents[1]) + int(input())
    print("Write how many grams of coffee beans do you want to add: ")
    contents[2] = int(contents[2]) + int(input())
    print("Write how many disposable cups of coffee do you want to add: ")
    contents[3] = int(contents[3]) + int(input())


def take():
    global money
    print("I gave you $" + str(money))
    money -= money
    if money < 0:
        money = 0


action = str(input("Write (buy, fill, take, remaining, exit): "))
while action != "exit":
    if action == "fill":
        fill()
    elif action == "take":
        take()
    elif action == "remaining":
        display()
    elif action == "buy":
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
        decision = str(input())
        check()
        if have_enough:
            buy()
    action = str(input("Write (buy, fill, take, remaining, exit): "))
