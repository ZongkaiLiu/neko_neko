import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 51)
y = np.sin(x)

plt.figure()
plt.plot(x, y, 'ro-')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
