#
#   FIXED-POINT ALGORITHM 2.2
#
#   To find a solution to p = g(p) given an
#   initial approximation p0
#
#   INPUT:  initial approximation; tolerance tol;
#           maximum number of iterations maxN.
#
#   OUTPUT: approximate solution P or 
#           a message that the method fails.
#


#   Add libraries
from math import *
from matplotlib import pyplot as plt
from numpy import *
from mpl_toolkits.axisartist.axislines import SubplotZero


#   Change function f for a new problem
def g(x):
    return sqrt(10.0 / (4.0 + x))

#   Draw function f
def myplot(P):
    plt.xkcd()
    fig = plt.figure()
    ax = SubplotZero(fig, 111)
    fig.add_subplot(ax)
    plt.axhline(y=0, color='#636363')
    plt.axvline(x=0, color='#636363')
    ax.set(xlabel='$x$', ylabel='$g(x)$', title='Fixed-Point Method')
    x = arange(P-2*abs(P),P+2*abs(P),0.01)
    yg = [g(i) for i in x]
    yx = x
    ax.plot(x,yg,label='$g(x)$')
    ax.plot(x,yx,label='$x$')
    ax.plot([P], [g(P)], 'ro-',label='root')
    ax.legend()
    plt.show()

print("This is the Fixed-Point Method.\n")
print("Has the function g been created in the program")
print("immediately preceding the INPUT function?\n")

AA = input("Enter Y or N :\n")

if AA == 'Y' or AA == 'y':
    #   PART[1] : INPUT
    #   Initial approximation P0
    P0 = float(input('Input initial approximation: \n'))

    #   PART[2] : INPUT
    #   The tolerance or accuracy
    OK = False
    while not OK:
        tol = float(input('Input tolerance:\n'))
        if tol < 0.0:
            print("Tolerance must be positive\n")
        else:
            OK = True

    #   PART[3] : INPUT
    #   Maximum number of iterations
    OK = False
    while not OK:
        maxN = int(
            input("Input maximum number of iterations - no decimal point.\n"))
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
    #   The Fixed-Point method
    if OK:
        i = 1
        OK = True
        if flag == 2:
            print('{:<10} {:<20} {:<21}'.format('Iteration','P','Error'))
            print('{:-<10} {:-<20} {:-<21}'.format('','',''))
        while i <= maxN and OK:
            P = g(P0)
            if abs(P-P0) < tol:
                if flag == 2:
                    print('{:<10} {:<20} {:<21}'.format(i,P,abs(P-P0)))
                print("\nApproximate solution P = ", P)
                print("Number of iterations = ", i)
                print("Tolerance = ", tol)
                if fplot == 'Y' or fplot == 'y':
                    myplot(P)
                OK = False
            else:
                if flag == 2:
                    print('{:<10} {:<20} {:<21}'.format(i,P,abs(P-P0)))
                i = i + 1
                P0 = P
        if OK:
            print("\nIteration number ", maxN)
            print("gave approximation ", P)
            print("not within tolerance : ", tol)


else:
    print("The program will end so that the function g can be created\n")
    OK = False
