num_list = list(input("점수입력:").split())
num_list.sort(reverse=True)
set_list=set(num_list)
last_list=list(set_list)
top_th=last_list[0:3]
count=0
for i in top_th:
    for j in num_list:
        if i==j:
            count+=1

print(count)
