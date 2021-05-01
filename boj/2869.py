a, b, v = map(int, input().split())
n = v - a

while(True):
    if n % (a - b) != 0:
        n += 1
    else:
        break

cnt = n // (a - b)
print(cnt + 1)