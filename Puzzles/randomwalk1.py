from random import randint
from turtle import *

#shape('turtle')
STEPS = 1000000
speed(0)

for i in range(STEPS):
    choice = randint(1,4)
    if xcor() >= 300 or ycor() >= 300 or xcor() <= -300 or ycor() <= -300:
        backward(3)
    else:
        if choice == 1:
            forward(3)
        elif choice == 2:
            right(90)
        elif choice == 3:
            left(90)
        else:
            backward(3)
