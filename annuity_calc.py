import math


class Calculator():

    def __init__(self, principal, payment, months, interest):
        self.principal = principal
        self.payment = payment
        self.months = months
        self.interest = interest

    def payment_calc(self):
        i = (self.interest / 12) / 100
        self.payment = (self.principal * ((i * pow((1 + i), self.months))
                        / (pow((1 + i), self.months) - 1)))
        self.payment = math.ceil(self.payment)
        print("Your annuity payment = " + str(self.payment) + "!")

    def month_calc(self):
        i = (self.interest / 12) / 100
        self.months = math.log((self.payment / (self.payment - i * self.principal)), 1 + i)
        self.months = math.ceil(self.months)
        years = 0
        while self.months >= 12:
            years += 1
            self.months -= 12
        if self.months > 1 and years > 1:
            print("It takes" + str(years) + " years and " + str(self.months) + " months to repay this credit")
        elif self.months > 1 and years == 1:
            print("It takes 1 year and " + str(self.months) + " months to repay this credit")
        elif years > 1 and self.months == 1:
            print("It takes " + str(years) + "years and 1 month to repay this credit")
        elif self.months == 1 and years == 0:
            print("It takes 1 month to repay the credit")
        elif years == 1 and self.months == 0:
            print("It takes 1 year to repay the credit")
        else:
            print("It takes " + str(years) + " years to repay this credit")

    def principal_calc(self):
        i = (self.interest * .01) / 12
        self.principal = self.payment / (i * pow(1 + i, self.months)
                                      / (pow(1 + i, self.months) - 1))
        self.principal = round(self.principal)
        print("Your credit principal = " + str(self.principal))


calculate1 = Calculator(0, 0, 0, 0)

print('''What do you want to calculate?
type "n" - for count of months
type "a" - for annuity monthly payment
type "p" - for credit principal''')
choice = str(input())
if choice == "n":
    print("Enter credit principal: ")
    principal = float(input())
    print("Enter monthly payment: ")
    payment = float(input())
    print("Enter credit interest: ")
    interest = float(input())
    calculate1.__init__(principal, payment, 0, interest)
    calculate1.month_calc()
elif choice == "a":
    print("Enter credit principal: ")
    principal = float(input())
    print("Enter count of periods: ")
    months = float(input())
    print("Enter credit interest: ")
    interest = float(input())
    calculate1.__init__(principal, 0, months, interest)
    calculate1.payment_calc()
elif choice == "p":
    print("Enter monthly payment: ")
    payment = float(input())
    print("Enter count of periods: ")
    months = float(input())
    print("Enter credit interest: ")
    interest = float(input())
    calculate1.__init__(0, payment, months, interest)
    calculate1.principal_calc()
