import numpy as np

b = np.arange(1,10,1).reshape(3,3)
print(b,"\n")
for a in b.flat:
   print(a)