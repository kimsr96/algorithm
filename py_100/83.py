def math(e):
    arr = list(e)
    sm = 0
    lg = 0
    for i in arr:
        if i == '(':
            sm += 1
        elif i == ')':
            sm -= 1
        
        if i == '{':
            lg +=1
        elif i == '}':
            lg -= 1

    if sm == 0 and lg == 0:
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
