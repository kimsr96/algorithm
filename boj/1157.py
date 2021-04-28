word = list(input())

for idx in range(len(word)):
    if ord(word[idx]) < ord('A') or ord(word[idx]) > ord('z'):
        exit()

cnt = []
for i in range(ord('z') - ord('a') + 1):
    c = ord('a') + i
    cnt.append(word.count(chr(c)) + word.count(chr(c - 32)))

err = cnt.count(max(cnt))
result = cnt.index(max(cnt))

if err != 1:
    print("?")
    exit()
 
print(chr(ord('A')+result)) 




