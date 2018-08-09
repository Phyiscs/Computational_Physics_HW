#name:Nijat
#surname:Shukurov
#id:1784222
#Homework 5 part A
#########################################
import numpy as np
import pylab as pl
import random
arraylist=[]
#########################################
def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num
prob_of_sucsess=0.2
prob_of_fail=0.8
N_trial=50
for i in range(1,N_trial+1):
    random_number=random.randint(-1,21)
    probability=factorial(N_trial)/(factorial(random_number)*factorial(N_trial-random_number))*((prob_of_sucsess)**random_number)*((prob_of_fail)**(N_trial-random_number))
    arraylist.append(probability)
def printlist(array_list):
    for i  in range(0,len(array_list)):
        print(array_list[i])

printlist(arraylist)


