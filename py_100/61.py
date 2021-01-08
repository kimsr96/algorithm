a = list(input())

# for i in a:
#     cnt=0
#     for y in a:
#         if i==y:     
#             cnt+=1
#     print(i,cnt)
#     pass

for cnt,alpha in enumerate(a):
    if a[cnt] != a[cnt-1] or cnt == len(a):
        print(alpha,a.count(alpha))


        
