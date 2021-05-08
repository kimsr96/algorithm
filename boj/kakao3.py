def solution(n, k, cmd):
    arr = ['무', '콘', '어', '제', '프', '네', '튜', '라']
    delete = []

    # for i in range(n):
    #     arr.append(i)

    for c in cmd:
        if c[0] == 'D':
            k += int(c[2])
        elif c[0] == 'U':
            k += (int(c[2]) * -1)
        elif c[0] == 'Z':
            temp = delete.pop()
            if temp <= k:
                k += 1
            arr.insert(temp, 'O')
        elif c[0] == 'C':
            delete.append(k)
            arr.pop(k)
            if k == len(arr):
                k -= 1
    delete.sort()
    for j in delete:
        arr.insert(j, 'X')
    print(arr)
    #answer = "".join(arr)
    return 1

print(solution(8, 2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))