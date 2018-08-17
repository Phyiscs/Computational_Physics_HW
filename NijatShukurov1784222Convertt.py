__author__ = 'Nicat'
## name:NIJAT
#  surname:SHUKUROV
#  ID:1784222
#  PHYS 443 COMPUTATIONAL PHYSICS
#  HOMEWORK 1##

##using this program
# you can convet
# Fahraneit F to C or vice versa##
#=====================================
##FUNCTIONS:
## this function converts C to F
def CeltoFahr(c):
    f=c*9/5 + 32
    print(c," C" ," is ",f," F...")

## this function converts F to C
def FahrtoCel(f):
    c=(f-32)*5/9
    print(f," F" ," is ",c," C...")
#======================================

print("Please input 'F' for Fahraneit to Celsius");
print("Please input 'C' for Celsius to Fahraneit");
print("Please input 'E' for exit")
#========================================
#inputs the command
a=input("input 'F' or 'C'")
#cheks if a is F
while a!='E':

    if a=='C':
        cels=input("Please input C number >>")
        int_cels=int(cels)
        CeltoFahr(int_cels)
        a=input("input 'F' or 'C' and 'E' for exit")
#cheks if a is C
    elif a=='F':
        fahr=input("Please input F number >>")
        int_farh=int(fahr)
        FahrtoCel(int_farh)
        a=input("input 'F' or 'C' and 'E' for exit")
    else:
        print("why u do this what is ",">>",a,"<<<","i cant understand it come on try it again :D")
        print("and please enter F or C ")
        a=input("input 'F' or 'C' and 'E' for exit")






