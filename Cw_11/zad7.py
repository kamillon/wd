import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

np.random.seed( 19634822 )

def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin

fig = plt.figure()
ax = fig.add_subplot( projection = '3d' )
n=20
xs = randrange(n, 23 , 32 )
ys = randrange(n, 0 , 100 )
zs = randrange(n, 0, 50)
ax.scatter(xs, ys, zs, c = "r", marker = "o", label="jablka")

ax.set_xlabel( 'X Label' )
ax.set_ylabel( 'Y Label' )
ax.set_zlabel( 'Z Label' )

xs = [0,20,20,38,38]
ys = [0,0,50,50,55]
zs = [0,0,0,0,10]
ax.plot(xs, ys, zs, c ='green', label="waz")
ax.set_xlabel( 'X' )
ax.set_ylabel( 'Y' )
ax.set_zlabel( 'Z' )

plt.legend()
plt.show()