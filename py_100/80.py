from itertools import combinations

a = input().split(',')
b = int(input())

c = list(combinations(a, b))
print(c, len(c))
