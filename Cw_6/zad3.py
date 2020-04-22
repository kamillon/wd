import numpy as np

def foo(n):
    a = np.arange(n*n).reshape(n,n)
    return a+1
print(foo(3))