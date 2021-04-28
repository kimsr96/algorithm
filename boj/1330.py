n = int(input())
num = []
num = list(map(int, input().split()))
max_num = max(num)

for i in range(n):
    num[i] = (num[i] / max_num) * 100
print(sum(num) / n)


