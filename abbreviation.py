# An acronym is an abbreviation that uses the first letter of each word 
# in a phrase. We see them everywhere. For instance, NCAA for National 
# Collegiate Athletic Association or NBC for National Broadcasting Company. 

# Write a program where the user enters an acronym and the program randomly 
# selects words from a wordlist such that the words would fit the acronym. 
# Below is some typical output generated when I ran the program:

# Enter acronym: ABC ['addressed', 'better', 'common']

# Enter acronym: BRIAN ['bank', 'regarding', 'intending', 'army', 'naive']
# j[0].lower() not in first_letters:
def generatedWords(wordList, *achronym):
    res = []
    first_letters = []
    for i in range(len(achronym)):
        for j in wordList:
            if achronym[i].lower() == j[0].lower() and achronym.count(achronym[i]) > first_letters.count(j[0].lower()):
                res.append(j)
                first_letters.append(j[0].lower())
    if len(res) == len(achronym):
        print(res)
    else:
        print('No matches!!')
# ordering problem
wordList = (['hello', 'asana', 'world', 'book', 'Armenia', 'Question', 'apple', 
             'pictures', 'programmer', 'rainbow', 'ball', 'child', 'monkey', 'head', 'super'])


while True:
    valid = True
    achronym = input('input the achronym\n')
    for i in achronym:
        if not i.isalpha():
            valid = False
            print('your input is not valid, please input only letters\n')
    if valid:
        break

generatedWords(wordList, *achronym)
