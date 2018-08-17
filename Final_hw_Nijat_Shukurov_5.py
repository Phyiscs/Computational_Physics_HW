##Name:Nicat
##Surname:Shukurov
## FINAL HOMEWORK 5
##=================================
import math
import pylab
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
##=================================
## arrays for graph data
x_data_graph=[]
t_data_graph=[]
u_data_graph=[]
## creating x data and t data
x=pylab.arange(3.4,4.2,0.1)
t=pylab.arange(0,5.1,0.1)
##creating u data as x t matrix
u_data=pylab.zeros([len(t),len(x)])
#=================================
for i in range(len(x)):
    if i>=1 and i<=7: ## counts data from 1st to 7
        u_data[0][i]=1 ## makes them equan to 1
    else: ## if it is not between 7 and 1
        pass ## then passes
#=================================

for a in range(len(t)-1):## counts t
    for b in range(len(x)-1): ## counts x as t const
        u_data[a+1][b]=0.5*u_data[a][b+1]+0.46*u_data[a][b] ## find u_data elements

##========================================================================
## as we found u data in x t matrix we cannot create 3d graph because of dimensiens of u_data x and t we should make dimensions same

## u_data is x t matrix and theere is x*t elements in matrix we should add them to one array with dim (x*t)
for a in range(len(t)):## while t changes
    for b in range(len(x)):## while t changes
        u_data_graph.append(u_data[a][b]) ## adds all u_Data matrix elements one by one to u_Data graph array

## as x dim is not same as x*t dimension for plotting graph we shpuld make it as (x*t) dim
for a in range(len(t)):## while t changes
    for b in range(len(x)):## while t changes
        x_data_graph.append(x[b])## adds x data from begging to end to the x_data_graph we x data comes to end
        ## then t changes in first loop then again same procses continus.

## as t data dim is not same as x*t dimension for plotting graph we shpuld make it as (x*t) dim
for a in range(len(t)):## wthile t changes
    for b in range(len(x)):## while t constant x changes
        t_data_graph.append(t[a])# adds t data from begging to end to the t_data_graph. when t data comes to end
        ## then t changes in first loop then again same procses continus.
##==========================================================================
## as we have same dimension of all data types then we can make graph
fig=plt.figure()
ax=fig.add_subplot(111, projection='3d')
ax.scatter(x_data_graph,t_data_graph,u_data_graph,color='b')
plt.show()

