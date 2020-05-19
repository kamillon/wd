import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.subplot(2,1,1)

x = np.arange(1,21)
plt.plot(x, 1/x, label='f(x)=1/x')
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axis([1,len(x),0,1])

plt.annotate('punkt: x = 5, y = 0.2)',
            xy=(5, 0.2), xycoords='data',
            xytext=(120, 30), textcoords='offset points',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='bottom')


plt.subplot(2,1,2)

x = np.arange(1,21)
plt.plot(x, 1/x, 'g:>', label='f(x)=1/x')
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axis([0,len(x),0,1])

plt.annotate('punkt: x = 10, y = 0.1)',
            xy=(10, 0.1), xycoords='data',
            xytext=(130, 20), textcoords='offset points',
            arrowprops=dict(facecolor='g', shrink=0.05),
            horizontalalignment='right', verticalalignment='bottom')

plt.show()