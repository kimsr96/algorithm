a = int(input())

for i in [2,3,5,7,11]:
    if a == i:
        res="yes"
        break
    elif a%i == 0:
        res="NO"
        break
    else:
        res="YES"
print(res)

# Solution
############################################
#인터넷에서 에라토스테네스의 체를 검색해보시고, 에라토스테네스의 체를 구현해보세요.

def check_prime(n):
    i = 2
    while i < n:
        if n % i == 0:
            break
        i = i + 1
    if i == n:
        print("YES")
    else:
        print("NO")
check_prime(int(input()))

###

x = int(input())
for i in range(2, x//2 + 1):
    if x == 1:
        print('소수가 아닙니다.')
        break
    if x == 2:
        print('소수입니다.')
        break
    if x % i == 0:
        print('소수가 아닙니다.')
        break
else:
    print('소수입니다.')