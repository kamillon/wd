import numpy as np

def gen(n):
    a = np.ones((n,n))
    a = a.astype('int64') + 1
    for x in range(n):
        for y in range(n):
            a[x,y] = a[x,y] + abs(x-y)*2
    return a
print(gen(4))