#Solution-10 Lisa Murray

#Import Libraries
import matplotlib.pyplot as plt
import numpy as np

#Define x axis
x = np.arange(0.0, 4.0, 1)

#Define the function
y1 = x
y2 = x**2
y3 = 2**x

#plot the y1-y3 functions
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)

#Labelling graph
plt.title('Solution 10 Graph - Plotting the function of X')
plt.xlabel('X')
plt.ylabel('Y')

#Legend details
plt.legend(['y1 = x', 'y2 = x^2', 'y3 = 2^x'])

#Show grid lines
plt.grid(True)

#display graph
plt.show()