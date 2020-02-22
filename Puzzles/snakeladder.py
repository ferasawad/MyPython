
def ladder(num):
    if num == 4:
        return 14
    elif num == 9:
        return 31
    elif num == 20:
        return 38
    elif num == 28:
        return 84
    elif num == 40:
        return 59
    elif num == 51:
        return 67
    elif num == 63:
        return 81
    else:
        return 91


def snake(num):
    if num == 99:
        return 78
    elif num == 95:
        return 76
    elif num == 93:
        return 73
    elif num == 87:
        return 24
    elif num == 64:
        return 60
    elif num == 62:
        return 19
    elif num == 54:
        return 34
    else:
        return 7

from random import randint

curr_pos = 0
new_pos = 0
plist = []


while curr_pos < 100:
    new_pos = curr_pos + randint(1,6)
    if new_pos > 100:
        new_pos = curr_pos
        curr_pos = new_pos
    elif new_pos == 100:
        print('DONE !!')
        curr_pos = new_pos
    elif new_pos in [4,9,20,28,40,51,63,71]:
        curr_pos = ladder(new_pos)
    elif new_pos in [99,95,93,87,64,62,54,17]:
        curr_pos = snake(new_pos)
    else:
        curr_pos = new_pos
        
    plist.append(new_pos)

print('STEPS = ',len(plist))
print('SEQUENCE =\n',plist)
