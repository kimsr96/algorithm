word = list(input())

for i in range(ord('z') - ord('a') + 1 ):
    c = chr(ord('a') + i)
    cnt = word.count(c)
    if cnt == 0:
        print("-1", end=' ')
        continue
    for j in range(len(word)):   
        if word[j] == c:
            print(j, end=' ')
            break
            
