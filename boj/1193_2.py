import pprint

n = int(input())
arr= [[0] * n] * n

for i in range(n):
    for j in range(n):
        arr[i][j] = j + 1

print(len(arr))