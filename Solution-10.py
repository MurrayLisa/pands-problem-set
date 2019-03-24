import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.0, 4.0, 1)
y1 = x
y2 = x**2
y3 = 2**x

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)

plt.title('Solution 10 Graph - Plotting the function of X')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(['y1 = x', 'y2 = x^2', 'y3 = 2^x'])

plt.show()