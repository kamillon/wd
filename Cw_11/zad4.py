import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize =(8, 3))
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
sh = [True, False]

for x in range (0,5,1):
    ax = plt.subplot(231+x, projection="3d")
    _x = np.arange(4)
    _y = np.arange(5)
    _xx, _yy = np.meshgrid(_x, _y)
    x, y = _xx.ravel(), _yy.ravel()
    top = x + y
    bottom = np.zeros_like(top)
    width = depth = 1
    ax.bar3d(x, y, bottom, width, depth, top, shade=sh[np.random.randint(len(sh))], color=colors[np.random.randint(len(colors))])

plt.show()