##Name:Nicat
##Surname:Shukurov
## FINAL HOMEWORK 2
##=================================
from scipy.integrate import odeint
from numpy import *
from pylab import *
L=10

V_data=[]
E=input("energy input")
L=input('input L')
def V(x):
    if x<=-int(L) or x>=int(L):
        return 0
    if x==0:
        return -50
    if x>-int(L) and x<0:
        return -50*((x+int(L))/int(L))
    if x>0 and x<int(L):
        return 50*((x-int(L))/int(L))


def deriv(psi,x):
    return array([psi[1],-2*(int(E)-V(x))*psi[0]])

x_data=linspace(-(int(L)+3),int(L)+3,2000)


psi_init=array([1.0,0.0])
psi=odeint(deriv,psi_init,x_data)

for a in range(len(x_data)):
    V_data.append(V(x_data[a]))


plot(x_data,psi[:,0],color='r')
plot(x_data,V_data,color='b')
ylim([-3,3])

title('Solution of schrodinger')
xlabel('$x$')
ylabel('$\psi(x)$')
      
show()
