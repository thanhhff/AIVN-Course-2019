import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10, 0.01)
y = np.cos(x)
plt.title('Cosine Funcion')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.plot(x, y)
plt.show()