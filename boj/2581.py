m = int(input())
n = int(input())
arr = [i for i in range(m, n + 1)]
result = []
for j in arr:
    cnt = 0
    k = 1
    if j != 2 and j != 3 or j != 5 or j != 7:
        if j % 2 == 0 or j % 3 == 0 or j % 5 == 0 or j % 7 == 0:
            break
    while(k < j + 1):
        if j % k  == 0:
            cnt += 1
            if cnt > 2:
                break
            elif k == j and cnt == 2:
                result.append(j) 
        k += 1
if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(result[0])