# tanh function

import matplotlib.pyplot as plt
import math


def tanh_function(data):
    return [(math.exp(x) - math.exp(-x)) / (math.exp(x) + math.exp(-x)) for x in data]


def tanh_derivative(data):
    # d/dx (tanh) = 1 - tanh^2
    return [1 - x**2 for x in data]


def linear_space(start, stop, num=10):
    num = int(num)
    start = start * 1.
    stop = stop * 1.

    assert num > 1, 'num should be greater than 1'

    step = (stop - start) / num

    result = []
    for i in range(num):
        result.append(start + step*i)
    return result


# Calculate plot points
data = linear_space(-5., 5., 100)
data_tanh = tanh_function(data)
data_dtanh = tanh_derivative(data_tanh)

# Chinh lai cac truc
fig, ax = plt.subplots(figsize=(10, 5))
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# Creat and show plot
# ax.plot(data, data_tanh, color="#d35400", linewidth=3, label="tanh")
# ax.plot(data, data_dtanh, color="#1abd15", linewidth=3, label="derivative")
# ax.legend(loc="upper left", frameon=False)
# fig.show()

plt.plot(data, data_tanh, color="#d35400", linewidth=3, label="tanh")
plt.plot(data, data_dtanh, color="#1abd15", linewidth=3, label="derivative")
plt.legend(loc="upper left", frameon=False)
plt.show()
