x = []
y = []

for _ in range(3):
    i, j = map(int, input().split())
    x.append(i)
    y.append(j)

for n in range(len(x)):
    if x.count(x[n]) == 1:
        rectangle_x = x[n]
    if y.count(y[n]) == 1:
        rectangle_y = y[n]

print(rectangle_x, rectangle_y)