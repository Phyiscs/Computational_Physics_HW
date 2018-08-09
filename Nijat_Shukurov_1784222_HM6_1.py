#name:Nijat
#surname:Shukurov
#id:1784222
#Homework 6 part 1_partA
#########################################
import numpy as np
import pylab as pl
import math
import matplotlib.pyplot as plt
import random



##part A
data=np.random.uniform(-math.pi,math.pi,10000)
print("part A random uniform numbers between -pi and +pi")
print(data)





##part_B
number=np.random.randint(0,1)
data_fx=[]
data_x=[]
def function(num):
    fx=5*num+3
    return fx

for a in range(0,10000):
    number=random.uniform(0,1)
    data_x.append(number)
    data_fx.append(function(number))
fig=plt.figure("Graphics")
ax1=fig.add_subplot(211)
ax1.plot(data_x,data_fx)
#ax1.xlabel("x")
#ax1.ylabel("F(x)")
#ax1.title('function plot x vs F(x)')




##part C
##mean and standart deviation for part A
b=max(data)##finds the max value
a=min(data)##finds the min value
mean_A=(a+b)/2
siqma_A=math.sqrt((b-a)/12)
print("Mean and standart deviation of part A ",mean_A,",",siqma_A)
##mean and standart deviation for part B
B=max(data_x)##finds the max value
A=min(data_x)##finds the min value
mean_B=(A+B)/2
siqma_B=math.sqrt((B-A)/12)
print("Mean and standart deviation of part B ",mean_B,",",siqma_B)



##part D
event_array=[]
func_array=[]
def f(x):##function
    if x>=0 and x<=math.pi:
        answer=math.sin(x)
    else:
        answer=0
    return answer

for i in range(0,10000):
    func_array.append(f(data_fx[i]))
ax2=fig.add_subplot(212)
ax2.plot(data_fx,func_array)
plt.show()
