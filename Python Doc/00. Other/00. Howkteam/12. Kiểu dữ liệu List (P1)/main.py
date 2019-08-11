# Container
# List
a = [1, 2, 3, 'Kteam', [100, 'How?']]
print(a)

print('------------------')
a = [i for i in range(30)]
print(a)

a = [[n, n*1, n*2] for n in range(1,4)]
print(a)

# Sử dụng constructor List
lst = list('THANh')
print(lst)

# Toan tu cua list 
lst += [1,2, 'Thanhhhh', [3, 4]]
lst += 'abc'
print(lst)
print('A' in lst)

# Cat list
print(lst[1:4])
print(lst[8][0])

# Thay đổi nội dung List
lst[2] = 10
print(lst)

# Ma trận 
print('------------------')
a = [[1,2,3],[4,5,6]]
print(a[0])
print(a[1])
print(a[0][2])

# Copy list
b = list(a) 
print(b)
