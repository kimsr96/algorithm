a = list(input())
print(a)
for i in a:
    for j in a:
        if i == '(' and i!=j:
            if j == ')':
                print("YES")
                break
            else:
                print("NO")
                break

