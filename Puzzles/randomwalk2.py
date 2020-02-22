from random import randint
from turtle import *

#shape('circle')
STEPS = 1000000
speed(0)

for i in range(STEPS):
    x = randint(-1,1)
    y = randint(-1,1)
    setx(xcor()+x)
    sety(ycor()+y)
