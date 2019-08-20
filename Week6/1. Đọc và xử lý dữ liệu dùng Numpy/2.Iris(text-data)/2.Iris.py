import numpy as np
import numpy.core.defchararray as np_f

# Bộ dữ liệu Iris có chứa cột species ở dạng chuỗi. Do đó, cần chuyển dạng này sang dạng số

# Lấy các đặc trưng và lưu vào biến X
X = np.genfromtxt('iris.csv', delimiter=',', dtype='float', usecols=[0, 1, 2, 3], skip_header=1)
print(X.shape)

# Lấy species và lưu vào biến y
y = np.genfromtxt('iris.csv', delimiter=',', dtype='str', usecols=4, skip_header=1)

# thay chuỗi bằng số
# Sử dụng np.unique() để lấy các loại chuỗi duy nhất trong một mảng np
categories = np.unique(y)
print(categories)

for i in range(categories.size):
    # hàm np_f.replace() để thay giá trị kiểu chuỗi
    y = np_f.replace(y, categories[i], str(i))

# đưa về kiểu float
y = y.astype('float')
print(y)
