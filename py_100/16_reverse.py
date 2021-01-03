# print(a)
# print(a[::-1])


while 1:
    a = input()
    a_list = list(a)
    a_list.reverse()
    a_rev=''.join(a_list).split()
    for i in range(len(a_rev)):
        rev_pop=a_rev.pop(0)
        print(rev_pop)
        if i == len(a_rev):
            break;
#     a = input()
#     a_list = list(a)
#     a_list.reverse()
# print(a_list)
# print(''.join(a_list))