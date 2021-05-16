def endgame(n, cnt):
    if n - 1 == 0:
        return cnt
    return endgame(n - 1, cnt + 1)

n = int(input())
cnt = 0
if n == 1:
    print(666)
else:
    print(str(endgame(n, cnt)) + '666')
