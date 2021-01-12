top = list(input().split())
rule = list(input())
for i in range(len(top)): #입력을 각 단어로 나누기
    b = []
    a = list(top[i])
    cnt=0
    for j in range(len(top[i])): # 각 단어를 한 글자씩 나누기
        for idx,char in enumerate(rule): #rule을 인덱스로 바꾸기
            if a[j] == char:
                cnt +=1
                b.append(idx)
    if sorted(b) == b:
        print("가능")
    else: 
        print("불가능")