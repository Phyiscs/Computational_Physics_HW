__author__ = 'Nicat'
##Name:Nijat
#Surname:Shukurov
#ID:1784222
#HW3 part 2 Subclasses
## in this program Square is the subclass of the Shape and both of
##classes has the int Area() method.
##================================================================
##classes
class Shape:
    def __init__(self,length=0):
        self.length=length
    def Area(self):
        return int(self.length)*int(self.length)
class Square(Shape):
    def __init__(self,length):
        super(Square, self).__init__(length)
        self.length=length
    def Area(self):
        return int(self.length)*int(self.length)
##Main function====================================================
length=input("input the lenght in (m) >>")##input the lenght
area=Shape(length)##add length as argument of shape class

print("AREA:",area.Area(),"m^2")#3prints the iinformations
## pause the command line
import os
os.system('pause')