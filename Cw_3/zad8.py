import math
def ciag(a=1, r=1, ile=10 ):
    return sum(a + wyraz*r for wyraz in range (ile))

print(ciag())
print(ciag(2,3,9))