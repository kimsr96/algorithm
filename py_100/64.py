n = int(input())

a = int(n/7)
b = n - (a*7)
c = int(b/3)



if n == (a*7)+(c*3):
    print(a+c)
else:
    print(-1)