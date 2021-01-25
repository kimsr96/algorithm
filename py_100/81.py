flag = [] #지뢰 없이 깃발만 있는 리스트
minesweeper = [] #지뢰를 찾은 리스트
for i in range(5):
    cnt = 5
    flag.append(input('깃발 값과 함께 입력하세요 :').split(' '))
    for j in range(cnt):
        if flag[i][j] == '0':
            minesweeper.insert(j,"*")
        elif flag[i][j] == '1':
            minesweeper.insert(j,"f")
        else:
            minesweeper.append("0")
        
    print(minesweeper)
        
print(flag)
print(minesweeper)
