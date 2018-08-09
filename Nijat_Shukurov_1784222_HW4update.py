from visual import *
import random
from visual.controls import *
##Name:Nijat
##Surname:Shukurov
##ID:1784222
##HOMEWORK4 one dice with animation
c = controls(title="Play Game",x=430, y=0, width=300, height=300, range=50)##shows control panel
n=button(pos=(0,0,0),width=40,height=40,text="ROll",action=lambda:input_to_roll())##roll button displays on control screen
r=vector(0,0,-1)
dice=box(pos=r,size=(3,3,3),color=color.blue)
def shake_for_roll():#fucntion for animation
    r=0
    while r <30:
        rate(25)
        dice.rotate(angle=pi/10,axis=(0,0-1))
        dice.rotate(angle=pi/10)
        r=r+1
def clean_dice():
    point6=points(pos=[(-1,0,1), (0,0,0)], size=50, color=color.blue)
    point7=points(pos=[(1,0,1), (0,0,0)], size=50, color=color.blue)
    point2=points(pos=[(1,-1,1), (0,0,0)], size=50, color=color.blue)
    point3=points(pos=[(-1,1,1), (0,0,0)], size=50, color=color.blue)
    point4=points(pos=[(-1,-1,1), (0,0,0)], size=50, color=color.blue)
    point5=points(pos=[(1,1,1), (0,0,0)], size=50, color=color.blue)
    point1=points(pos=[(0,0,1), (0,0,0)], size=50, color=color.blue)

def points_for_dice(num):## generate the dots for numbers on first dice 
    if num==1:
        point1=points(pos=[(0,0,1), (0,0,0)], size=50, color=color.red)
    if num==2:
        point2=points(pos=[(1,-1,1), (0,0,0)], size=50, color=color.black)
        point3=points(pos=[(-1,1,1), (0,0,0)], size=50, color=color.black)
    if num==3:
        point1=points(pos=[(0,0,1), (0,0,0)], size=50, color=color.black)
        point2=points(pos=[(1,-1,1), (0,0,0)], size=50, color=color.black)
        point3=points(pos=[(-1,1,1), (0,0,0)], size=50, color=color.black)
    if num==4:
        point2=points(pos=[(1,-1,1), (0,0,0)], size=50, color=color.black)
        point3=points(pos=[(-1,1,1), (0,0,0)], size=50, color=color.black)
        point4=points(pos=[(-1,-1,1), (0,0,0)], size=50, color=color.black)
        point5=points(pos=[(1,1,1), (0,0,0)], size=50, color=color.black)
    if num==5:
        point1=points(pos=[(0,0,1), (0,0,0)], size=50, color=color.black)
        point2=points(pos=[(1,-1,1), (0,0,0)], size=50, color=color.black)
        point3=points(pos=[(-1,1,1), (0,0,0)], size=50, color=color.black)
        point4=points(pos=[(-1,-1,1), (0,0,0)], size=50, color=color.black)
        point5=points(pos=[(1,1,1), (0,0,0)], size=50, color=color.black)
    if num==6:
        point6=points(pos=[(-1,0,1), (0,0,0)], size=50, color=color.black)
        point7=points(pos=[(1,0,1), (0,0,0)], size=50, color=color.black)
        point2=points(pos=[(1,-1,1), (0,0,0)], size=50, color=color.black)
        point3=points(pos=[(-1,1,1), (0,0,0)], size=50, color=color.black)
        point4=points(pos=[(-1,-1,1), (0,0,0)], size=50, color=color.black)
        point5=points(pos=[(1,1,1), (0,0,0)], size=50, color=color.black)
def input_to_roll():
    clean_dice()
    shake_for_roll()
    number=random.randint(1,6)#generated number one
    points_for_dice(number)
