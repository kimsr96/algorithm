change = list(input())
changed = list()
for i in change:
    if i.isupper() == True:
        j=i.lower()
        changed.append(j)
    elif i.islower() == True:
        j=i.upper()
        changed.append(j)

print(changed)
