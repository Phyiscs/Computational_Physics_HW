##Name:NIJAT
##Surname:Shukurov
##ID:1784222
##Homework 7 part1 a
import numpy as np
import pylab as pl
from math import *
## NOTE:
# N(t)=N(0)e^(-t/ta)
# ln(N(t))=ln(N(0))-t/ta
# y=C-Dt
# C=ln(N(0)) ; 1/ta=D
#  ##

data=np.loadtxt("hw7data.txt","d")## reads the data from hw7data.txt file
ti_data=data[:,1]## reads the second coloumn ti as array
yi_data=data[:,3]## reads the forth coloumn  yi as array
Ni_data=data[:,2]## reads the third coloumn  Ni as array
sum_ti=0
sum_ti_ti=0
sum_yi=0
sum_ti_ty=0
sum_Ni=0
one_over_sum_Ni=0
ti_yi_over_sum_Ni=0
yi_over_sum_Ni=0
ti_over_sum_Ni=0
ti_ti_over_sum_Ni=0
for i in range(0,10):
    one_over_sum_Ni=one_over_sum_Ni+Ni_data[i]## sum(1/siqma^2)
    ti_yi_over_sum_Ni=ti_yi_over_sum_Ni+ti_data[i]*yi_data[i]*Ni_data[i]## sum(ti*yi*/siqma^2)
    yi_over_sum_Ni=yi_over_sum_Ni+yi_data[i]*Ni_data[i]## sum(yi/siqma^2)
    ti_over_sum_Ni=ti_over_sum_Ni+ti_data[i]*Ni_data[i]## sum(ti/siqma^2)
    ti_ti_over_sum_Ni=ti_ti_over_sum_Ni+ti_data[i]*ti_data[i]*Ni_data[i]## sum(ti^2/siqma^2)
    ###################################################################
    sum_ti=sum_ti+ti_data[i]
    sum_yi=sum_yi+yi_data[i]
    sum_ti_ty=ti_data[i]*yi_data[i]
    sum_ti_ti=ti_data[i]*ti_data[i]
    sum_Ni=sum_Ni+Ni_data[i]
    ##################################################################
##Life time calculating
##D=[sum(1/siqma^2)*sum(ti*yi*/siqma^2)-sum(yi/siqma^2)*sum(ti/siqma^2)]/[sum(1/siqma^2)*sum(ti^2/siqma^2)-sum(ti/siqma^2)*sum(ti/siqma^2)]
## Lifetime=-1/D
D=(one_over_sum_Ni*ti_yi_over_sum_Ni-yi_over_sum_Ni*ti_over_sum_Ni)/(one_over_sum_Ni*ti_ti_over_sum_Ni-ti_over_sum_Ni*ti_over_sum_Ni)
lifetime=-1/D
print("lifetime: ",lifetime)
## error calculating
##sd_square=sum(1/siqma^2)/[sum(1/siqma^2)*sum(ti^2/siqma^2)-sum(ti/siqma^2)*sum(ti/siqma^2)]
sd_square=one_over_sum_Ni/(one_over_sum_Ni*ti_ti_over_sum_Ni-ti_over_sum_Ni*ti_over_sum_Ni)
error=sqrt(sd_square)/(D*D)
print("Error:",error)
print("lifetime:",lifetime,"+-",error)







