# Crossword cheater: When working on a crossword puzzle, 
# often you will have a word where you know several of 
# the letters, but not all of them. You can write a computer 
# program to help you. For the program, the user should be 
# able to input a word with the letters they know filled in 
# and asterisks for those they don’t know. The program should 
# print out a list of all words that fit that description. 
# For example, the input th***ly should return all the words 
# that could work, namely thickly and thirdly. 


def matched(str):
    file = open('words.txt', 'r')
    result = []
    for line in file.readlines():
        if len(str) == len(line[:-1]):
            same = True
            for j in range(len(str)):         
                if str[j] != '.' and str[j] != line[j]:                    
                    same = False
                    break
            if same and line[:-1] not in result:
                result.append(line[:-1])
    if len(result):
        print('\nthere are all matches\n')
    else:
        print('\nno matches')
    return result


print('\n\n\t\twellcome to crossword puzzle\n\n'.upper())
print('Please input your word to find in our word Database\n')
word = input()
for i in matched(word):
    print(i)