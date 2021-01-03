weight = int(input())
n = int(input())
num_list = list(map(int, input().split()))
sum =0
count = 0
for j in range(n):
    for i in range(len(num_list)):
        if sum < weight:
            sum+=num_list[i]
            count=i
print(count)
