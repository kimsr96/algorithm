T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    n = 2
    x += 1
    y -= 1
    d = y - x
    cnt = 0

    for i in range(d):
        x += n
        n += 1
        cnt += 1
        if x >= y:
            break
    
    if d <= 0:
        cnt = d
    print(cnt + 2)
