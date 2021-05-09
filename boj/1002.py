n = int(input())
for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if x1 == y1 == x2 == y2  and r1 == r2:
        print(-1)
    elif (x1 == y1 == x2 == y2) and r1 != r2:
        print(0)
    else:
        x = -2 * (x1 - x2)
        y = -2 * (y1 - y2)
        right = (r1 ** 2) - (r2 ** 2) - ((x1 ** 2) - (x2 ** 2) + (y1 ** 2) - (y2 ** 2))
        if x == 0:
            y = right // y
        elif y == 0:
            x = right // x
        
        if (y ** 2) == (r1 ** 2) or (y ** 2) == (r2 ** 2) or (x ** 2) == (r1 ** 2) or (x ** 2) == (r2 ** 2):
            print(1)
        else:
            print(2)
