from scipy.optimize import fsolve
from math import *

def triangleQ(x,y,z):
    if x+y>z and x+z>y and y+z>x:
        return True
    else:
        return False


def theSystem(variables):
    global x,y,z
    a, b, c = variables
    return (a**2 + b**2 - a*b - x**2, a**2 + c**2 - a*c - y**2, c**2 + b**2 - c*b - y**2)

x = 1
y = 2
z = sqrt(3)
sol = fsolve(theSystem, (0.0, 0.2, 1.2))
print(sol)