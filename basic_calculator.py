# define the functions needed add, sub, mul, div
# print options to the user
# get user input (ask for values)
# call the functions

import sys

def add(a, b):

    return (a + b)

def sub(a, b):
    
    return (a - b)

def mul(a, b):

    return (a * b)

def div(a, b):

    return (a / b)


def calculator():

   

    while True:
        print("----Calculator Menu----")
        print("----Press 1 for add----")
        print("----Press 2 for sub----")
        print("----Press 3 for mul----")
        print("----Press 4 for div----")
        print("----Press 5 to exit the program----")
        
        option = int(input("Choose a option: "))
   
        if option == 1:
            a = int(input("Add a number: "))
            b = int(input("Add another number: "))
            print(add(a,b))
        elif option == 2:
            a = int(input("Add a number: "))
            b = int(input("Add another number: "))
            print(sub(a,b))
        elif option == 3:
            a = int(input("Add a number: "))
            b = int(input("Add another number: "))
            print(mul(a,b))
        elif option == 4:
            a = int(input("Add a number: "))
            b = int(input("Add another number: "))
            print(div(a,b))
        elif option == 5:
            sys.exit()
        else:
            "Introduceti un numar intre 0 si 4. "


calculator()