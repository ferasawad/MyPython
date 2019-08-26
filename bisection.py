#
#   BISECTION ALGORITHM
#
#   To find a solution to f(x) = 0 given the continuous function
#   f on the interval [a,b], where f(a) and f(b) have opposite signs:
#
#   INPUT:   endpoints a,b; tolerance TOL;
#            maximum number of iterations N0.
#
#   OUTPUT:  approximate solution p or
#            a message that the algorithm fails.
#


#   Add math library
from math import *

#   Change function f for a new problem


def f(x):
    #fval = (x + 4.0) * (x**2) - 10.0
    fval = log(x) + x
    return fval


print("This is the Bisection Method.\n")
print("Has the function F been created in the program")
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
    #   The Bisection method
    if OK:
        i = 1
        OK = True
        while i <= maxN and OK:
            C = (B - A) / 2.0
            P = A + C
            fP = f(P)
            if abs(fP) == 0.0 or C < tol:
                print("\nApproximate solution P = ", P)
                print("with f(P) = ", fP)
                print("Number of iterations = ", i)
                print("Tolerance = ", tol)
                OK = False
            else:
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


else:
    print("The program will end so that the function f can be created\n")
    OK = False
