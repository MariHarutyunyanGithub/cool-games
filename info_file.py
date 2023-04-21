# Write a program that works with a text file. The aim of the program is to read a text 
# from the text file and analyze it. Specifically it should count and print:
# 1. the number of words
# 2. the number of letters
# 3. the number of sentences
# 4. the most used letter in a text
# 5. the most used word in a text
# For example if our text file contains this text: 
# “Hello from C++ world”
# the program should give the following output: 
# Words: 4 
# Letters: 15 (special characters and space are not counted)
# Sentences: 1 
# Letter frequency: o (both o and l are used 3 times so any of the letters is considered as a right answer)
# Word frequency: 0 (there is no word that is used more than once)
# The result should be kept in a separate text file. 

def wordCount():
    file = open(file_name)
    ls = []
    text = file.read()
    ls = text.split()
    file.close()
    return len(ls)

def characterCount():
    file = open(file_name)
    count = 0
    for lines in file:
        for i in lines:
            if i.isalpha() or i.isdigit():
                count += 1
    file.close()
    return count

def lineCount():
    file = open(file_name)
    count = 0
    for lines in file:
        count += 1
    file.close()
    return count

def mostUsedWord():
    file = open(file_name)
    text = file.read()
    if not len(text):
        return
    ls = text.split()
    max_count = 0
    max_used = ''
    for i in range(len(ls)):
        if max_count < ls.count(ls[i]):
            max_count = ls.count(ls[i])
            max_used = ls[i]
    file.close()                      
    return max_used    

def mostUsedCharacter():
    file = open(file_name)
    text = file.read()
    file.close()
    if not len(text):
        return 0
    max_used_char = ''
    di = {}
    for i in text:
        if i.isdigit() or i.isalpha():
            di[i] = text.count(i)
    max_count = max(di.values())
    for i in text:
        if text.count(i) == max_count and (i.isdigit() or i.isalpha()):
            return i


file_name = input('enter file name to analize\n')
print(f'in file \'{file_name}\'\n')
print(f'1.the number of words is {wordCount()}\n')
print(f'2. the number of letters is {characterCount()}\n')
print(f'3. the number of sentences is {lineCount()}\n')
print(f'4. the most used letter in a text is {mostUsedCharacter()}\n')
print(f'5. the most used word in a text is {mostUsedWord()}\n')
