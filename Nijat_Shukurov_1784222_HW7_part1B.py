##Name:NIJAT
##Surname:Shukurov
##ID:1784222
##Homework 7 part1 b
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
##Life time calculating
##D=[sum(1/siqma^2)*sum(ti*yi*/siqma^2)-sum(yi/siqma^2)*sum(ti/siqma^2)]/[sum(1/siqma^2)*sum(ti^2/siqma^2)-sum(ti/siqma^2)*sum(ti/siqma^2)]
## Lifetime=-1/D
D=(one_over_sum_Ni*ti_yi_over_sum_Ni-yi_over_sum_Ni*ti_over_sum_Ni)/(one_over_sum_Ni*ti_ti_over_sum_Ni-ti_over_sum_Ni*ti_over_sum_Ni)
lifetime=-1/D
## error calculating
##sd_square=sum(1/siqma^2)/[sum(1/siqma^2)*sum(ti^2/siqma^2)-sum(ti/siqma^2)*sum(ti/siqma^2)]
sd_square=one_over_sum_Ni/(one_over_sum_Ni*ti_ti_over_sum_Ni-ti_over_sum_Ni*ti_over_sum_Ni)
error=sqrt(sd_square)/(D*D)
## X2 calculation
lnA=4.725
A=112.73
X2=0
for i in range(0,10):
    X2=X2+((Ni_data[i]-A*exp(-ti_data[i]/lifetime))*(Ni_data[i]-A*exp(-ti_data[i]/lifetime)))/(A*exp(-ti_data[i]/lifetime))
print("X2:",X2)
dof=8
X2_per_dof=X2/dof
print("the X2 per dof : ",X2_per_dof)

