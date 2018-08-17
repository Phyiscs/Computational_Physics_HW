##Name:Nicat
##Surname:Shukurov
## FINAL HOMEWORK 1 b NEWTONS METHOD
##=================================
import math
##=================================
##FUCNTION=========================
def f(x):
    return math.cos(x)+0.1*x**2-0.5
##PARAMETRS========================
##Boundaries
b=4 ##final inital=0
tol=0.01
##DERIVATION FUCNTION==============
def derivative(f):
    def compute(x, dx):
        return (f(x+dx) - f(x))/dx
    return compute

##NEWTONS METHOD===================
dx=0.000001
def newtons_method(f, b, tol,dx):
    '''f is the function f(x)'''
    df = derivative(f)
    while True:
        x1 = b - f(b)/df(b, dx)
        t = abs(x1 - b)
        if t < tol:
            break
        b = x1
    return b
##=====Program running=============
print("x=",newtons_method(f,b,tol,dx))