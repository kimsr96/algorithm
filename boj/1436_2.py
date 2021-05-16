def endgame(n):
    if n.count('6') == 0:
        return (str(int(n) - 1) + '666')

n = input()
if n == 1:
    print('666')
else:    
    print(endgame(n))