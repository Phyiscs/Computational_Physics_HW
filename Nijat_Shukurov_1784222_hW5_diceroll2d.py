import random
from visual import *
from visual.controls import *
import os

c = controls(title="Play Game",x=430, y=0, width=300, height=300, range=50)##shows control panel
dice_1=box(pos=(-2,0,0),size=(2,2,2),color=color.blue)##displays dice one
dice_2=box(pos=(2,0,0),size=(2,2,2),color=color.blue)##displays dice two
n=button(pos=(0,0,0),width=40,height=40,text="ROll",action=lambda:input_to_roll())##roll button displays on control screen
m=button(pos=(0,-30,0),width=20,height=20,text="Exit",action=lambda:exit_dice())
def exit_dice():
    quit()
    os._exit()


def clean_dice1():##cleans the firsts dice
        point1=points(pos=[(-1.7,0,2), (2,0,0)], size=50, color=color.blue)
        point6=points(pos=[(-2.2,0,2), (2,0,0)], size=50, color=color.blue)
        point7=points(pos=[(-1.2,0,2), (2,0,0)], size=50, color=color.blue)
        point2=points(pos=[(-1.2,0.5,2), (2,0,0)], size=50, color=color.blue)
        point3=points(pos=[(-2.2,-0.5,2), (2,0,0)], size=50, color=color.blue)
        point4=points(pos=[(-1.2,-0.5,2), (2,0,0)], size=50, color=color.blue)
        point5=points(pos=[(-2.2,0.5,2), (2,0,0)], size=50, color=color.blue)
        
def clean_dice2():## cleans the second dice
        point1=points(pos=[(-1.7,0,2), (2,0,0)], size=50, color=color.blue)
        point6=points(pos=[(2.2,0,2), (2,0,0)], size=50, color=color.blue)
        point7=points(pos=[(1.2,0,2), (2,0,0)], size=50, color=color.blue)
        point2=points(pos=[(1.2,0.5,2), (2,0,0)], size=50, color=color.blue)
        point3=points(pos=[(2.2,-0.5,2), (2,0,0)], size=50, color=color.blue)
        point4=points(pos=[(1.2,-0.5,2), (2,0,0)], size=50, color=color.blue)
        point5=points(pos=[(2.2,0.5,2), (2,0,0)], size=50, color=color.blue)
        
def points_for_dice1(num):## generate the dots for numbers on first dice 
    if num==1:
        point1=points(pos=[(-1.7,0,2), (2,0,0)], size=50, color=color.red)
    if num==2:
        point2=points(pos=[(-1.2,-0.5,2), (2,0,0)], size=50, color=color.black)
        point3=points(pos=[(-2.2,0.5,2), (2,0,0)], size=50, color=color.black)
    if num==3:
        point1=points(pos=[(-1.7,0,2), (2,0,0)], size=50, color=color.black)
        point2=points(pos=[(-1.2,-0.5,2), (2,0,0)], size=50, color=color.black)
        point3=points(pos=[(-2.2,0.5,2), (2,0,0)], size=50, color=color.black)
    if num==4:
        point2=points(pos=[(-1.2,0.5,2), (2,0,0)], size=50, color=color.black)
        point3=points(pos=[(-2.2,-0.5,2), (2,0,0)], size=50, color=color.black)
        point4=points(pos=[(-1.2,-0.5,2), (2,0,0)], size=50, color=color.black)
        point5=points(pos=[(-2.2,0.5,2), (2,0,0)], size=50, color=color.black)
    if num==5:
        point1=points(pos=[(-1.7,0,2), (2,0,0)], size=50, color=color.black)
        point2=points(pos=[(-1.2,0.5,2), (2,0,0)], size=50, color=color.black)
        point3=points(pos=[(-2.2,-0.5,2), (2,0,0)], size=50, color=color.black)
        point4=points(pos=[(-1.2,-0.5,2), (2,0,0)], size=50, color=color.black)
        point5=points(pos=[(-2.2,0.5,2), (2,0,0)], size=50, color=color.black)
    if num==6:
        point6=points(pos=[(-2.2,0,2), (2,0,0)], size=50, color=color.black)
        point7=points(pos=[(-1.2,0,2), (2,0,0)], size=50, color=color.black)
        point2=points(pos=[(-1.2,0.5,2), (2,0,0)], size=50, color=color.black)
        point3=points(pos=[(-2.2,-0.5,2), (2,0,0)], size=50, color=color.black)
        point4=points(pos=[(-1.2,-0.5,2), (2,0,0)], size=50, color=color.black)
        point5=points(pos=[(-2.2,0.5,2), (2,0,0)], size=50, color=color.black)
        

def points_for_dice2(num):## generate the dots for numbers on second dice
    if num==1:
        point1=points(pos=[(1.7,0,2), (2,0,0)], size=50, color=color.red)
    if num==2:
        point2=points(pos=[(1.2,0.5,2), (2,0,0)], size=50, color=color.black)
        point3=points(pos=[(2.2,-0.5,2), (2,0,0)], size=50, color=color.black)
    if num==3:
        point1=points(pos=[(1.7,0,2), (2,0,0)], size=50, color=color.black)
        point2=points(pos=[(1.2,0.5,2), (2,0,0)], size=50, color=color.black)
        point3=points(pos=[(2.2,-0.5,2), (2,0,0)], size=50, color=color.black)
    if num==4:
        point2=points(pos=[(1.2,0.5,2), (2,0,0)], size=50, color=color.black)
        point3=points(pos=[(2.2,-0.5,2), (2,0,0)], size=50, color=color.black)
        point4=points(pos=[(1.2,-0.5,2), (2,0,0)], size=50, color=color.black)
        point5=points(pos=[(2.2,0.5,2), (2,0,0)], size=50, color=color.black)
    if num==5:
        point1=points(pos=[(1.7,0,2), (2,0,0)], size=50, color=color.black)
        point2=points(pos=[(1.2,0.5,2), (2,0,0)], size=50, color=color.black)
        point3=points(pos=[(2.2,-0.5,2), (2,0,0)], size=50, color=color.black)
        point4=points(pos=[(1.2,-0.5,2), (2,0,0)], size=50, color=color.black)
        point5=points(pos=[(2.2,0.5,2), (2,0,0)], size=50, color=color.black)
    if num==6:
        point6=points(pos=[(2.2,0,2), (2,0,0)], size=50, color=color.black)
        point7=points(pos=[(1.2,0,2), (2,0,0)], size=50, color=color.black)
        point2=points(pos=[(1.2,0.5,2), (2,0,0)], size=50, color=color.black)
        point3=points(pos=[(2.2,-0.5,2), (2,0,0)], size=50, color=color.black)
        point4=points(pos=[(1.2,-0.5,2), (2,0,0)], size=50, color=color.black)
        point5=points(pos=[(2.2,0.5,2), (2,0,0)], size=50, color=color.black)

def input_to_roll():##main funticon
        clean_dice1()
        clean_dice2()
        number1=random.randint(1,6)#generated number one
        number2=random.randint(1,6)#generated number two
        points_for_dice1(number1)
        points_for_dice2(number2)
    

