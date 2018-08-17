##Name:Nicat
##Surname:Shukurov
## FINAL HOMEWORK 3 b 1
## Trapezoid method

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
##Trapezoid method
def trapezoid_method(a,b):
    h=0.5
    N=(float(b-a))/h
    sum=h/2*(f(a)+f(b))
    for i in range(int(N)):
        sum+=h*f(a+i*int(N))
    return sum
##Program running==========
print("Homework 3 b 1 ")
print("TRAPEZOPID METHOD")
T=input("Please input temprature")
print("input boundaries")
b=input("Please input b>>")
a=input("Please input a>>")

summation=((kb**4)*(int(T)**4)/(4*(math.pi**2)*(c**2)*(h_**3)))*trapezoid_method(int(a),int(b),int(n))
print("the summation is:",summation)