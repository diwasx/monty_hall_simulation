#!/bin/python3

import random

n = 10000000 # Trails
debug = False

def trail():
    r = random.randint(0,2)
    if(r == 0):
        doors = [1,0,0]
    elif(r == 1):
        doors = [0,1,0]
    elif(r == 2):
        doors = [0,0,1]


    return doors

def winning_probability():
    wins = 0
    for i in range(n):
        doors = trail()
        choice = random.randint(0,2)

        if(doors[choice] == 1):
            # print("Car!!!!")
            win = True
        elif(doors[choice] == 0):
            win = False
        if(win): wins+=1

        if(debug): print("Wins: {}\nWining Probability: {}\n---------------------------------------------------------".format(wins, round(wins/(i+1)*100,3)))
    print("Wins: {}\nWining Probability: {}\n---------------------------------------------------------".format(wins, round(wins/(i+1)*100,3)))


def switch_case(switch):
    wins = 0
    for i in range(n):
        doors = trail()
        choices = [0,1,2]
        choice = random.randint(0,2)
        other_choices = [x for x in choices if x!=choice]

        host_choice = random.choice(other_choices)

        if(doors[host_choice] == 1):
            other_choices.remove(host_choice)
            host_choice = other_choices[0]

        if(switch):
            switched_choice = [x for x in choices if x not in [choice, host_choice]][0]
            choice = switched_choice

        if(debug): print("You chose door: {}, Host opens door: {}, You switch to door: {}".format(choice, host_choice, switched_choice))

        if(doors[choice] == 1):
            win = True
        elif(doors[choice] == 0):
            win = False
        if(win): wins+=1

        if(debug): print("Prize door: {}, Wins: {}, Wining Probability: {}\n---------------------------------------------------------\
                ".format(doors.index(1), wins, round(wins/(i+1)*100,3)))
    print("Prize door: {}, Wins: {}, Wining Probability: {}\n---------------------------------------------------------\
            ".format(doors.index(1), wins, round(wins/(i+1)*100,3)))


# winning_probability()
# switch_case(False)
switch_case(True)
