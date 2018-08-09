__author__ = 'Nicat'
##Nicat Shukurov 1784222
## this program uses treading class to stop the calculation when we want
# ,when the program startes the calculation of PI number startes at the same time and at the same time
# we can input anything to stop calculation loop and print the result. program will stop
# after one hour calculation if you will not stop it.#
import threading
import math
print("PI=SUM[4x(1-1/(3+2n)+1/(5+2n)] , n is from 0 to infinite... ")
print("the program will calculate the pi for 1 hour \nto stop the calculation input anything")
print("============================================================")
print("input anything and press enter to stop the calculation")
##Functions ==========================================================================================
def calc_PI():
    global terminate ## this boolean using this we can terminate the threading
    A=-1/3
    B=1/5
    n=1
    while(terminate==False):##while there is no input the calculation will last
        A=float(A-1/(3+4*n))
        B=float(B+1/(5+4*n))
        n+=1
        pass

    PI=float(4*(1+A+B))
    print("Calculated PI number:",PI)
##Main function===============================================
global terminate
terminate=False
our_thread=threading.Thread(target=calc_PI)##defining the threading function
our_thread.start()#starting the threading function
print("!!!!!CALCULATION STARTED!!!!!")
input("input and press enter to stop calculation>>>")##just need any input to go other line
terminate=True##true stops the loop on calc_PI() function and prints the calculated PI number
print("Python math class PI number:",math.pi)

print("====================================================")
##for pause the command line
import os
os.system('pause')




