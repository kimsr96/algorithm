while(True):
    x, y, z = map(int, input().split())
    arr = [x, y, z]
    arr.sort()

    if sum(arr) == 0:
        exit()

    if arr[2] ** 2 == (arr[0] ** 2) + (arr[1] ** 2):
        print("right")
    else:
        print("wrong")
