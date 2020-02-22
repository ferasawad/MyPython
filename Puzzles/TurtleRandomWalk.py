from turtle import *
from random import *

speed(0)

while True:
  guess = randint(1,4)
  if guess == 1:
    forward(5)
  elif guess == 2:
    backward(5)
  elif guess == 3:
    left(90)
  else:
    right(90)
