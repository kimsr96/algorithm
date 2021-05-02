n = int(input())

for i in range(n):
    x, y, z = map(int, input().split())
    if z % x == 0:
        floor = x
        room = z // x
    else: 
        floor = z % x
        room = (z // x) + 1
    print("%d%02d" %(floor,room))

