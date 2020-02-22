import random

dice = [1,2,3,4,5,6]

face1 = 0
face2 = 0
face3 = 0
face4 = 0
face5 = 0
face6 = 0

rolls = int(input('How many rolls you need ? '))

for i in range(rolls):
    face = random.randint(1,6)
    if face==dice[0]:
        face1+=1
    elif face==dice[1]:
        face2+=1
    elif face==dice[2]:
        face3+=1
    elif face==dice[3]:
        face4+=1
    elif face==dice[4]:
        face5+=1
    elif face==dice[5]:
        face6+=1

faces = [face1,face2,face3,face4,face5,face6]

print('Num.\tFreq.')
for i in range(6):
    print(dice[i],'\t',faces[i])

