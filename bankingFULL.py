import sqlite3
import random

conn = sqlite3.connect('card.s3db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS card(
               id INTEGER, 
               number TEXT, 
               pin TEXT, 
               balance INTEGER DEFAULT 0)''')
conn.commit()


class BankAccount:

    def __init__(self):

        self.choice = None
        self.pin = None
        self.card_no = None
        self.entry1 = None
        self.logged_in = False
        self.luhn = False
        self.trans_account = ""
        self.exists = False

    def user_entry(self):

        self.choice = None
        while self.choice != 0:
            print("1. Create an account\n2. Log into account\n0. Exit""")
            self.choice = int(input())
            if self.choice == 1:
                account.luhn_calc()
                account.create_account()
                continue
            elif self.choice == 2 and self.logged_in is False:
                account.log_in()
            elif self.choice == 0:
                print("Bye!")
                quit()
            else:
                continue

    def create_account(self):

        self.pin = str(random.randint(0000, 9999)).zfill(4)
        next_id = cur.execute('SELECT MAX(id) FROM card')
        for row in next_id:
            id = row[0]
        if id is None or id == 0:
            id = 1
        else:
            id += 1
        cur.execute('INSERT INTO card(id, number, pin) VALUES (?, ?, ?)', (id, self.card_no, self.pin))
        print("Your card has been created\nYour card number:")
        print(self.card_no)
        print("Your card PIN:")
        print(self.pin)
        conn.commit()

    def luhn_calc(self):

        luhn_check = False
        while luhn_check is False:
            num = "400000" + str(random.randint(0000000000, 9999999999)).zfill(10)
            num_list = [int(x) for x in num]
            check_sum = num_list[-1]
            num_list.pop(-1)
            count = 1
            total = 0
            double_list = []
            check_list = []
            for num in num_list:
                if count % 2 == 0:
                    count += 1
                    double_list.append(num)
                else:
                    num *= 2
                    count += 1
                    double_list.append(num)
            for num in double_list:
                if num > 9:
                    num -= 9
                    check_list.append(num)
                else:
                    check_list.append(num)
            for num in check_list:
                total += num
            if (total + check_sum) % 10 == 0:
                luhn_check = True
        num_list.append(check_sum)
        card_no = ""
        for x in num_list:
            card_no += str(x)
        self.card_no = card_no

    def log_in(self):

        global entry2
        card_list = []
        pin_list = []
        card_numbers = cur.execute('SELECT number FROM card')
        for row in card_numbers:
            card_list.append(row[0])
        pin_numbers = cur.execute('SELECT pin FROM card')
        for row in pin_numbers:
            pin_list.append(row[0])
        while self.logged_in is False:
            print("Enter your card number:")
            self.entry1 = str(input())
            print("Enter your PIN:")
            entry2 = str(input())
            if self.entry1 in card_list:
                if entry2 in pin_list:
                    self.logged_in = True
                    print("You have successfully logged in!")
                    account.account_actions()
                else:
                    print("Wrong card or PIN!")
                    account.user_entry()
            else:
                print("Wrong card or PIN!")
                account.user_entry()

    def account_actions(self):

        self.choice = None
        while self.choice != 0:
            print('''1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit''')
            self.choice = int(input())
            if self.choice == 1:
                balance = cur.execute('SELECT balance FROM card WHERE number = ?', (self.entry1,))
                for row in balance:
                    balance = row[0]
                print("Balance: " + str(balance))
            elif self.choice == 2:
                account.add_income()
            elif self.choice == 3:
                account.transfer()
            elif self.choice == 4:
                account.close_account()
            elif self.choice == 5:
                print("You have successfully logged out!")
                account.user_entry()
                self.logged_in = False
            elif self.choice == 0:
                print("Bye!")
                quit()
            else:
                continue

    def add_income(self):

        print('How much would you like to deposit?')
        deposit = 'UPDATE card SET balance = balance + ? WHERE number = ?'
        cur.execute(deposit, (int(input()), self.entry1))
        conn.commit()
        account.account_actions()

    def transfer(self):

        self.exists = False
        print('Please enter the account number to receive the transfer: ')
        self.trans_account = str(input())
        account.luhn_check()
        account.does_exist()
        if self.trans_account == self.entry1:
            print("You can't transfer money to the same account!")
            account.account_actions()
        elif self.exists is False:
            print("Such a card does not exist.")
            account.account_actions()
        else:
            print('Please enter the amount you would like to transfer: ')
            transfer_amount = int(input())
            balance = cur.execute('SELECT balance FROM card WHERE number = ?', (self.entry1,))
            for row in balance:
                balance = row[0]
            if balance < transfer_amount:
                print("Not enough money!")
                account.account_actions()
            else:
                transfer1 = 'UPDATE card SET balance = balance + ? WHERE number = ?'
                cur.execute(transfer1, (transfer_amount, self.trans_account))
                transfer2 = 'UPDATE card SET balance = balance - ? WHERE number = ?'
                cur.execute(transfer2, (transfer_amount, self.entry1))
                conn.commit()
                account.account_actions()

    def luhn_check(self):

        luhn = False
        num_list = [int(x) for x in self.trans_account]
        check_sum = num_list[-1]
        num_list.pop(-1)
        count = 1
        total = 0
        double_list = []
        check_list = []
        for num in num_list:
            if count % 2 == 0:
                count += 1
                double_list.append(num)
            else:
                num *= 2
                count += 1
                double_list.append(num)
        for num in double_list:
            if num > 9:
                num -= 9
                check_list.append(num)
            else:
                check_list.append(num)
        for num in check_list:
            total += num
        if (total + check_sum) % 10 == 0:
            luhn = True
        if luhn is False:
            print('You probably made a mistake in the card number. Please try again!')
            account.account_actions()

    def does_exist(self):

        account_list = []
        accounts = cur.execute('SELECT number FROM card')
        for row in accounts:
            account_list += row
        for num in account_list:
            if num == self.trans_account:
                self.exists = True

    def close_account(self):

        delete = 'DELETE FROM card WHERE number = ?'
        cur.execute(delete, (self.entry1,))
        print('Account successfully deleted.')
        self.logged_in = False
        conn.commit()
        account.user_entry()


account = BankAccount()
account.user_entry()