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

print(cnt)