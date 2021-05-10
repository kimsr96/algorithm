n = int(input())
for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = ((x1 - x2) ** 2) + ((y1 - y2) ** 2)
    d1 = int(d ** (1 / 2))
    d2 = r1 + r2

    if d1 == 0 and r1 != r2:
        print(0)
    elif 
    elif d1 > d2:
        print(0)
    elif d1 == 0 and r1 == r2:
        print(-1)
    elif d1 == d2:
        print(1)
    elif d1 < d2:
        print(2)
    else:
        print(-1)