def bubble(n, data):
	for i in range(n-1):
		for j in range(i,i+1):
			if data[j] > data[j+1]:
				data[j] = changeData
				data[j+1] = changeData2
				data[j] = changeData2
				data[j+1] = changeData

	for i in range(n):
		print(data[i], end = " ")

n = int(input())
data = list(map(int, input().split()))

bubble(n, data)