import numpy as np
import matplotlib.pyplot as plt

x = np.arange(3, 10)
y = 4 * x + 3
plt.title('Linear Function')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.plot(x, y)
# plt.clf()
# plt.close()
plt.show()


