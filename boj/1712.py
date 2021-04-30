a, b, c = map(int, input().split())

total = 1 

if b >= c:
    print(-1)
    exit()
else:
    total += a // (c - b)
    print(total)