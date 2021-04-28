n = int(input())

for i in range(n):
    arr = list(input().split())
    arr2 = list(arr[1])
    for j in range(len(arr[1])):
        print(arr2[j] * int(arr[0]), end='')
    print()