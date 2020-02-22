#
#   BISECTION ALGORITHM
#
#   To find a solution to f(x) = 0 given the continuous function
#   f on the interval [a,b], where f(a) and f(b) have opposite signs:
#
#   INPUT:   endpoints A,B; tolerance tol;
#            maximum number of iterations maxN.
#
#   OUTPUT:  approximate solution P or
#            a message that the algorithm fails.
#


#   Add libraries
from math import *
from matplotlib import pyplot as plt
from numpy import *
from mpl_toolkits.axisartist.axislines import SubplotZero

#   Change function f for a new problem
def f(x): 
    return x**2 * (x + 4) - 10.0

#   Draw function f
def myplot(P):
    plt.xkcd()
    fig = plt.figure()
    ax = SubplotZero(fig, 111)
    fig.add_subplot(ax)
    plt.axhline(y=0, color='#636363')
    plt.axvline(x=0, color='#636363')
    ax.set(xlabel='$x$', ylabel='$f(x)$', title='Bisection Method')
    x = arange(P-2*abs(P),P+2*abs(P),0.01)
    y = [f(i) for i in x]
    ax.plot(x,y,label='$f(x)$')
    ax.plot([P], [0], 'ro-',label='root')
    ax.legend()
    plt.show()


print("This is the Bisection Method.\n")
print("Has the function f been created in the program")
print("immediately preceding the INPUT function?\n")

AA = input("Enter Y or N :\n")

if AA == 'Y' or AA == 'y':
    #   PART[1] : INPUT
    #   Interval endpoints A and B,
    #   where A < B and f(A)*f(B) < 0
    OK = False
    while not OK:
        A = float(input('Enter left endpoint A: \n'))
        B = float(input('Enter right endpoint B:\n'))
        if A > B:
            temp = A
            A = B
            B = temp
        elif A == B:
            print("\nA cannot equal B. Try again. \n")
        else:
            fA = f(A)
            fB = f(B)
            if fA * fB > 0.0:
                print("\nf(A) and f(B) have same sign. Try again. \n")
            elif fA == 0.0 or fB == 0.0:
                print("\nf has root at one of the endpoints. \n")
                OK = True
            else:
                OK = True

    #   PART[2] : INPUT
    #   The tolerance or accuracy
    OK = False
    while not OK:
        tol = float(input('Input tolerance:\n'))
        if tol < 0.0:
            print("Tolerance must be positive\n")
        else:
            print('NOTE: you need at least', int(ceil(log((B-A)/tol)/log(2))), 'iterations.\n')
            OK = True

    #   PART[3] : INPUT
    #   Maximum number of iterations
    OK = False
    while not OK:
        maxN = int(input("Input maximum number of iterations - no decimal point.\n"))
        if maxN <= 0:
            print("Must be positive integer\n")
        else:
            OK = True

    #   PART[4] : OUTPUT
    #   Detail or summary
    OK = False
    while not OK:
        flag = int(input('Select type of output\n1. Answer only\n2. All intermeditate approximations\n'))
        if flag == 1 or flag == 2:
            OK = True
        else:
            print("Choose 1 or 2.\n")
    
    #   PART[5] : OUTPUT
    #   Plotting
    fplot = input("Grapgh the function? Enter Y or N :\n")
    

    #   PART[6] : OUTPUT
    #   The Bisection method
    if OK:
        i = 1
        OK = True
        if flag == 2:
            print('{:<10} {:<20} {:<20} {:<20} {:<21}'.format('Iteration','A','B','P','Error'))
            print('{:-<10} {:-<20} {:-<20} {:-<20} {:-<21}'.format('','','','',''))
        while i <= maxN and OK:
            C = (B - A) / 2.0
            P = A + C
            fP = f(P)
            if abs(fP) == 0.0 or C < tol:
                if flag == 2:
                    print('{:<10} {:<20} {:<20} {:<20} {:<21}'.format(i,A,B,P,abs(fP)))
                print("\nApproximate solution P = ", P)
                print("with f(P) = ", fP)
                print("Number of iterations = ", i)
                print("Tolerance = ", tol)
                if fplot == 'Y' or fplot == 'y':
                    myplot(P)
                OK = False
            else:
                if flag == 2:
                    print('{:<10} {:<20} {:<20} {:<20} {:<21}'.format(i,A,B,P,abs(fP)))
                i = i + 1
                if fA*fP > 0.0:
                    A = P
                    fA = fP
                else:
                    B = P
                    fB = fP
        if OK:
            print("\nIteration number ", maxN)
            print("gave approximation ", P)
            print("f(P) = ", fP)
            print("not within tolerance : ", tol)
            if fplot == 'Y' or fplot == 'y':
                    myplot(A,B,P)


else:
    print("The program will end so that the function f can be created\n")
    OK = False