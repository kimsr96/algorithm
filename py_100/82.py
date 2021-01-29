def math(e):
    arr = list(e)
    for idx_i,i in enumerate(arr):
        if i == '(':
            for idx_j,j in enumerate(arr):
                if j == ')' and idx_i < idx_j:
                    return True
                else:
                    return False
 

while 1:
    order = input('데이터 입력(1), 프로그램 종료(2) :')
    if order == '1':
        ex = input('데이터를 입력하세요 :')
        print(math(ex))
    else:
        break