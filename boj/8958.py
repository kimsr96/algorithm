n = int(input())

for i in range(n):
    arr = list(map(int, input().split()))
    student = arr[0]
    total = sum(arr) - arr[0]
    avg = total / student
    cnt = 0
    for j in range(1, arr[0] + 1):
        if arr[j] > avg:
            cnt += 1
    print("{:.3f}%".format(float((cnt / student) * 100)))