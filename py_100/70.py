a = tuple(input().split())
b = tuple(input().split())
# a = ([1,2],[2,4])
# b = ([1,0],[0,3])

    # c =  1, 2     e = 1,0
    # d =  2, 4     f = 0,3

if type(a) and type(b) == tuple:
    print(type(a))
    c,d = list(zip(*(a)))
    e,f = list(zip(*(b)))
    print(f"{[c[0]*e[0] + c[0]*f[0], c[0]*e[1]+c[1]*f[1]]},{[d[0]*e[0]+d[1]*f[0], d[0]*e[1]+d[1]*f[1]]}")
else:
    print(-1)