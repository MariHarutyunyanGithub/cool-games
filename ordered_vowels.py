# You are given a file namelist.txt that contains a bunch of names. 
# Print out all the names in the list in which the vowels a, e, i, o, and u 
# appear in order (with repeats possible). The first vowel in the name must 
# be a and after the first u, it is okay for there to be other vowels. 
# An example is Ace Elvin Coulson.

import collections

def collectCandidatWords(lst):
    ls = []
    with open('namelist.txt') as file:
        for line in file:
            valid = True
            for j in lst:
                if j.lower() not in line.lower():
                    valid = False
                    break
            if valid:
                ls.append(line.strip('\n'))
    return ls

def takeOutVowels(candidates, lst):
    all_vowels = []
    for name in candidates:
        vowels = []
        for char in name:
            if char.lower() in lst:
                vowels.append(char.lower())
        all_vowels.append(vowels)
    return all_vowels
                
def makeUnique(all_vowels):
    unique_vowels = []
    for vowels in all_vowels:
        size = len(vowels)
        i = 0
        while len(vowels) - 1 > i:
            if vowels[i] == vowels[i + 1]:
                vowels.pop(i)
            else:
                i += 1
        unique_vowels.append(vowels)
    return unique_vowels

def check_order(uniques, pattern):
    indexes = []
    for vowels in uniques:
        matches = True
        for i in range(len(pattern)):
            if vowels[i] != pattern[i]:
                matches = False
        if matches:
            indexes.append(uniques.index(vowels))
    return indexes

def matching(indexes, candidates):
    result = []
    for i in indexes:
        for j in candidates:
            if candidates.index(j) == i:
                result.append(j)
    print(result)


def action(pattern):
    candidates = collectCandidatWords(pattern)
    vowels_list = takeOutVowels(candidates, pattern)
    uniques = makeUnique(vowels_list)
    indexes = check_order(uniques, pattern)
    matching(indexes, candidates)

    

pattern = ['a', 'e', 'i', 'o', 'u'] 
action(pattern)  
