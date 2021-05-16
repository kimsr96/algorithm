m = int(input())
arr = [int(i) for i in str(m)]
l = len(arr)

if m >= 20:
    n = m - (9 * l)
else:
    n = 1

while(n <= m):
    arr2 = [int(j) for j in str(n)]
    if n + sum(arr2) == m:
        print(n)
        exit()
    n += 1
print(0)
