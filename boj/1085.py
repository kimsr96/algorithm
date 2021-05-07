x, y, w, h = map(int, input().split())
arr = [x, y]
arr.append(h - y)
arr.append(w - x)

print(min(arr))