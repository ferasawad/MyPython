from random import *
from numpy import *
from math import *
from statistics import *
from matplotlib import pyplot as plt
import warnings

n = 4
N = 32
pc = 0.70
pm = 0.001
steps = 15

#chromosome generator
def chromosome():
    return [randint(0,1) for i in range(n)]

#population generator
def population():
    return [chromosome() for i in range(N)]

#transform chromosome from binary to decimal
def btod(x_child):
    return int("".join([str(i) for i in x_child]),2)

#function to be maximized
def f(x):
    return 16*x - x**2

#probability distribution
def pdf(x_pop):
    total = sum([f(btod(j)) for j in x_pop])
    prob  = [f(btod(j))/total for j in x_pop]
    return prob

#probability density
def cdf(x_pop):
    return cumsum(pdf(x_pop))

#cross over process
def crossover(x_pop):
    c = []
    for i in range(0,N,2):
        A = x_pop[i]
        B = x_pop[i+1]
        ctest = uniform(0,1)
        if ctest < pc:
            cut = randint(1,n)
            temp1 = A[:cut]
            temp2 = B[:cut]
            A[:cut] = temp2
            B[:cut] = temp1
            c.append(A)
            c.append(B)
        else:
            c.append(A)
            c.append(B)
    return c

#mutation process
def mutate(x_pop):
    npop = x_pop
    for i in range(N):
        if uniform(0,1) <= pm:
            gene = randint(0,n-1)
            if npop[i][gene] == 0:
                npop[i][gene] = 1
            else:
                npop[i][gene] = 0
    return npop
    
#define the score function = average fitness
def score(x_pop):
    return mean([f(btod(j)) for j in x_pop])

#generate the new population
def newpop(x_pop):
    npop = x_pop
    bestfit = score(npop)
    while True:
        candidates = choices(npop, cum_weights = cdf(npop), k = N)
        guesspop = mutate(crossover(candidates))
        newfit = score(guesspop)
        npop = guesspop
        if newfit < bestfit:
            continue
        else:
            break
    return npop


maxArr = []
avgArr = []

p = population()
sol = [btod(i) for i in p]
val = [f(i) for i in sol]

maxArr.append(max(val))
avgArr.append(mean(val))

print("Generation: %d" %0, '\t', "Max Value = %0.2f" %max(val), '\t', "Approximate = %0.4f" %mean(val))

for i in range(steps):
    p = newpop(p)
    warnings.simplefilter("ignore")
    sol = [btod(i) for i in p]
    val = [f(i) for i in sol]
    maxArr.append(max(val))
    avgArr.append(mean(val))
    print("Generation: %d" %(i+1), '\t', "Max Value = %0.2f" %max(val), '\t', "Approximate = %0.4f" %mean(val))
        
        

xval = [i for i in range(steps+1)]
plt.plot(xval, maxArr,'g-',label='exact')
plt.plot(xval, avgArr,'r--',label='approximate')
plt.xlabel("Generation")
plt.ylabel("Fitness")
plt.legend()
plt.show()
