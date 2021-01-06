nationWidth = {'korea': 220877, 'Rusia': 17098242,'China': 9596961,'France': 543965,'Japan': 377915,'England' : 242900 
}
similar = []
for name, width in nationWidth.items():
    if name != 'korea':
        similar.append(width)
minus = abs(nationWidth['korea'] - min(similar))
print(minus)
for name, width in nationWidth.items():
    if width == min(similar):
        print(name, minus)



# similar = []
# for i in nationWidth.values():
#     if i != 220877:
#         similar.append(abs(nationWidth['korea'] - i))
# print(min(similar))