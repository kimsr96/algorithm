# a = int(input())
# l = [str(i) for i in range(1,a+1)]
# strl="".join(l)
# count = 0
# for i in list(strl):
#     if i == '1':
#         count+=1
# print(count)
########################
def count(n):
	countN = str(list(range(n+1))).count('1')
	return countN

print(count(1000))