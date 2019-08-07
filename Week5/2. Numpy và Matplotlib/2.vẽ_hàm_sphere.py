import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10, 0.01)
y = x * x
plt.title('Sphere Function')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.plot(x, y)
plt.show()
