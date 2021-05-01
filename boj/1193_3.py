n = int(input())

total = 0
line = 0

for i in range(1, n + 1):
    total += i
    line += 1
    if total >= n:
        break

line_arr = [j for j in range(1, line + 1)]
line_arr_reverse = list(reversed(line_arr))

if line % 2 == 0:
    print(f"{line_arr[n - total - 1]}/{line_arr_reverse[n - total - 1]}")
else:
    print(f"{line_arr_reverse[n - total - 1]}/{line_arr[n - total - 1]}")
    
