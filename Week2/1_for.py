# dùng hàm range để tạo một iterable có giá trị 0,1,2,3,4
for i in range(5):
    print('Python 3.7')
    print('i_value: ', i)

for _ in range(5):
    print('Hello AI VIETNAM')
    print('làm gì đó ...')

for i in range(10):
    if i == 5:
        break
    print('i_value:', i)

# duyệt phần tử trong range(10)
for i in range(10):
    if i == 5:
        continue
    print('Giá trị i là', i)
    