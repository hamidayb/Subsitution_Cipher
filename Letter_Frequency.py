import operator

def substitute_single(string, sub_with='', sub_by=''):
    if(sub_with == ''):
        sub_with = input('Subsitute with: ').lower()
        sub_by = input('Substitute By: ').lower()
    return string.lower().replace(sub_with, sub_by)

def substitute_multiple(string):
    string = string.lower()
    print('Press 0 to quit entering substituion letters')
    sub_with = sub_by = ' '
    s = string
    while sub_with != '0' and sub_by != '0':
        sub_with = input('Subsitute with: ').lower()
        sub_by = input('Substitute By: ').lower()
 
        s = substitute_single(s, sub_with, sub_by)

    return s

def frequency_count(string):
    d = {}
    for letter in string:
        if(letter.isalpha()):
            if letter not in d:
                d[letter] = 1
            else:
                d[letter] += 1

    d = {r: d[r] for r in sorted(d, key=d.get, reverse=True)}
    letters = []
    values = []

    for key,value in d.items():
        letters.append(key)
        values.append(value)
        
    print('\nTotal Frequency: ',sum(d.values()), '\n')

    for l in letters:
        print(l,end='  ||  ')
    print()
    for v in values:
        print(v,end='  ||  ')
    print()
    

string = input('Enter string: ')

string_copy = string

while(True):
    choice = int(input("\n1 for Substitute Single \n2 for Substitute Multiple \n3 for Frequency Count \n4 for String reset \n0 for Quit \nYour input: "))

    if(choice == 1):
        string = substitute_single(string, '', '')
        print(string)
    elif(choice == 2):
        string = substitute_multiple(string)
        print(string)
    elif(choice == 3):
        frequency_count(string)
    elif(choice == 4):
        string = string_copy
    elif(choice == 0):
        exit(0)
    else:
        continue


    
