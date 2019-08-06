# Tuple bảo vệ dữ liệu không bị thay đổi
# có thể dùng làm key của dictionary

a = (i for i in range(10) if i % 2 == 0)
tup = tuple(a)
print(tup)
print(type(tup))

# các toán tử tương tự list
# Tuple và chuỗi đều là một dạng hash object 
