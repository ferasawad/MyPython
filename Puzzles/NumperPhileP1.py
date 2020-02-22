from random import *

simulations = int(input('How many simulations you need ? '))

#Outputs of Win
output1 = [1,1,1]
output2 = [1,1,0]
WinSet = [output1,output2]

#Outputs of Lose
output3 = [0,1,1]
output4 = [0,1,0]
output5 = [1,0,1]
LoseSet = [output3,output4,output5]

#Outputs of Repeat
output6 = [1,0,0]
output7 = [0,0,1]
output8 = [0,0,0]
RepeatSet = [output6,output7,output8]

win = 0
lose = 0

for i in range(simulations):
    flipping = sample([output6,output5,output4,output3,output2,output1,output7,output8],1)
    if flipping[0] in WinSet:
        win = win + 1
    else:
        if flipping[0] in LoseSet:
            lose = lose + 1

print('Probability of WIN  =\t',100*win/(win+lose))
print('Probability of LOSE =\t',100*lose/(win+lose))