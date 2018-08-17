##Name:Nicat
##Surname:Shukurov
## FINAL HOMEWORK 2
##=================================
from pylab import *
import math
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.optimize import brentq
import sys
h_bar=1.054*10**(-34)
m_elc=9.1*10**(-31)
fi=[]
fi_1=[]
fi_2=[]
b=2.0
L=200
V0=-50
 #potential outside square well
steps=100
E=0.0   #global variable, change by Final_Value()
##potelcial fucntion==============
def V(x):
    if x<=-L or x>=L:
        return 0
    if x==0:
        return -50
    if x>-L and x<0:
        return -50*((x+L)/L)
    if x>0 and x<L:
        return 50*((x-L)/L)

def v1(x):
    if x<1:
        return 0
    else:
        return 20
##================================

def SE(y,x):
    """
    Returns derivs for the 1-D TISE, for use in odeint.
    Requires global value E to be set elsewhere.
    Note that we are using x as time here... Python doesn't care!
    """
    g0=y[1]
    g1=-2.0*(E-V(x))*y[0]
    return array([g0,g1])


def Final_Value(energy):
    """
    Calculates psi for this value of E, and
    returns the value of psi at point b to check divergence
    """
    global y
    global E
    E=energy
    y=odeint(SE,y0,x)
    return y[-1,0]    #return final value (psi at b)

y=zeros([steps,2])
y0=array([1.0,0.0])   #initial psi and psi-dot
x=linspace(0,b,steps)

E1=-100
E2=100

answer=brentq(Final_Value,E1,E2) #use brentq to solve for E-> psi=0 at b

print ('Eigenvalue found at E=%.8f'%answer)

plt.plot(x,y[:,0])
plt.xlabel("Position(Units of L)")
plt.show()






