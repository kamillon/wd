import math
def okrag(x=2, y=2, a=0, b=0):
    r = math.sqrt((x-a)**2 + (y-b)**2)
    return r

print(okrag())
print(okrag(1,1))
print(okrag(1,1,0,0))