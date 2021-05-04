n = int(input())
arr = [int(x) for x in input().split()]
cnt = 0

for i in arr:
    if i == 1:
        cnt += 1
    j = 2
    while(j < i):
        if i % j == 0:
            cnt += 1
            break
        j += 1

print(n - cnt)
