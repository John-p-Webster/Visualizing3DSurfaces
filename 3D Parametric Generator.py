import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d
from matplotlib.animation import FuncAnimation

# Sets graph to 3d
ax = plt.axes(projection="3d")

# Time function, 0 -> 50 with .1 increment
t = np.arange(0, 50, .1)

# Equations for each dimension
x = np.sin(t)
y = np.cos(t)
z = np.cos(t)

# Titles axes and graph
ax.set_title("3D Line Graph")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

# Creates graph
plt.plot(x, y, z, 'c')
plt.show()

