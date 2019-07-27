# tanh function pyplot

import matplotlib.pyplot as plt
import math

def tanh_function(data):
    return [(math.exp(x) - math.exp(-x)) / (math.exp(x) + math.exp(-x)) for x in data]

def tanh_derivative(data):
    return [1 - x**2 for x in data]

def linear_space(start, stop, num = 10):
    num = int(num)
    start = start * 1.
    stop = stop * 1.

    assert num > 1, 'num shou be greater than 1'

    step = (start - stop) / num
    result = []

    for i in range(num):
        result.append(start + step * i)
    return result

# Calculate plot points
data = linear_space(-5., 5., 100)
data_tanh = tanh_function(data)
data_dtanh = tanh_derivative(data_tanh)

# Setup centered axes
fig, ax = plt.subplots(figsize=(10,5))
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# Create and show plot 
ax.plot(data, data_tanh, color = "#d35400", linewidth = 3, label = "tanh")
ax.plot(data, data_dtanh, color = "#1abd15", linewidth = 3, label = "derivative")
ax.legend(loc = "upper left", frameon = False)
fig.show()

