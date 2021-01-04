# a = int(input())
# b= list()

# while 1:
#     if a%2 == 1:
#         a //= 2
#         b.append(1)
#     elif a<=1:
#         break
#     else:
#         a //= 2
#         b.append(0)
# print(b[::-1])


# Solution 
a = int(input())
b = []

while a:
    print(a)
    b.append(str(a % 2))
    a = int(a / 2)

print(b)
b.reverse()
print(b)
print(''.join(b))


