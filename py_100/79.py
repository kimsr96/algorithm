l = [10, 20, 25, 27, 34, 35, 39] #기존 입력 값
n = int(input('순회 횟수는 :'))

def rotate(inL, inN):
    original = inL.copy()
    m = []
    minus = []
    for i in range(inN):
        m.append(inL.pop())
    
    m += inL

    for k in range(len(original)):
        minus.append(abs(original[k]-m[k]))

    min_value = min(minus)

    idx = minus.index(min_value)

    value1 = abs(original[idx])
    value2 = abs(m[idx])
    return print(min_value, value1, value2)


rotate(l, n)

# solution
# def sol(a, t):
#     b = a.copy()
#     c = []
#     for i in range(t):
#         b.insert(0,b.pop())
#     for i,j in zip(a,b):
#         c.append(abs(i-j))
#     index = c.index(min(c))
#     print("index :",index)
#     print("value :",a[index],b[index])

# sol(l,turn)

