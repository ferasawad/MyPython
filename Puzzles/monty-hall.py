from math import *
from random import *
import time

wonstay = 0
wonchange = 0

size = 1000000

while size <= 0:
    print('Wrong choice. Your number should be a positive integer.')
    size = int(input('How many simulations you need ? \n'))

decision = ['Y','N']

beginT = time.time()

for counter in range(size):
    prize = randint(1, 3)
    yourchoice = randint(1, 3)
    stay = randint(0,1)

    if prize == yourchoice and decision[stay] == 'Y':
        wonstay += 1
    elif prize != yourchoice and decision[stay] == 'N':
        wonchange += 1

endT = time.time()

wonstayP = round(100 * wonstay/(wonstay+wonchange),2)
wonchangeP = round(100 *wonchange/(wonstay+wonchange),2)
processT = round(endT - beginT,3)

print('After',processT,'seconds of',size,'trials:')
print('You will win with probabilit',wonstayP,'%', 'if you stay,')
print('while you will win with probabilit',wonchangeP,'%', 'if you change.')