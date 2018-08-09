__author__ = 'Nicat'
user_array=[]


#=======================================================
class PERM:
    cluser_array=[]
    def __init__(self,cluser_array):
        self.cluser_array=cluser_array

    def permutation(self):
        perm_array=[]
        for i in range (0,len(self.cluser_array)):
           for j in range (0,len(self.cluser_array)):
               if self.cluser_array[i]==self.cluser_array[j]:
                   pass
               else:
                a=str(self.cluser_array[i])+str(self.cluser_array[j])
                b=int(a)
                perm_array.append(b)

        print("PERMUTATION ARRAY")
        print(perm_array)

#======================================================
print("Please input one line two positive integers separeted by a space n m ")
print("NOTE:0<m<n<20")
a=input("input n m >>")
h=a.find(" ",0,len(a))
n=int(a[0:h])
m=int(a[h+1:])
print("First integer:",n)
print("Second integer:",m)

while n<0 or m<0 or n>20 or m>n:
    print("WARNING, the integers must be 0<m<n<20 type ")
    a=input("input n m >>")
    h=a.find(" ",0,len(a))
    n=int(a[0:h])
    m=int(a[h+1:])


print("Congratulations,this is true type of integers ",n ," and ",m)
print("the integer set is:")
for i in range(1,n+1):
    if i==n:
       print(i,"}")
    elif i==1:
        print("{",i,end=",")
    else:
        print(i,end=",")


for j in range(1,n+1):
    user_array.append(j)
print("array type:")
print(user_array)

d=PERM(user_array)
d.permutation()
print("======================")
print("NIJAT SHUKUROV")
print("id:1784222")
print("All rights recerved (c)")

import os
os.system('pause')










