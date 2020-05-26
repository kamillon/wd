import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin

colors = ['red','green','blue','orange','cyan']
markers = ['.','^','v','o','s']

fig = plt.figure()
ax = fig.add_subplot( 111 , projection='3d' )
n = 100

for x in range(5):
    xs = randrange(n, 2 , 54 )
    ys = randrange(n, 16 , 25 )
    zs = randrange(n, 0, 100)
    ax.scatter(xs, ys, zs, c=colors[np.random.randint(len(colors))], marker=markers[np.random.randint(len(markers))])

ax.set_xlabel( 'X Label' )
ax.set_ylabel( 'Y Label' )
ax.set_zlabel( 'Z Label' )
plt.show()