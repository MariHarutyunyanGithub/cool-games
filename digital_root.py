# The digital root of a number n is obtained as follows: 
# Add up the digits n to get a new number. Add up the digits
# of that to get another new number. Keep doing this until you 
# get a number that has only one digit. That number is the 
# digital root. For example, if n = 45893, we add up the 
# digits to get 4 + 5 + 8 + 9 + 3 = 29. We then add up the 
# digits of 29 target 2+9=11. We then add up the digits of 
# 11toget 1+1=2. Since 2 has only one digit, 2 is our digital root.

import functools

def sum(a, b):
    return a + b

def digitalRoot(num):
        ls = []
        while num:
            ls.append(num % 10)
            num //= 10
        sum_digits = functools.reduce(sum, ls)
        if sum_digits <= 9:
            return sum_digits
        else:
            return digitalRoot(sum_digits)
        


print('input an integer  to calculate it\'s digital root\n')
while True:
    number = input()
    if number.isdigit():
        number = int(number)
        if number > 0:
            print(digitalRoot(number))
            break
        else:
            print('the number must be positive')
    else:
        print('your input is not an integer, try again\n')    
