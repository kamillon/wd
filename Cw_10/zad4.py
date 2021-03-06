import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,30.1,0.1)
s = 2 + np.sin(x)
s2 = np.sin(-x)

plt.plot(x,s,label='sin(x)')
plt.plot(x,s2,label='sin(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Wykres sin(x), sin(x)')
plt.legend(loc=6)
plt.show()