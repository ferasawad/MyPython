
n = int(input('Enter a positive integer : '))

print('STEP', 0, ': ',n)

def digit_mult(n,steps=0):
    if len(str(n)) == 1:
        return "Done"

    result = 1
    steps+=1
    for i in str(n):
        result *= int(i)
    print('STEP', steps, ': ',result)
    digit_mult(result,steps)

digit_mult(n)