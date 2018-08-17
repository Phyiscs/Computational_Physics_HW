##Name:Nicat
##Surname:Shukurov
## FINAL HOMEWORK 3 b 2
## Simpsons method
##=================================

import random
import math
from pylab import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
##=================================
## variables
h_plank=6.626*10**(-34)
kb=1.38*10**(-23)
c=3*10**8
h_=h_plank/2*math.pi
##FUCNTION=========================
def f(x):
    return (x**3)/((e**x)-1)
## Simpson method==================
def simpson_method(a,b):
    h=0.5
    N=(float(b-a))/h
    sum=0.0
    x=float(a)
    m=int(int(N)/2)
    for i in range(m):
        sum+=f(x)+(2.0*f(x+h))
        x+=2*h

    sum=(2*sum)-f(a)+f(b)
    sum=h*sum/3
    return sum

##program running==================
print("Homework 3 b 2 ")
print("SIMPSON METHOD")
T=input("Please input temprature")
print("input boundaries")
b=input("Please input b>>")
a=input("Please input a>>")

summation=((kb**4)*(int(T)**4)/(4*(math.pi**2)*(c**2)*(h_**3)))*simpson_method(int(a),int(b))
print("the summation is:",summation)
##end