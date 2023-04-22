# Implement a program, that allows to register a contact information (name, surname, 
# phone number, address).The program should provide a console interface , 
# where the user is able to add a new contact , edit the contact information 
# of the already existing one and remove one of the contacts. All the registered 
# information should be kept in a text file, so that it is not lost after closing the program.
# After any change of the contact information it should be saved in the existing file. 
# During the time the program runs it should be able to read from the text file 
# where all the information is kept. 

contacts = {}
phones = [] # phone number must be unique

def fillInfo():
    file = open('contact.txt')
    for line in file.readlines():
        name = ''            
        for i in line:
            if i != '|':                
                name += i
            else: break
        contacts[name] = line
    file.close()
    file = open('contact.txt')
    for line in file.readlines():
        idx = findNthCharacter(line, '|', 2)
        phone = ''
        for i in range(idx + 1, len(line)):
            if line[i] != '|':
                phone += line[i]
            else: break
        phones.append(phone)
    file.close()
        



def funcDeduce(key):
    match(key):
        case 1: createContact()
        case 2: editContact()
        case 3: removeContact()
        case 4: exitFromProgram()

    

def wellcome():
    while True:
        print('''\t\t [1] ----------add contact
                 [2] ---------edit contact
                 [3] -------remove contact
                 [4] -----------------exit''')
        try:
            key = int(input('\n\nyour choice\t'))
            if key in (1, 2, 3, 4):
                break
            print('please, input from range [1:4]\n')
        except:
            print('\nyour input is not valid, please input an intager value\n')                
    funcDeduce(key)

def addContact(info):
    file = open('contact.txt', 'a')    
    file.write(info)
    file.close()

def createName(st):
        while True:
            valid = True
            name = input(f'input contact {st} : ')
            for i in name:
                if not i.isalpha() and i not in (' ', '-', '_'):
                    valid = False
            if valid:
                break
            else:
                print(f'\nyour input for {st} is not valid, please try again\n')
        return name

def createPhone():
    while True:
        valid = True
        phone = input('input phone number : ')
        for i in phone:
            if not i.isdigit():
                valid = False
                break
        if valid:
            if phone in phones:
                print('that number already exists, please input another number\n')
            else:
                break
        else:
            print('\nyour input for phone number is not valid, please try again\n')
    return phone

def createAddress():
    while True:
        valid = True
        address = input('input address : ')
        for i in address:
            if (not i.isalpha() and not i.isdigit()) and (i not in('_', '-', '/', '.', ',', ' ')):
                valid = False
                break
        if valid:
            break
        else:
            print('\nyour input for address is not valid, please try again\n')
    return address

def createContact():
    while True:
        name = createName('name')
        if name in contacts.keys():
            print('contact already exists, input another name(sorry, but my program is not ideal)\n')
        else:
            break    
    surname = createName('surname')
    phone = createPhone()
    address = createAddress()
    text = name + '|' + surname + '|' + phone + '|' + address + '|'
    contacts[name] = text
    addContact(text)
    print('\n\t\tContact created successfully!!!\n')
    wellcome()

def deleteFromFile(st):
    with open('contact.txt', 'r') as file:
        lines = file.readlines()
    with open("contact.txt", "w") as file:
        for line in lines:
            if line != contacts[st]:
                file.write(line)

def changeNameInfo(info, new_name):
    name = ''
    for i in info:
        if i != '|':
            name += i
        else: break    
    info = info.replace(name, new_name)    
    return info

def changeSurNameInfo(info, new_surName):
    idx = findNthCharacter(info, '|', 1)
    surname = ''
    for i in range(idx + 1, len(info)):
        if info[i] != '|':
            surname += info[i]
        else: break
    info = info.replace(surname, new_surName)
    return info

def changePhoneInfo(info, new_phone, phone):
    info = info.replace(phone, new_phone)
    return info

def changeAddressInfo(info, new_address):
    address = ''
    idx = findNthCharacter(info, '|', 3)
    for i in range(idx + 1, len(info)):
        if info[i] != '|':
            address += info[i]
        else: break
    info = info.replace(address, new_address)
    return info

def findNthCharacter(st, substr, n):
    k = 0
    for index, c in enumerate(st):
        if c == substr:
            k += 1
            if k == n:
                return index
            
def removeFromPhones(info):
    idx = findNthCharacter(info, '|', 2)
    phone = ''
    for i in range(idx + 1, len(info)):
        if info[i] != '|':
            phone += info[i]
        else: break
    phones.remove(phone)
    return phone

def changeContactAttribute(key, name):
    if key == 'm':
        wellcome()
    else:
        deleteFromFile(name)
        info = contacts[name]
        del contacts[name]
        match(key):
            case 'n': 
                while True:
                    new_name = createName('name')  
                    if new_name not in contacts.keys():          
                        contacts[new_name] = changeNameInfo(info, new_name)
                        break
                    else:
                        print('contact already exists, input another name(sorry, but my program is not ideal)\n')
                addContact(contacts[new_name])              
            case 's': 
                new_surName = createName('surname')
                contacts[name] = changeSurNameInfo(info, new_surName)
                addContact(contacts[name])
            case 'p': 
                old_phone = removeFromPhones(info)
                new_phone = createPhone()
                contacts[name] = changePhoneInfo(info, new_phone, old_phone)
                addContact(contacts[name])
            case 'a': 
                new_address = createAddress()
                contacts[new_address] = changeAddressInfo(info, new_address)
                addContact(contacts[new_address]) 

def updating():
    print('What do you want to change on this contact?\n')
    while True:
        print('''\t\t[n]-------------name
                [s]----------surname
                [p]-----phone number
                [a]----------address
                [m]--------main menu''')
        key = input('\n\nyour choice\t')
        if key in ('n', 's', 'p', 'a', 'm'):
            break
        else:
            print('\nyour input is not valid\n')
    return key


def editContact():
    while True:
        name = createName('name')
        if name not in contacts.keys():
            print(f'{name} is not exist in our base. Please input another name')
        else: break
    key = updating()
    changeContactAttribute(key, name) 
    print('\n\t\tContact updated!!!\n') 
    wellcome()  

def removeContact():
    while True:
        name = createName('name')
        if name not in contacts.keys():
            print(f'{name} is not exist in our base. Please input another name')
        else: break
    removeFromPhones(contacts[name])
    deleteFromFile(name)
    del contacts[name]
    print('\nC\t\tcontact successfully deleted!!\n')
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


print("\n\n\t    Wellcome to contact management system".upper(), '\n\n')
fillInfo()
wellcome()