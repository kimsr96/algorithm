# 3	1	1
# 6	1	2
# 9	1	3
# 33	1*3 + 1	4
# 36	1*3 + 2	5
# 39	1*3 + 3	6
# 63	2*3 + 1	7
# 66	2*3 + 2	8
# 69	2*3 + 3	9
# 93	3*3 + 1	10
# 96	3*3 + 2	11
# 99	3*3 + 3	12
# 333	1*9 + 1*3 + 1	13

# def sol(n):
#     n = list(str(n))
#     answer = 0
#     count = 1
#     d = {3 : 1, 6 : 2, 9 : 3}
#     while n:
#         answer += d[int(n.pop())] * count
#         count *= 3
        
#     return answer

def sol(n):
    n = list(str(n))
    while n:
        print("hi")
    return n

print(sol(3))
# for i in range(len(a)):
#     if a[i] == '3': 
#         cnt += (i+i+1)

#     elif a[i] == '6':
#         cnt += (i+2)+(i*3)

#     elif a[i] == '9':
#         cnt += (3 * (i+1))

# print(cnt)




# a = int(input()
# cnt =0
# c=[]
# for i in range(1,a+1):
#     b = list(str(i))
#     for j in range(len(b)):
#         if (b[j] and b[j-1] == '3') or (b[j] and b[j-1] == '6') or (b[j] and b[j-1] == '9'):
#             c.append(b)
        
# print(c)


# for i in range(1,a+1):
#     b = list(str(i))
#     if i == 3 or i == 6 or i==9:
#         for j in range(len(b)):
#             if b[j] == '3'or b[j] == 6 or b[j] ==9 :
#             cnt +=1

# print(cnt)
