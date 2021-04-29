data = input()
list_data = list(data)
alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
total = 0

for i in range(len(alpha)):
    total += data.count(alpha[i])
    print(total)

if  data.count('z=') != 0:
    total -= data.count('dz=')
    print(total)

if (len(list_data) == data.count('dz=') * 3):
    print(len(list_data) - (data.count('dz=') * 2))
elif (data.count('dz=') != 0):
    print(len(list_data) - (data.count('dz=') * 2) - total + 1)
else:
    print(len(list_data) - total)



