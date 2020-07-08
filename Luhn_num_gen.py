import random

luhn_check = False
while luhn_check is False:
    num = "400000" + str(random.randint(0000000000, 9999999999)).zfill(10)
    num_list = [int(x) for x in num]
    print(num_list)
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
    print(double_list)
    for num in double_list:
        if num > 9:
            num -= 9
            check_list.append(num)
        else:
            check_list.append(num)
    print(check_list)
    for num in check_list:
        total += num
    if (total + check_sum) % 10 == 0:
        luhn_check = True
num_list.append(check_sum)
card_no = ""
for x in num_list:
    card_no += str(x)
print(card_no)