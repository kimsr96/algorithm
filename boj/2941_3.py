data = input()
alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = []
for i in range(len(alpha)):
    if  alpha[i] == 'z=':
        cnt.append(data.count(alpha[i]) - data.count('dz='))
    else:
        cnt.append(data.count(alpha[i]))
print(len(data) - sum(cnt) - data.count('dz='))



