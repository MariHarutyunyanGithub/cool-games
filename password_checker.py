# Write a Python program that allows users to check the strength of 
# a password. The program should prompt the user to enter a password, 
# and then analyze it based on the following criteria:

# Length:               The password should be at least 8 characters long.
# Complexity:           The password should include a combination of uppercase and lowercase letters, 
#                       numbers, and special characters.

# Dictionary Words:     The password should not include common dictionary words or phrases.

# The program should then provide feedback to the user on the strength of their password, 
# and suggest ways to improve it if necessary.

# Here are some additional specifications for the program:
# * The program should use a predefined list of common dictionary words, stored in a 
#       separate text file, with one word or phrase per line.
# * The program should handle input errors gracefully, and provide helpful error 
#       messages if the user enters invalid input.
# * The program should allow the user to specify custom criteria for password strength, 
#       such as minimum length or required character types.


def fillInfo(keywords):
    file = open('dict_words.txt')
    all_words = file.read()
    keywords = all_words.split()
    file.close()
    return keywords


def checkComplexity(pas, char_list):
    is_digit = False
    is_upper = False
    is_lower = False
    is_my_char = False
    for i in pas:
        if i.isdigit():
            is_digit = True
        elif i.isupper():
            is_upper = True
        elif i.islower():
            is_lower = True
        elif i in char_list:
            is_my_char = True
    return is_digit, is_upper, is_lower, is_my_char

def checkPassword(pas, keywords, char_list, min_size):
    if len(pas) < min_size:
        print(f'The password should be at least {min_size} characters long')
        return False

    if checkComplexity(pas, char_list) != (1, 1, 1, 0):
        print('The password should include a combination of uppercase and lowercase letters, numbers, and special characters.\n')
        if not checkComplexity(pas, char_list)[0]:
            print('your password does not contain a number')
        elif not checkComplexity(pas, char_list)[1]:
            print('your password does not contain an uppercase letter')
        elif not checkComplexity(pas, char_list)[2]:
            print('your password does not contain a lowercase letter')
        elif checkComplexity(pas, char_list)[3]:
            print("your password does not contain a special character")
        return False
    
    for word in keywords:
        if word in pas:
            print('The password should not include common dictionary words or phrases')
            return False
        
    return True


char_list = input("input special character list separated by spaces (for example % ^ &)\n").split()
keywords = []
keywords = fillInfo(keywords)
while True:
    min_length = input('input minimum size of password\n') 
    try:
        min_length = int(min_length)
        if min_length > 0:
            break
        elif min_length == 0:
            print('incorrect input. length must be positive\n')
        else:
            print('invalid input. The length cannot be negative\n')
    except:
        print('your input is not valid, please input an integer\n')
while True:
    pas = input('please, input your password\n')
    if checkPassword(pas, keywords, char_list, min_length):
        print('\n\t\t\tValid Password\n\n')
        break