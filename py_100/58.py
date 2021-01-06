# a = input()
# strl ="".join(reversed(a))
# listStr=list(strl)
# for i in range(len(listStr)):
#     if i%4 ==0:
#         listStr.insert(i+3,',')
# listStr.reverse()
# print(''.join(listStr))

n = int(input())

result = format(n, ',')
print(result)
