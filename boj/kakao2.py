def solution(places):
    answer = [1 for _ in range(5)]
    for i in range(5):
        arr_x = []
        arr_y = []
        flag = 0
        for j in range(5):
            for k in range(5):
                if places[i][j][k] == 'P':
                    arr_x.append(j)
                    arr_y.append(k)
        for l in range(len(arr_x)):
            for m in range(l + 1, 5):
                dx = (arr_x[m] - arr_x[l]) ** 2
                dy = (arr_y[m] - arr_y[l]) ** 2
                if dx + dy <= 1:
                    answer[i] = 0
                    flag = 1
                    break
                elif dx + dy == 2:
                    if places[i][arr_x[l]][arr_y[m]] == 'X' and places[arr_x[m]][arr_y[l]] == 'X':
                        continue
                    else:
                        answer[i] = 0
                        flag == 1
                        break
                elif dx + dy == 4:
                    if arr_x[m] == arr_x[l]:
                        if arr_y[m] > arr_y[l]:
                            if places[i][arr_x[m]][arr_y[l + 1]]  == 'X':
                                continue
                        elif places[i][arr_x[m]][arr_y[m + 1]]  == 'X':
                            continue
                    elif arr_y[m] == arr_y[l]:
                        if arr_x[m] > arr_x[l]:
                            if places[i][arr_x[l + 1]][arr_y[m]]  == 'X': 
                                continue
                        elif places[i][arr_x[m + 1]][arr_y[m]]  == 'X':     
                            continue
                    else:
                        answer[i] = 0
                        flag == 1
                        break
                if flag == 1: 
                    break
        print(answer)
    return answer
solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])