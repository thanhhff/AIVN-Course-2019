emty_list = []

my_list = [0, 1, 2, 3, 4, 5]
print(my_list)
mixedList = [True, 5, 'some string', 123.45]
print(mixedList)

# Thêm phần tử vào danh sách
mixedList.append(1000)
print(mixedList)

data = mixedList + my_list
print(data)

data.insert(1, 'FFFF')
print(data)
del data[1:3]
print(data)

data.remove('some string')
print(data)

data.pop(1)
print(data)
data.sort(reverse = True)
print(data)
