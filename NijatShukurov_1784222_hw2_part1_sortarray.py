__author__ = 'Nicat'
## NIJAT SHUKUROV
#  ID:1784222
#  HOMEWORK 1 PART 1
#  write mysort function #

#EXPLANATION:
#I CREATED MYSORT CLASS AND array_sort() method to sort array
# there is own allogritma in this method/funtion to sort
# array numbers. #

##==============================
## THIS IS MYSORT CLASS
class MYSORT:
    array=[]
    #defines which type variable MYSORT CLASS will use
    def __init__(self,array):
        self.array=array
    # array_sort fucntion to sort arrays.
    def array_sort(self):
        #takes  member to loop and cheks
        for i in range (0,len(self.array)):
            #by taking first member to loop checks this member by comparing with other members in loop
            for j in range(0,len(self.array)):
                # if taken member is smaller than member which next to it changes the places of this members
                if self.array[i] < self.array[j]:
                    a=self.array[i]
                    b=self.array[j]
                    self.array[i]=b
                    self.array[j]=a
                # if taken member is bigger than member which next to it dont do anything
                elif self.array[i] > self.array[j]:
                    pass
                #if taken member is same as member which next to it dont do anything
                elif self.array[i] == self.array[j]:
                    pass
        print("sorted array:")
        print(self.array)

##===============================

##MAIN FUNCTION
#variables
use_array=[]
print("Hello using this program you can extend your array how much you want and sorting all member from small to big")

b=0;
## using while program inputs the array memmbers
while b!=-1:##-1 never can be added in array

    a=input("Please, insert array member or and  '-1' to finish extend>>")
    b=int(a)

    if b!=-1:##using this if statement -1 never added to the array
        use_array.append(b)
    else:
        pass

print("the array which you entered")
print(use_array)

# we import MYSORT CLASS
d=MYSORT(use_array)
# USING array_sort method of MYSORT CLASS
d.array_sort()
print("=========================")
print("NICAT SHUKUROV")
print("ID 1784222")
print("all rights reserved (c)")
print("have a nice day :D")
# for pause the command line screen
import os
os.system('pause')











