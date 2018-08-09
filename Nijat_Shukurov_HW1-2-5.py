#NAME:Nijat
#SURNAME:Shukurov
#id:1784222
#HOMEWORK 1 , 2-5
import random
data_x=[]
data_fx=[]
##generating 100000 times random number between 0 and 2
for a in range(0,10000):
    b=random.uniform(0,2)## generating random number
    data_x.append(b)## appending random number to the data_x
data_x.sort()##sorting data from small to big
##===============================================================
##fucntion uses data1 as x variable and creates y variables by adding them in data2 empty array
def fx(data1,data2):
    for i in range (0,len(data1)):##choosing range from zero to length of data1
        a=data1[i]*data1[i]+data1[i]## fucntion is y=x**2+x
        data2.append(a)##adding them to the data2.
    return data2
#calling the fx fucntion
fx(data_x,data_fx)#now we have data_x and data_fx
##================================================================
#SIMPSONS METHOD.....
def simpson(data_x,data_x2):
    sum=0.0
    carp=0
    for i in range(0,len(data_x)):
        #================================
        if i!=len(data_x)-1:
            dx=data_x[i+1]-data_x[i]
        else:
            dx=0
        #================================
        if i==0 or i==len(data_x):
            carp=1
        elif i%2==0 and i!= len(data_x)-1:
            carp=2
        else:
            carp=4
        #================================
        sum+=carp*dx*data_x2[i]
        #================================
    return (sum)/3


print(simpson(data_x,data_fx))

