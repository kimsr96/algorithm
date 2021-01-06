a = input()
num = int(len(a)/2)
b = 50 - len(a)
for i in range(0,b):
    if i==25-num+1:
        print(a,end="")
    else:
        print(f"{i}",end="")