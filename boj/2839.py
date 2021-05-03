n = int(input())

a = n // 5
b = n % 5

for i in range(a, 0, -1):
    if (n - (i * 5)) % 3 == 0:
        a = i
        b = (n - (i * 5)) // 3
        print(a + b)
        exit()

if n % 3 == 0:
    print(n // 3)
    exit()
else:
    print(-1)
