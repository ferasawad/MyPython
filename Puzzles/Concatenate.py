signs = ['+', '-']
for a in signs:
    for b in signs:
        for c in signs:
            for d in signs:
                print(eval('(81{}31{}9{}13{}4)/3'.format(a,b,c,d)))