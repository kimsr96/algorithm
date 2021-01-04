a = [str(i) for i in range(1,101)]
b = ''.join(a)
c = [int(y) for y in b ]
result =0
for j in c:
    result += j
print(result)