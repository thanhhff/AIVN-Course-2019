import numpy as np

# # Tạo list
# l = list(range(1, 4))
#
# # Tạo ndarray
# data = np.array(l)
#
# # print(data[0])
# # print(data.shape[0])
#
# arr1 = np.arange(12)
# # print(np.arange(1,19, 2))
#
# arr2 = arr1.reshape((3, 4))
# print(arr2)
# # print(type(arr1[0]))


# arr3 = np.array([1, 2], dtype=np.float)

# print(np.zeros((1, 3), dtype=int))
# print(np.ones((1, 3)))

# print(np.full((2, 3), 9))
# print(np.eye(3, dtype=int))

# arr = np.random.randint(4, 10, (3, 4))
# print(arr)

arr = np.arange(10)
# print(arr)

# out = np.where(arr < 5, arr, 10 * arr)
# print(out)

# arr = np.array([[1, 2], [3, 4]])
# print(arr)
# print(arr.flatten())

# print(arr[1:2, :])

# arr_b = arr[1:2, :].copy()
# print(arr_b)
#
# arr_b[0, 0] = 10
# print(arr_b)
# print(arr)

# bool_idx = (arr > 2)
# print(bool_idx)
# print(arr[arr > 1])

X = np.array([[1, 2, 3], [4, 5, 5], [7, 9, 0]])
v = np.array([1, 2, 3])

print(X + v)