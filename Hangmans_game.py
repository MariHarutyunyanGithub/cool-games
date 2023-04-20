# Hangman Games writes a Python program that allows users to play a 
# game of hangman. The program should generate a random word from a 
# predefined list of words, and then prompt the user to guess letters 
# in the word. The user should be allowed to make a limited number of 
# incorrect guesses before they lose the game.

# The program should use a pre-defined list of words, stored in a 
#           separate text file, with one word per line.
# The program should display the number of letters in the word, 
#           with each unknown letter represented by an underscore (_).
# The user should be allowed to guess one letter at a time. 
# The program should display the letters that have already been guessed, 
#           along with the remaining number of guesses.
#   If the user correctly guesses a letter, the program should 
#           update the display to show the letter in the correct position(s).
# If the user makes an incorrect guess, the program should decrement 
#           the remaining number of guesses and display a hangman graphic.
# If the user correctly guesses all of the letters in the word
#           before running out of guesses, the program should 
#           display a message indicating that they won the game.
# If the user runs out of guesses before correctly guessing all of 
#           the letters in the word, the program should display a message 
#           indicating that they lost the game, and reveal the word.


import random

def chooseWord():
    with open('words.txt') as file:
        text = file.read()
        ls = text.split()
        idx = random.randint(0, len(ls))
        print(ls[idx], '(for easy test)')
        return ls[idx]
            


def render(word):
    ls = list(word)
    for i in range(len(ls)):
        ls[i] = '- '
    def closier(char):
        for i in range(len(word)):
            if word[i].lower() == char.lower():
                ls[i] = char.upper()
        return "  ".join(ls)
    return closier

def punishment():
    image = '''                          ------------
                            |       |
                            |        
                            |          
                            |        
                            |         
                            |
                           ---'''
    image = list(image)

    def closier(chance):
        match(chance):
            case 5: image[113] = 'o'
            case 4: 
                image[151] = '|'
                image[191] = '|'
            case 3: image[150] = '\\'
            case 2: image[152] = '/'
            case 1: image[228] = '/'
            case 0: 
                image[230] = '\\'
                # image[189] = '/'
                # image[191] = '\\'
                image[150] = '/'
                image[152] = '\\'
        return ''.join(image)
    return closier

def playAgain():
    while True:
        ans = input()
        if ans.lower() == 'y':
            word = chooseWord()
            game(word)
        elif ans.lower() == 'n':
            print('\n\n\t\t\t\t\tBYE!!!!\n\n')
            exit()
        else:
            print('your input is not valid, input \'y\' or \'n\'\n')


def game(word):
    print('\n\t\t\t\tWellcome\U0001F60A')
    print('\n\n\t\t\tLets play Hangman game...\n\n')
    print('\tplease enter any letter to guess the number we have memorized.')
    print(f'\n\t\t\tAs a hint, our word looks like this\n')
    print('\t\t\t\t', end = '')
    chance = 6
    penalty = punishment()
    for i in range(len(word)):
        print('-  ', end = '')
    print(f'\n\n\t\t\tyou have {chance} chances to be wrong\n')
    print('\t\t\totherwise your end will be bad\U0001F47F')
    print(penalty(chance))
    display = render(word)
    while chance:
        answer = input(f'\n\ncharacter\t')
        result = display(answer)
        if answer.lower() not in word.lower():            
            chance -= 1
            print('\nwrong answer!!\n')
            print(penalty(chance))
            print(f'\n\t\t\t{result}')
            if chance == 0:
                print('\n\t\t\t\tGAME OVER!\n\n')
                print('do you want to try again?y/n :  ')
                playAgain()


        else:
            print(penalty(chance))
            print(f'\n\t\t\t{result}')  
            if '- ' not in result:
                print('\n\t\tcongratulations, you won!'.upper(), '\U0001F60A\n\n')
                playAgain()
                   
            


word = chooseWord()
game(word)

            

                

    




