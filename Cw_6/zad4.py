import numpy as np

def generuj(n,m):
    a = np.logspace(1, m, num=m, base=n, dtype='int64')
    return a
print(generuj(2,4))