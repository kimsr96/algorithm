n = int(input())

sum = 1
cnt = 1
i = 1

while True:
    if n > sum:
        sum += (6 * i)
        i += 1
    elif n <= sum:
        break
    cnt += 1

arr = [i for i in range(sum - (6 * (i-1)) + 1, sum + 1)]
arr2 = list(reversed(arr))
result_arr = []
num = 0

for j in range(len(arr2)):
    result_arr.append(num)
    if num == 0:
        num = cnt - 2
    else:
        num -= 1

result_arr.reverse()
cnt2 = result_arr[arr.index(n)]
print(result_arr, cnt2)
print(cnt + cnt2)
    