import numpy as np

a = np.ones(25).astype('int64')
for n in range(2,25):
    a[n] = a[n-1] + a[n-2]
a = a.reshape(5,5)
print(a)