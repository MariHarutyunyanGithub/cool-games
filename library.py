# The Library Management System is a program that allows users to manage a library 
# collection of books. The system provides the following functionalities: 
# * Add Books: The user is allowed to enter the full name of the author, the 
#       name of the book and its publication date. The list of all the books should 
#       be kept in a text file.
# * Remove Books: The user is allowed to remove a book from the list by using its name.
# * View All Books: The user can see the list of all the books in the library. 
# * Sort Books Alphabetically: The user can make the sorted list of all the books in 
# the library. The system should store the library's book collection in a text file. 

# When the program starts, it should read the file and load the books into memory.
# When the user makes changes to the library, such as adding or removing a book, 
# the program should update the file accordingly. To implement this system, 
# you can use Python's built-in file handling capabilities to read and write to 
# the file that stores the library collection. You can also use Python's data 
# structures like lists and dictionaries to store the book collection in memory 
# and provide the necessary functionalities like sorting and removing books.


books = {}

def fillInfo():
    file = open('books.txt')
    for line in file:
        title = ''            
        for i in line:
            if i != '|':                
                title += i
            else: 
                break
        books[title] = line
    file.close()

def funcDeduce(key):
    match(key):
        case 1: createBookInstance()
        case 2: removeBook()
        case 3: viewAllBooks()
        case 4: sortBooks()
        case 5: exitFromProgram()    

def wellcome():
    while True:
        print('''\t\t [1] ------------add book
                 [2] ---------remove book
                 [3] ------view all books
                 [4] ----------sort books
                 [5] ----------------exit''')
        try:
            key = int(input('\n\nyour choice\t'))
            if key in (1, 2, 3, 4, 5):
                break
            print('please, input from range [1:5]\n')
        except:
            print('\nyour input is not valid, please input an intager value\n')                
    funcDeduce(key)

def addBook(info):
    file = open('books.txt', 'a')    
    file.write(info)
    file.close()

def createAutorName():
        while True:
            valid = True
            name = input(f'input autor name: ')
            for i in name:
                if not i.isalpha() and i not in (' ', '-', '_', '.'):
                    valid = False
            if valid:
                break
            else:
                print(f'\nyour input for autor name is not valid, please try again\n')
        return name

def createPublicationDate():
    while True:
        valid = True
        date = input('input publication date : ')
        for i in date:
            if not i.isdigit():
                valid = False
                break
        if valid:
            if int(date) > 2023:
                print('that date for future, please input another number\n')
            else:
                break
        else:
            print('\nyour input for date is not valid, please try again\n')
    return date

def createBookInstance():
    while True:
        title = input('input title of book\n')
        if title in books.keys():
            print('this book title already exists, input another title\n')
        else:
            break    
    autorNeme = createAutorName()
    date = createPublicationDate()
    text = title + '|' + autorNeme + '|' + date + '|\n'
    books[title] = text
    addBook(text)
    print('\n\t\tBook added successfully!!!\n')
    wellcome()

def deleteFromFile(title):
    with open('books.txt', 'r') as file:
        lines = file.readlines()
    with open("books.txt", "w") as file:
        for line in lines:
            if line != books[title]:
                file.write(line)

def findNthCharacter(st, substr, n):
    k = 0
    for index, c in enumerate(st):
        if c == substr:
            k += 1
            if k == n:
                return index

def removeBook():
    while True:
        title = input('input title to remove from library\n')
        if title not in books.keys():
            print(f'{title} is not exist in our library. Please input another title')
        else: break
    deleteFromFile(title)
    del books[title]
    print('\nC\t\tbook deleted successfully !!\n')
    wellcome()

def exitFromProgram():
    print('Are you sure you want to exit?(y/n)')
    while True:
        key = input()
        if key.lower() == 'y':
            print('\n\n\t\t\tBYE!!!\n\n')
            exit()
        elif key.lower() == 'n':
            wellcome()
        else:
            print('your input is not valid, please input \'y\' or \'n\'\n')

def viewAllBooks():
    print('\n')
    with open('books.txt') as file:
        for line in file:
            info = line.replace('|', '      ')
            print(info)
    wellcome()

def sortBooks():
    print('\n\t\t\tSorded library here\n')
    for i in sorted(books.keys()):
        print(books[i], end = '\n')
    print('\n')
    wellcome()


print("\n\n\t\t    WELLCOME TO LIBRARY\n\n")
fillInfo()
wellcome()
