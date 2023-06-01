import numpy as np
import matplotlib.pyplot as plt
import sys


who = sys.argv[1] if len(sys.argv) > 1 else 2
x = np.linspace(0,float(who)*np.pi,1000)
y = np.sin(x)

plt.plot(x,y)
plt.grid()
plt.show()