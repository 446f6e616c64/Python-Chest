#!/usr/bin/python
# Script that Generates unique User Names

import random

def quantity(message):
    try:
        userInput = int(input(message))
    except ValueError:
        print("Only use Numbers!")
        quit()
    else:
        print("Ok! Let's generate " + str(userInput) + " names for you!")
        return userInput

def gender(message):
    boy = ['boy','b']
    girl = ['girl', 'g']
    random = ['random', 'r']

    print("You can choose Boy(b) Girl(g) or Random(r)")
    answer = input(message).lower()
    if answer in boy:
        print("You selected Boy")
        answer = 'boy'
        return answer
    elif answer in girl:
        print("You selected Girl")
        answer = 'girl'
        return answer
    elif answer in random:
        print("You selected Random")
        answer = 'random'
        return answer
    else:
        print("You entered something else")

def generate_name(qty,gdr):
    a = str(gdr)
    b = int(qty)
    d = []

    if a == 'boy':
        try:
            with open('boy_first.txt', 'r') as f:
                firstname = [line.strip() for line in f]
            with open('lastnames.txt', 'r') as l:
                lastname = [line.strip() for line in l]
            for i in range(b):
                first = random.choice(firstname)
                firsti = first[:1]
                last = random.choice(lastname)
                fullname = first + " " + last
                username = str(firsti).lower() + str(last).lower()
                d.append(fullname)
                d.append(username)
        except:
            print("Failed Here - 100")

        print(d)

    elif a == 'girl':
        try:
            with open('girl_first.txt', 'r') as f:
                firstname = [line.strip() for line in f]
            with open('lastnames.txt', 'r') as l:
                lastname = [line.strip() for line in l]
            for i in range(b):
                first = random.choice(firstname)
                firsti = first[:1]
                last = random.choice(lastname)
                fullname = first + " " + last
                username = str(firsti).lower() + str(last).lower()
                d.append(fullname)
                d.append(username)
        except:
            print("Failed Here - 200")

        print(d)

    elif a == 'random':
        try:
            with open('boy_first.txt', 'r') as f:
                firstname = [line.strip() for line in f]
            with open('girl_first.txt', 'r') as f:
                firstname.append([line.strip() for line in f])
            with open('lastnames.txt', 'r') as l:
                lastname = [line.strip() for line in l]
            for i in range(b):
                first = random.choice(firstname)
                firsti = first[:1]
                last = random.choice(lastname)
                fullname = first + " " + last
                username = str(firsti).lower() + str(last).lower()
                d.append(fullname)
                d.append(username)
        except:
            print("Failed Here - 300")

        print(d)


#MAIN PROGRAM STARTS HERE
qty = quantity("How many names would you like to create? ")
gdr = gender("Boys, Girls, or Random?")
generate_name(qty,gdr)
