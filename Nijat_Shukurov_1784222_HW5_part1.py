__author__ = 'Nicat'
import numpy as np
import pylab as pl
import random
dataarray=[]
def p(k):
    N=50
    ps=0.2
    pf=0.8
    probability=factorial(N)/(factorial(k)*factorial(N-k))*((ps)**k)*((pf)**(N-k))
    return probability

def factorial(number):
     if number == 0:
         return 1
     else:
         return number * factorial(number-1)


def arraylist_append():
    for i in range(0,20):
        dataarray.append(p(i))

arraylist_append()
for a in range(0,len(dataarray)):
    print(dataarray[a])

import os
os.system('pause')