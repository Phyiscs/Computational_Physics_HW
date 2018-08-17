__author__ = 'Nicat'
#NIJAT SHUKUROV
#ID:1784222
#HOMEWORK 2 PART 2#

#array variable
user_array=[]
#=======================================================
#CLASS PERM AND METHOD permutation to find permutation of any arraylist in main class
class PERM:
    cluser_array=[]
    def __init__(self,cluser_array):
        self.cluser_array=cluser_array

    def permutation(self):
        perm_array=[]
        for i in range (0,len(self.cluser_array)):
           for j in range (0,len(self.cluser_array)):
               if self.cluser_array[i]==self.cluser_array[j]:#if there is permutation of same integer it passes
                   pass
               else:
                a=str(self.cluser_array[i])+str(self.cluser_array[j])# adding integers as a string
                b=int(a)#chancing the string to integer
                perm_array.append(b)

        print("PERMUTATION ARRAY")
        print(perm_array)

#======================================================

print("Please input one line two positive integers separeted by a space n m ")
print("NOTE:0<m<n<20")
a=input("input n m >>")# input as string
h=a.find(" ",0,len(a))# finds the number of place where space character in string
n=int(a[0:h])#takes the strings from 0 to space character and converts to integer variable
m=int(a[h+1:])#takes the string from space character to the end of string and converts to integer variable
print("First integer:",n)
print("Second integer:",m)

while n<0 or m<0 or n>20 or m>n:#this loop works while 0<m<n<20 statement is not true
    print("WARNING, the integers must be 0<m<n<20 type ")
    a=input("input n m >>")
    h=a.find(" ",0,len(a))
    n=int(a[0:h])
    m=int(a[h+1:])

print("Congratulations,this is true type of integers ",n ," and ",m)
print("the integer set is:")

#prints the integer set in '{ }' brackets from 1 to n
for i in range(1,n+1):
    if i==n:
       print(i,"}")
    elif i==1:
        print("{",i,end=",")
    else:
        print(i,end=",")
#adds all integer variables in array and prints them
for j in range(1,n+1):
    user_array.append(j)
print("array type:")
print(user_array)

#imports the PERM class
d=PERM(user_array)
#uses the permutation() method/function of the PERM class
d.permutation()
#end of main fucntion

print("======================")
print("NIJAT SHUKUROV")
print("id:1784222")
print("All rights reserved (c)")
#pause the command line
import os
os.system('pause')










