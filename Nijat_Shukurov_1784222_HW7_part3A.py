__author__ = 'Nicat'
##Name:NIJAT
##Surname:Shukurov
##ID:1784222
##Homework 7 part3
# partA  Calculate the average & compute the average number events expected in an interval.
import numpy as np
import pylab as pl
from math import *
data=np.loadtxt("hm7part3data.txt","i")
event=data[:,0]
intervals=data[:,1]
##calculate average
up=0
a=0
for i in range(0,10):
    up=up+intervals[i]
    a=a+1
average=up/a
print("average ", average)

##calculating average number event
upper_part_sum=0
sum_intervals=0
for i in range(0,10):
    upper_part_sum=upper_part_sum+event[i]*intervals[i]
    sum_intervals=sum_intervals+intervals[i]
average_number_event=upper_part_sum/sum_intervals

print("average number events:",average_number_event)
##part B
##Calculate a ? considering first nine data and assuming the data are described by a Poisson distribution.

def fac(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

#The predicted number of intervals is given by:
num_intervals=sum_intervals*exp(-average_number_event)*average_number_event**(8)/fac(8)
print("intervals:",num_intervals)
X2=0;
for a in range(0,8):

    X2=X2+((num_intervals)-average_number_event)**2/average_number_event

print(X2)
