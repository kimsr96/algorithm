n = int(input())

for _ in range(n):
    f = int(input())
    r = int(input())
    arr = [r for r in range(1, r + 1)]
    for i in range(f):
        arr_next = []
        total = 0
        for j in arr:
            total += j
            arr_next.append(total)
        arr = arr_next
    print(arr[r-1])
