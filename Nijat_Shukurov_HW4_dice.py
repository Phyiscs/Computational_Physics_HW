__author__ = 'Nicat'
##Name:Nijat
##Surname:Shukurov
##ID:1784222
## dice rolling game
import random
def dice(num):## using print method we can change numbers from 1 to 6 as visual in command line screen
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

def input_t0_roll():##main funticon
    a=input("enter to roll")##press enter to continue
    roll=True##roll true after press
    while(roll==True):##loop works while roll true
        number1=random.randint(1,6)#generated number one
        number2=random.randint(1,6)#generated number two
        print("you rolled")
        print("----------")
        dice(number1)
        print("----------")
        dice(number2)
        print("===========")
        a=input("press enter to roll")
        roll=True
input_t0_roll()