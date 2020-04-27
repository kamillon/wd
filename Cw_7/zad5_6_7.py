import numpy as np

ma = np.arange(1,7).reshape(2,3)
a = np.sin(ma)
mb = np.arange(7,13).reshape(2,3)
b = np.cos(mb)

print(a+b)