# Write a Python program that allows users to analyze a text file 
# and extract useful information. The program should prompt the 
# user to enter the name of the file to analyze, and then offer several analysis options:

# Word Count: The program should count the total number of words in the file.
# Character Count: The program should count the total number of characters
#                   (including spaces) in the file.
# Line Count: The program should count the total number of lines in the file.
# Most Frequent Words: The program should display the 10 most frequent words in 
#                   the file, along with their frequencies.
# Word Search: The program should prompt the user to enter a word to search 
#                   for in the file, and then display all instances of that word, along with 
#                   the line numbers where they occur.

def opening():
    while True:
        file_name = input('\nenter the name of the file (with extention) to analyze\n')
        try:
            file = open(f'{file_name}')
            break
        except IOError:
            print('Could not open file!')
    return file

def wordCount():
    file = opening()
    ls = []
    text = file.read()
    ls = text.split()
    file.close()
    print(f'\nThere are {len(ls)} words in {file.name}\n')
    return len(ls)

def characterCount():
    file = opening()
    count = 0
    for lines in file.readlines():
        for i in lines:
            count += 1
    file.close()
    print(f'\nin file {file.name} {count} charactes\n')
    return count

def lineCount():
    file = opening()
    count = 0
    for lines in file.readlines():
        count += 1
    file.close()
    print(f'\ncount of lines in file {file.name} is {count}\n')

def mostFrequentWords():
    file = opening()
    text = file.read()
    ls = []
    ls = text.split()
    di = {}
    for i in range(len(ls)):
        di[ls[i]] = ls.count(ls[i])
    max_key = ''
    ls = []
    while len(ls) < 10:
        max_value = max(di.values())
        for i, j in di.items():
            if j == max_value:
                ls.append(i)
                di[i] = 0
                if len(ls) >= 10:
                    break 
    file.close() 
    print(f'\nThe 10 Frequent words on file {file.name} are\n\n')                      
    return ls    

def Word_Search(word):
    file = opening()
    count = 0
    ls = []
    while text := file.readline():
        count += 1
        for j in text.split():
            if j == word:
                ls.append(count)
    file.close()
    if len(ls) > 1:
        print(f'\'{word}\' in \'{file.name}\' on lines')
    elif not len(ls):
        print(f'\nThere is not such word in \'{file.name}\'')
        return
    else:
        print(f'\'{word}\' in {file.name} on line')
    return ls

def quit():
    print('\nAre you sure, you want to exit from programm? (y/n)')
    while True:
        answer = input()
        if answer.lower() == 'y':
            print('\n\n\n\t\t\t\t\U0001F91A BYE \U0001F91A\n\n\n')
            exit()
        elif answer.lower() == 'n':
            variants()
        else:
            print('\nyour input is not valid, please, input \'y\' or \'n\'\n')
    
def variants():
    while True:
        print('\n\n')
        print('\t\t\t\t[1] ------------- Word Count')
        print('\t\t\t\t[2] -------- Character Count')
        print('\t\t\t\t[3] ------------- Line Count')
        print('\t\t\t\t[4] ---- Most Frequent Words')
        print('\t\t\t\t[5] ------------ Word Search')
        print('\t\t\t\t[6] ------------------- Exit')
        try:
            answer = int(input('\n\n\t\t\t\tyour choice\t'))
            if answer in (1, 2, 3, 4, 5, 6):
                break
            print('please, input from range [1:6]\n')
        except:
            print('\nyour input is not valid, please input an intager value\n')
            
    functions(answer)

def functions(key):
    match(key):
        case 1: wordCount()
        case 2: characterCount()
        case 3: lineCount()
        case 4: print(mostFrequentWords())
        case 5: 
            word = input('\ninput the word you wont to search\t')
            print(Word_Search(word))
        case 6: quit()

def start():
    print('\n\n\t\t\t\t\tWellcome to TEXT_ANALIZER\n\n')
    while True:
        variants()

start()