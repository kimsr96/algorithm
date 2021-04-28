n = list(input())
cnt = 1
while(n[0] == ' '):
    if len(n) == 1:
        print(0)
        exit()
    del n[0]

for i in range(1, len(n)):
    try:
        if n[i] != ' ' and n[i - 1] == ' ':
            cnt += 1
    except:
        continue
print(cnt)

