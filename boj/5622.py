alpha = list(input())
dic = {}
num = 2
total = 0
for i in range(ord('Z') - ord('A') + 1):
    if i % 3 == 0 and num < 8:
        num += 1
    elif chr(ord('A') + i) == 'T':
        num += 1
    elif chr(ord('A') + i) == 'W':
        num += 1
    dic[chr(ord('A') + i)] = num

for a in alpha:
    total += dic[a]

print(total)