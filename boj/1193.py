n = int(input())
arr = []
arr2 = []
cnt = 0
for i in range(n):
    cnt += 1
    for j in range(1, cnt):
        arr.append([cnt - 1, cnt - j])
        # if cnt % 2 == 1:
        #     arr.append(cnt - j)
        #     arr2.append(j)
        # else:
        #     arr.append(j)
        #     arr2.append(cnt - j)

print(arr)
#print(arr2[n - 1], arr[n - 1])
