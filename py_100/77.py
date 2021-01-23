def sol(strings):
    result = []
    for i in range(1,len(strings)+1):
        for j in range(i):
            result.append(strings[j:j+len(strings)-i+1])
    return result

input1 = input()

#문자열 나열될 수 있는 모든 경우의수 만들기
list1 = sol(input1)


print(list1)