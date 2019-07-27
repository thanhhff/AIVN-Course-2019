import matplotlib.pyplot as plt

# x_data = [0, 1, 2, 3]
# y_data = [1, 3, 2, 4]

# plt.plot(x_data, y_data)
# plt.xlabel('x values')
# plt.ylabel('y values')

# plt.show()

# ham linear_space
def linear_space(start, stop, num = 10):
    num = int(num)
    start = start * 1.
    stop = stop * 1.

    assert num > 1, 'num should be greater than 1'

    step = (stop - start) / num

    result = []
    for i in range(num):
        result.append(start + step*i)
    return result

print(linear_space(1, 8, 7))
