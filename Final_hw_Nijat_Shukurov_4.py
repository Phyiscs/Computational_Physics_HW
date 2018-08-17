##Name:Nicat
##Surname:Shukurov
## FINAL HOMEWORK 4
import math
from pylab import *
##=================================
h=0.3
## 0<x<3
u_data=[]
u_data.append(0)
dudx_data=[]
x_data=arange(0,3.3,0.3)## arange x from 0 to 3 by 0.3
##u array for runga kutta
u_data_runge=zeros(len(x_data))
u_data_runge[0]=1 ## the first element of array is 1

##u array for euler
u_data_euler=zeros(len(x_data))
u_data_euler[0]=1## the first element of array is 1

##u array for analtic
u_data_analtic=zeros(len(x_data))
u_data_analtic[0]=1## the first element of array is 1

##Function======================================
## du/dx fucntion
def dudx(u,x):
    return (x**2)*math.e**(-u-1)
## the u(x) function founded by analtic method
def u(x):
    return log((x**3)/3+e**2)-1
## Runge kutta==================================
def runge_kutta(u,x,dx,derivation):
   for a in range(len(x)-1):
      k1=dx*derivation(u[a],x[a])
      k2=dx*derivation(u[a]+0.5*k1,x[a]+dx*0.5)
      k3=dx*derivation(u[a]+0.5*k2,x[a]+dx*0.5)
      k4=dx*derivation(u[a]+k3,x[a]+dx)
      u[a+1]=u[a]+(k1+2*k2+2*k3+k4)/6
   return u
##==============================
## Euler method=================================
def euler_method(u,x,dx,derivation):
    for a in range(len(x)-1):
        u[a+1]=u[a]+dx*derivation(u[a],x[a])
    return u
##===============================
## Analytic method==============================
for i in range(len(x_data)):
    u_data_analtic[i]=u(x_data[i])
##===============================
##plotting the graph
plt.plot(x_data,u_data_runge,color='g',label="runge kutta")
plt.plot(x_data,u_data_euler,color='b',label="euler")
plt.plot(x_data,u_data_analtic,color='r',label="analtic")
plt.legend(loc="upper left")
plt.show()
## end