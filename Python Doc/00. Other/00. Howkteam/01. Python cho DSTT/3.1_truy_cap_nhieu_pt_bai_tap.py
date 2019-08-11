# Bài tập: Cho trước một số tự nhiên n. 
# Tạo một mảng có n phần tử mà các phần tử có chỉ số chẵn (bắt đầu từ 0) là một cấp số cộng bắt đầu từ 2, công sai bằng -0.5; các phần tử có chỉ số lẻ bằng -1.

# Ví dụ:
# Với n=4, kết quả trả về là mảng [ 2. -1. 1.5 -1. ]. Với n=5, kết quả trả về là mảng [ 2. -1. 1.5 -1. 1. ].

import numpy as np 

def myfunc(n):
    x = 1.0 * np.arange(n)
    x[:n] = -1.0
    for i in range(n):
        if i % 2 == 0:
            if i == 0:
                x[i] = 2.0
            else:
                x[i] = x[i - 2] - 0.5
    return x

print(myfunc(5))
