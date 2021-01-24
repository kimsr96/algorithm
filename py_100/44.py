# a = list(input())
# a = [int (i) for i in a]
# sum=0
# for i in a:
#     sum += i
# print(sum)

result = 0
for i in input():
    result += int(i)
print(result)

####################
n = list(map(int,input()))
result = 0
for i in n:
	result += i
	
print(result)
