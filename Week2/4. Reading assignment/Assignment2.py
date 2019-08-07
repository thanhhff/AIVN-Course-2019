# Cho list data = [1, 2, 3, 4, 5, 6, 7, 8, 9].
# Các giá trị trong list thể hiện điểm số của mỗi phần tử. Phần tử đầu có điểm số nhỏ nhất là 1 và phần tử cuối có điểm số lớn nhất là 9.

import random
import numpy as np

m = 1000

list_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

result = np.random.choice(list_data, size=m, replace=True, p=list_data / list_data.sum())

count_result = np.unique(result, return_counts=True)
print(count_result)
