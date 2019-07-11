# Bài tập: Thay toàn bộ các phần tử của mảng bằng trung bình cộng các phần tử trong mảng đó, sử dụng vòng for.
# Hàm này không trả về biến nào mà chỉ thay đổi các giá trị của biến đầu vào x.

import numpy as np 

def myavg(x):
    d = x.shape[0]    
    res = 0
    for i in range(d):
        res += x[i]
    m = res / d
    for i in range(d):
        x[i] = m 

x = np.array([1., 2, 3, 4, 5, 6, 7, 8, 9, 10])
myavg(x)
print(x)
