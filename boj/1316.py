n = int(input())

cnt = 0
for i in range(n):
    data = input()
    arr = [data[0]]
    for j in range(1,len(data)):
        if data[j] not in arr:
           arr.append(data[j])
        else:
            if data[j - 1] == data[j]:
                continue
            else:
                cnt += 1
                break
print(n - cnt)