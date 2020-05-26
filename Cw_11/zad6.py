import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

np.random.seed( 19680822 )

def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin

fig = plt.figure()
ax = fig.add_subplot( 121 , projection = '3d' )

n=20
xs = randrange(n, 23 , 32 )
ys = randrange(n, 0 , 100 )
zs = randrange(n, 0, 50)
ax.scatter(xs, ys, zs, c = "g", marker = "o")

ax = fig.add_subplot( 122 , projection = '3d' )
n=5
xs = randrange(n, 2 , 5 )
ys = randrange(n, 4 , 5 )
zs = randrange(n, 6 , 8 )
ax.plot(xs, ys, zs)
ax.set_xlabel( 'X Label' )
ax.set_ylabel( 'Y Label' )
ax.set_zlabel( 'Z Label' )
plt.show()