##NAME: Nijat
##SURNAME: Shukurov
##id: 1784222
#HOMEWORK 1 , 2-7
from math import *
from matplotlib import pyplot

def f(a,b,n):
    #Function which generates array of number which differs from each other dx.
    data=[]
    dx=float(b-a)/n## you can choose dx by chancing n.
    while a<=b:
        data.append(a)
        a+=dx
    return data


def sinus(data):
    #Function using data as x variables returs data_x and data_y as y=cos(x)
    data_y=[]
    for i in range(len(data)):
        b=sin(data[i])
        data_y.append(b)
    pyplot.plot(data,data_y)
    pyplot.title("sinus fucntion")
    pyplot.show()
    return data ,data_y

def cosinus(data):
    #Function using data as x variables returs data_x and data_y as y=sin(x)
    data_y=[]
    for i in range(len(data)):
        b=cos(data[i])
        data_y.append(b)
    pyplot.plot(data,data_y)
    pyplot.title("cosinus fucntion")
    pyplot.show()
    return data,data_y


def derivative_f(data_x,data_y,title):
    der_data_y=[]
    dx=data_x[2]-data_x[1]
    for i in range(1,len(data_y)-1):
        der=(data_y[i+1]-data_y[i-1])/(2*dx)
        der_data_y.append(der)
    ##================
    del data_x[-1]
    del data_x[-1]
    ##================
    pyplot.plot(data_x,der_data_y)
    pyplot.title(title)
    pyplot.show()
data1,data2=cosinus(f(0,10,10000))
derivative_f(data1,data2,"derivative of cosunus function")
data1,data2=sinus(f(0,10,10000))
derivative_f(data1,data2,"derivative of sinus function")