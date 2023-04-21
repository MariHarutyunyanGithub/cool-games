# Write a Python program that allows users to check the strength of 
# a password. The program should prompt the user to enter a password, 
# and then analyze it based on the following criteria:

# Length: The password should be at least 8 characters long.
# Complexity: The password should include a combination of uppercase and lowercase letters, 
# numbers, and special characters.

# Dictionary Words: The password should not include common dictionary words or phrases.

# The program should then provide feedback to the user on the strength of their password, 
# and suggest ways to improve it if necessary.

# Here are some additional specifications for the program:
# * he program should use a predefined list of common dictionary words, stored in a 
#       separate text file, with one word or phrase per line.
# * The program should handle input errors gracefully, and provide helpful error 
#       messages if the user enters invalid input.
# * The program should allow the user to specify custom criteria for password strength, 
#       such as minimum length or required character types.

def LengthValidator(func):
    def wrapper(pas, size):
        assert len(pas) >= size, 'The password should be at least 8 characters long'
        return func(pas, size)
    return wrapper

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


def DictionaryWord(pas, di):
    return di in pas

@LengthValidator
def checkPassword(pas, word_list, char_list, min_size):

    if checkComplexity(pas, char_list) != (1, 1, 1, 0):
        print('The password should include a combination of uppercase and lowercase letters, numbers, and special characters.\n')
        if not checkComplexity(pas, char_list)[0]:
            print('your password does not contain a number')
        elif not checkComplexity(pas, char_list)[1]:
            print('your password does not contain an uppercase letter')
        elif not checkComplexity(pas, char_list)[2]:
            print('your password does not contain a lowercase letter')
        elif not checkComplexity(pas, char_list)[3]:
            print("your password does not contain a special character")
    
    if DictionaryWord(pas, word_list):
        print('The password should not include common dictionary words or phrases')

def inputPassword():
    while True:
        # pas = input('please, input your password\n')
        char_list = input('input special character list').split()
        min_length = input('input minimum size of password') 

            
        
