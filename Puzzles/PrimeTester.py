from math import *

n = int(eval(input('Enter an integer : ')))

while n<=0:
    print("Error. ",end="")
    n = int(input('Please enter a positive integer : '))

for i in range(2,round(sqrt(n))+1):
    if n%i == 0:
        print("Your number ", n, " is not a prime")
        print("since it is divisible by ", i)
        break
else:
    print(n," is prime !!")
