l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(l)
len_l = len(l)

for i in range(len_l):
    print(l[i])

print('In nguoc danh sach:')
for i in range(len_l):
    print(l[-i - 1])

print('List Slicling:')

for i in range(3, len_l):
    print(l[i])

