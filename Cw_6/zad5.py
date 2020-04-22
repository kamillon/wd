import numpy as np

def foo(n):
    a = np.arange(n, 0, step=-1)
    print(a, end="\n\n")
    a = np.diag(a)
    print(a)
foo(4)