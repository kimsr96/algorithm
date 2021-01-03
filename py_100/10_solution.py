n = int(input())
for i in range(n+1):
    print(" "*(n-i)+("*"*(2*i-1)))

# My Solution
# a = input()
# for i in range(1,int(a)+1):
#     for j in range(0, int(a)*2-1):
#         if j < int(a)-i:
#             print(" ",end="")
#         elif j >= int(a)-i and j< int(a)+i-1:
#             print('*',end="")
#         elif j> int(a)-i:
#             print(" ", end="")
#     print()