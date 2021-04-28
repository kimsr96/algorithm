def han(a):
    chk = list(str(a))
    if (int(chk[2]) - int(chk[1])) == (int(chk[1]) - int(chk[0])):
        return 1
    else:
        return 0

n = int(input())
arr = list(range(1, n + 1))
total = 99
j = 100

if n < 100:
    print(n)
    exit()
else:
    while(j <= n):
        total += han(j) 
        j += 1
print(total)
