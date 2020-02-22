#Install pulp package by typing the following in Terminal
#pip install pulp
from pulp import *

#Create the LP Problem
lp = LpProblem("testLP", LpMaximize)

#Define the Variables
x1 = LpVariable("x1",lowBound=0,upBound=None)
x2 = LpVariable("x2",lowBound=0,upBound=None)

#The Objective Function
lp += 20*x1 + 30*x2

#The Constraints
lp += 1*x1 + 2*x2 <= 100
lp += 2*x1 + 1*x2 <= 100

# The problem data is written to an .lp file
lp.writeLP("testLP.lp")

#To Display the LP Problem
print(lp)

#Solve with Default Solver
status = lp.solve()
print(LpStatus[status])

# Each of the variables is printed with it's resolved optimum value
for v in lp.variables():
    print(v.name, "=", v.varValue)

# The optimised objective function value is printed to the screen
print("The Optimal Objective Function Value = ", value(lp.objective))