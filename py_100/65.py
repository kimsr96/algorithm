a = [1,2,3,4]
b = ["a","b","c","d"]

order = True

for i in range(len(a)):
    if i%2 == 1 :
        print([b[i],a[i]],end=',')
    else:
        print([a[i],b[i]],end=',')
