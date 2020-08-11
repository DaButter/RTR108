import matplotlib.pyplot as plt
import  numpy as np
import math

x = np.arange(0.0,10.0,0.01)
y= np.sin(x)**2


plt.plot(x, y)
plt.grid()
plt.show()
