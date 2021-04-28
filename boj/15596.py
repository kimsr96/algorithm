def self_num(a):
    arr = list(str(a))
    total = a
    for i in range(len(arr)):
        total += int(arr[i])
    return total

result = list(range(1,10000))
n = 1
while (n < 10000):
    try:
        result.remove(self_num(n))
    except:
        n += 1
        continue
    n += 1

for i in result:
    print(i)
