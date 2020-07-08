import math
import argparse


class Calculator():

    def __init__(self, choice, principal, payment, months, interest):
        self.choice = choice
        self.principal = principal
        self.payment = payment
        self.months = months
        self.interest = interest

    def payment_calc(self):
        i = (self.interest / 12) / 100
        if self.choice == "annuity":
            self.payment = (self.principal * ((i * pow((1 + i), self.months))
                                              / (pow((1 + i), self.months) - 1)))
            self.payment = math.ceil(self.payment)
            print("Your annuity payment = " + str(self.payment) + "!")
            overpayment = (self.payment * self.months) - self.principal
            overpayment = math.ceil(overpayment)
            print("Overpayment = " + str(overpayment))
        else:
            count = 0
            month = 1
            overpayment = 0
            while count != self.months:
                diff_pay = (self.principal / self.months + i * (self.principal - (
                        (self.principal * (month - 1)) / self.months)))
                diff_pay = math.ceil(diff_pay)
                overpayment += diff_pay
                print("Month " + str(month) + " paid out " + str(diff_pay))
                month += 1
                count += 1
            overpayment -= self.principal
            print("Overpayment = " + str(overpayment))

    def month_calc(self):
        i = (self.interest / 12) / 100
        self.months = math.log((self.payment / (self.payment - i * self.principal)), 1 + i)
        self.months = math.ceil(self.months)
        years = 0
        overpayment = (self.payment * self.months) - self.principal
        overpayment = math.ceil(overpayment)
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
        print("Overpayment = " + str(overpayment))

    def principal_calc(self):
        i = (self.interest * .01) / 12
        self.principal = self.payment / (i * pow(1 + i, self.months)
                                         / (pow(1 + i, self.months) - 1))
        self.principal = math.ceil(self.principal)
        print("Your credit principal = " + str(self.principal))
        overpayment = (self.payment * self.months) - self.principal
        overpayment = math.ceil(overpayment)
        print("Overpayment = " + str(overpayment))


parser = argparse.ArgumentParser(description="Annuity or differential payment calculator")
parser.add_argument("--type", help="Enter diff or annuity")
parser.add_argument("--payment", default=0, help="Monthly payment amount")
parser.add_argument("--principal", default=0, help="Enter principal amount")
parser.add_argument("--periods", default=0, help="Enter number of months")
parser.add_argument("--interest", default=0, help="Enter interest rate")
args = parser.parse_args()

choice = args.type
payment = args.payment
principal = args.principal
months = args.periods
interest = args.interest

choice = str(choice)
payment = float(payment)
principal = float(principal)
months = int(months)
interest = float(interest)

check_value = [payment, principal, months]
count = 0
for x in check_value:
    if x == 0:
        count += 1

if choice != "diff" and choice != "annuity":
    print("Incorrect parameters")
    quit()
elif choice is "diff" and payment != 0:
    print("Incorrect parameters")
    quit()
elif interest <= 0:
    print("Incorrect parameters")
    quit()
elif payment < 0 or principal < 0 or months < 0:
    print("Incorrect parameters")
    quit()
elif count > 2:
    print("Incorrect parameters")
    quit()
else:
    calculator = Calculator(choice, principal, payment, months, interest)
    calculator.__init__(choice, principal, payment, months, interest)
    if payment == 0:
        calculator.payment_calc()
    elif principal == 0:
        calculator.principal_calc()
    elif months == 0:
        calculator.month_calc()
