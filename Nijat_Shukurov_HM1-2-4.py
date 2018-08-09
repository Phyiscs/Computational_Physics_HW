##NAME: Nijat
##SURNAME: Shukurov
##id: 1784222
##homework 1 ,2-4
import scipy

def Hemisphere(x,y,a):
    #FUCNTION OF HEMISPHERE cheking if x**2 +y**2 smaller or equal than a**2
    #if yes returns the hemisphere fucntion
    #if not returns zero
    if scipy.sqrt(x**2+y**2) <= a:
        return abs(scipy.sqrt(a**2-x**2-y**2))
    else :
        return 0

##simple method for 3d volume
def simple_method_3d(f,a,n):
    ## giving boundary a fucntion itself gives boundary form-5 to 5 to x and y
    ## n gives you dx and dy distance
    print("Simple method running")
    dx=float(2*a)/n
    dy=float(2*a)/n
    dxdy=dx*dy # small rectangle
    summation=0.
    x=-a
    y=-a
    while x<=a and x>=-a:
        y=-a
        while y<=a and y>=-a:
            summation+=dxdy*f(x,y,a)
            y+=dy
        x+=dx
    return summation

print("volume of hemisphere======")
print(simple_method_3d(Hemisphere,2,1000))

