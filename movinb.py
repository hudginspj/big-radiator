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
'''
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