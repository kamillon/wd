import numpy as np

a = np.arange(12)
print(a,"\n")
b = a.reshape(3,4)
print(b,"\n")
c = a.reshape(4,3)
print(c,"\n")
d = a.reshape(2,6)
print(d,"\n")
print(a.ravel(),"\n")
print(b.ravel(),"\n")
print(c.ravel(),"\n")
# wyniki są identyczne