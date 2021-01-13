a = int(input())    
b= [2,3,5,7]
for num in range(2,a):
    if num % 2 != 0 and num %3 != 0 and num %5 !=0 and num %7 !=0:
        b.append(num)
    
for i in b:
    for j in b:
        if i+j == a:
            print(i,j)
