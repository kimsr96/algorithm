T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    arr = [0, 1, 2]
    n = 2
    x += 1
    y -= 1
    d = y - x
    cnt = 0 

    for i in range(d):
        for idx in range(2, -1, -1):
            if x + arr[idx] <= y:
                x += arr[idx]
                cnt += 1
                break
        if x == y:
            break
        arr.pop(0)
        n += 1
        arr.append(n)
    
    if d <= 0:
        cnt = d
    print(cnt + 2)
