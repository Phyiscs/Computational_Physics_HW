__author__ = 'Nicat'
##Name:Nijat
#Surname:Shukurov
#ID:1784222
#HW3 Rectangle class
#==============================================================
##Classes
class Rectangle:
    ##Rectangle class has a fucntion compute_area()
    #using this function we compute the area of any Rectangle #
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def compute_area(self):
        return int(self.length)*int(self.width)##return integer
##=============================================================

##Main class
rec_length=input("Please , enter the length of Rectangle in (m) >>")##Input the length

rec_width=input("Please , enter the width of Rectangle in (m) >>")##Input the width
rec=Rectangle(rec_length,rec_width)## calling the class and defining the arguments in int
print("The parameters of a Rectangle:\nLENGTH:",rec_length,"m","\nWIDTH:",rec_width,"m","\nAREA:",rec.compute_area(),"m^2")
print("All rights reserved (c)")
import os
os.system('pause')

