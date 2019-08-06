import numpy as np 

# Kich thuoc cua mang
# Kích thước của một mảng numpy x nói chung được xác định bằng numpy.array.shape
x = np.array([3, 4, 5, 10])

y = np.array([[3, 4, 5, 10]])
print(x)
print(y)
print(x.shape)

d = x.shape[0]
print(d)

# Chi so
print("\n--------------------")
print(x[0])

# Chi so nguoc

print(x[d-1] - x[-1])
print(x[-2])


