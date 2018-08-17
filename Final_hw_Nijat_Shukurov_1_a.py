##Name:Nicat
##Surname:Shukurov
## FINAL HOMEWORK 1 a BISECTION METHOD
##=================================
import math
##=================================
##FUCNTION=========================
def f(x):
    return math.sin(x)-0.25*x
##PARAMETRS========================
##Boundaries
b=3 ## final
a=2 ## intial
tol=0.02
##BISECTION_METHOD=================
def bisetion_method(b,a,f):
   dx=abs(b-a)
   while dx>tol:
      x=(a+b)/2.0
      if (f(a)*f(x))<0:
         b=x
      else:
         a=x
         dx=abs(b-a)
   return x
##Running the program=============
print("x=",bisetion_method(b,a,f))


