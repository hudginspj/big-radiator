'''
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Extract unique labels
unique = list(set(labels))
# Define the colors
colors = [plt.cm.jet(float(i + 1) / (max(unique) + 1)) for i in unique]

# Define plot style
with plt.style.context(('ggplot')):
    # Loop over the view angles
    for angle in range(0, 360, 5):

        # Define figure and 3D axes
        fig = plt.figure(figsize=(10, 7))
        ax = Axes3D(fig)

        # Loop over every element of X
        for i, u in enumerate(unique):
            xi = [X[j, 0] for j in range(len(X[:, 0])) if lab[j] == u]
            yi = [X[j, 1] for j in range(len(X[:, 1])) if lab[j] == u]
            zi = [X[j, 2] for j in range(len(X[:, 2])) if lab[j] == u]

            # Scatter plot
            ax.scatter(xi, yi, zi, c=colors[i], s=80, label=str(u))

        # Set the view angle
        ax.view_init(30, angle)

        # Label the axes
        ax.set_xlabel('PC1')
        ax.set_ylabel('PC2')
        ax.set_zlabel('PC3')

        # Save the figure
        plt.savefig('.\\movie\\t4_' + str(angle).zfill(3) + '.png', dpi=100)

'''


from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as ani
import ringinterpret as dt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
def anime(a):
    data = dt.step()
    for i in data:
        values = data[i]
        x = values['x']
        y = values['y']
        z = values['z']
        ax.set_xlabel('x axis')
        ax.set_ylabel('y axis')
        ax.set_zlabel('z axis')
    ax.scatter(x, y, z, c='g', marker='o')


gr = ani.FuncAnimation(fig, anime,interval=1000)
plt.show()





'''
from __future__ import print_function

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import time

def generate(X, Y, phi):
    R = 1 - np.sqrt(X**2 + Y**2)
    return np.cos(2 * np.pi * X + phi) * R

plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

xs = np.linspace(-1, 1, 50)
ys = np.linspace(-1, 1, 50)
X, Y = np.meshgrid(xs, ys)
Z = generate(X, Y, 0.0)

wframe = None
tstart = time.time()
for phi in np.linspace(0, 360 / 2 / np.pi, 100):

    oldcol = wframe

    Z = generate(X, Y, phi)
    wframe = ax.plot_wireframe(X, Y, Z, rstride=2, cstride=2)

    # Remove old line collection before drawing
    if oldcol is not None:
        ax.collections.remove(oldcol)

    plt.draw()

print ('FPS: %f' % (100 / (time.time() - tstart)))

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import animation

x = [0, 1, 2,3,4,5,6,7,8,9,10,12,13,14]
y = [0, 1, 2,3,4,5,6,7,8,9,10,12,13,14]
yaw = [0.0, 0.5, 1.3,0.0,0.5,1.3,0.0,0.5,1.3,0.0,0.5,1.3,0.0,0.5,1.3,0.0,0.5,1.3,0.0,0.5,1.3]
fig = plt.figure()
plt.axis('equal')
plt.grid()
ax = fig.add_subplot(111)
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)

patch = patches.Rectangle((0, 0), 0, 0, fc='y')
patch2 = patches.Rectangle((-8, 0), 0, 0, fc='y')
def init():
    ax.add_patch(patch)
    ax.add_patch(patch2)
    return patch, patch2

def animate(i):

    patch.set_width(1.2)
    patch.set_height(1.0)
    patch.set_xy([x[i], y[i]])
    patch._angle = -np.rad2deg(yaw[i])
    patch2.set_width(2)
    patch2.set_height(1.0)
    patch2.set_xy([x[-i], y[-i]])
    patch2._angle = -np.rad2deg(yaw[i])
    return patch, patch2

anim = animation.FuncAnimation(fig, animate,
                               init_func=init,
                               frames=len(x),
                               interval=500,
                               blit=True)
plt.show()

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(7, 6.5)

ax = plt.axes(xlim=(0, 10), ylim=(0, 10))
patch = plt.Circle((5, -5), 0.75, fc='y')

def init():
    patch.center = (5, 5)
    ax.add_patch(patch)
    return patch,

def animate(i):
    x, y = patch.center
    x = 5 + 3 * np.sin(np.radians(i))
    y = 5 + 3 * np.cos(np.radians(i))
    patch.center = (x, y)
    return patch,

anim = animation.FuncAnimation(fig, animate,
                               init_func=init,
                               frames=360,
                               interval=20,
                               blit=True)
anim2 = animation.FuncAnimation(fig, animate, init_func=init, frames= 360 , interval=-1, blit=True)

plt.show()
'''