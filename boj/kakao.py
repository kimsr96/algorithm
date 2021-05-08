def solution(s):
    answer =  ''
    d = {'zero' : 0, 'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4, 'five' : 5, 'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9, 'ten' : 10}
    find_arr = []
    s_list = []
    temp = ''

    for j in s:
        if  48 <= ord(j) <= 57:
            s_list.append(temp)
            temp = ''
            s_list.append(j)
        else:
            temp += j
        try:
            48 <= d[temp] <= 57
            s_list.append(str(d[temp]))
            temp = ''
        except:
            continue
    for i in s_list:
        if i == '':
            continue
        else:
            answer += i
    
    return int(answer)

print(solution("2three45sixseven"))