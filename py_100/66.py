top = list(input().split())
rule = list(input())

for i in range(len(top)):
    # print(top[i],end='')
    a = list(top[i])
    for idx,char in enumerate(rule):
        print(zip(int(idx),char))
        

    print(rule)