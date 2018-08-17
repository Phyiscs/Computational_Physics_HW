__author__ = 'Nicat'

import random

def roll(sides=6):
    num_rolled=random.randint(1,sides)
    return num_rolled
def Roll():
    dice_side=6
    rolling=True
    while rolling==True:
        roll_again=input("ENTER=Roll, Q=Quit")
        if(roll_again.lower()!="q"):
           num1=roll(sides)
           num2=roll(sides)
           print("you rolled", num1,num2)
           dice(num1)
           print("==========")
           dice(num2)
        else:
            rolling=False
def dice(num):
    if num==1:
        print("|     |")
        print("|  0  |")
        print("|     |")
    if num==2:
        print("|0    |")
        print("|     |")
        print("|    0|")
    if num==3:
        print("|0    |")
        print("|  0  |")
        print("|    0|")
    if num==4:
        print("|0   0|")
        print("|     |")
        print("|0   0|")
    if num==5:
        print("|0   0|")
        print("|  0  |")
        print("|0   0|")
    if num==6:
        print("|0   0|")
        print("|0   0|")
        print("|0   0|")
main()
