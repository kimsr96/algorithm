data1 = input()
data = list(data1)
#alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0
for i in range(len(data) - 1):
    if data[i] == 'c' or data[i] == 's':
        if data[i + 1] == '=':
            cnt += 1
    elif  data[i] == 'z':
        if data[i-1] == 'd':
            continue
        elif data[i+1] == '=':
            cnt += 1
    elif data[i] == 'd':
        if data[i + 1] == 'z' and data[i + 2] == '=':
            cnt += 1
    elif (data[i] == 'c' or data[i] == 'd') and (data[i + 1]== '-'):
        cnt += 1
    elif (data[i] == 'l' or data[i] == 'n') and (data[i + 1]== 'j'):
        cnt += 1
print(len(data) - cnt - data1.count('dz='))
