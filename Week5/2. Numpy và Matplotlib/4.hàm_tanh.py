import matplotlib.pyplot as plt
import numpy as np


def tanh(x):
    ex = np.exp(x)
    emx = np.exp(-x)
    return (ex - emx) / (ex + emx)


# Calculate plot points
x = np.arange(-5., 5., 0.1)
a = tanh(x)
dx = 1 - a ** 2

# Setup centered axes
fig, ax = plt.subplots(figsize=(10, 5))
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# Creat and show plot
ax.plot(x, a, color='#d35400', linewidth=3, label='tanh')
ax.plot(x, dx, color='#1abd15', linewidth=3, label='derivative')
ax.legend(loc='upper left', frameon=False)
fig.show()