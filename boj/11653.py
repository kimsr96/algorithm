n = int(input())

total = 1

if n == 1:
    exit()

def check_prime(i):
    cnt = 0
    k = 2
    arr = []
    while(k * k <= i):
        if i % k ==0:
            arr.append(i)
    if len(arr) == 1:
        return 1

i = 2 
num = n
while(True):
    if n % i == 0:
        if (check_prime(i)):
            total *= i
            if total == num:
                break
                n //= i
                print(i)
                i = 2
                continue
    i += 1
