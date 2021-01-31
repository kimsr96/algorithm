from itertools import permutations

a = list(input())
b = int(input())
c = sorted(list(map(''.join, permutations(a,b))))

print(c[-1])