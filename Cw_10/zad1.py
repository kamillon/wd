import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.arange(1,21)
plt.plot(x, 1/x, label='f(x)=1/x')
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axis([1,len(x),0,1])
plt.show()