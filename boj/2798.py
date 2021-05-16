n, m = map(int, input().split())
arr = list(map(int, input().split()))
max_num = 0

for i in range(n):
    j = i + 1
    for j in range(i + 1, n):
        k = j + 1
        for k in range(j + 1, n):
            total = arr[i] + arr[j] + arr[k]
            if total == m:
                print(total)
                exit()
            elif total < m and max_num < total:
                max_num = total

print(max_num)