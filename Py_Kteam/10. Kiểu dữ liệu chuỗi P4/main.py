# Các phương thức biến đổi
string = 'Chuỗi  Mặc ĐỊNH 日本語 M m M'
# Phương thức capitalize - Viét hoa chữ đầu tiên, sau đó viết thường 
print(string.capitalize())

# Phương thức upper và lower 
print(string.upper())
print(string.lower())

# Phương thức swapcase - Chữ viết thường thành viết hoa & chữ viết hoa thành viết thường
print(string.swapcase())

# Phương thức title - Các từ được viết hoa chữ đầu tiên 
print(string.title())


# Các phương thức định dạng
# Phương thức center
print(string.center(50, '.'))

# Phương thức rjust
print(string.rjust(50))

# Phương thức ljust
print(string.ljust(50))

# Phương thức encode
# Phương thức join

# Phương thức replace
print(string.replace('M', 'mmmmmmmm', 2))

# strip & rstrip & lstrip
A = '123456789'

B = A.strip('90')

print(B)

# C = A.strip('xxx1')

# print(C)


