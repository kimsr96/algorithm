# 입력 - 입력은 한글 혹은 영어로 입력됩니다.
# 복잡한 세상 편하게 살자


# 출력 - 띄어쓰기를 기준으로 하여 짧은 형태로 출력합니다.
# 복세편살
arr=[]
a = list(input().split())
for idx, first in enumerate(a):
    print(first[0:1],end="")
