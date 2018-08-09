##NAME: Nijat
##SURNAME: Shukurov
##id: 1784222
#HOMEWORK 1 , 2-2
from math import *
#fucntion 1
def f1(x):
    return cos(x)
#fucntion 2
def f2(x):
    return 1/(x**2)
#fucntion 3
def f3(x):
    return x**2+x+1
#fucntion 4
def f4(x):
    return cos(pi*(x**2))
#TRAPEZOID METHOD
def trapezoid_method(f,a,b,n):
    dx=float(b-a)/n
    x=a
    y=b
    summation=0.0
    for i in range(n):
        summation+=dx*(f(x)+f(x+dx))/2
        x+=dx
    return summation

#SIMPSONS METHOD
def simpsons_method(f,a,b,n):
    dx=float(b-a)/n
    sum=0.0
    x=a
    carp=0
    for i in range(1,n+1):
        if i==1 or i==n:
            carp=1
        elif i%2==0 and i!= n:
            carp=4
        else:
            carp=2
        sum+=carp*f(x)
        x+=dx
    return (sum*dx)/3

print(trapezoid_method(f1,1,10,10000))
print(simpsons_method(f2,1,10,10000))
print(simpsons_method(f3,1,10,10000))
print(simpsons_method(f4,1,10,100000))