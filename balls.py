# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 17:37:28 2018
"""
# when we're in pylab mode, the next two imports are not necessary
# we do it here for correctness sake, iow your code will also run without pylab mode

import numpy as np
import matplotlib.pyplot as plt

import matplotlib.animation as animation

# gravitational acceleration on Earth in m*s^-2
g = 9.80665
#g = 1.6249
# acceleration vector due to g
ag = np.array((0,-g))
# coefficient of restitution (ratio of velocity after and before bounce)
# see http://en.wikipedia.org/wiki/Coefficient_of_restitution
cor = 0.95

# bounds of the room
xlim = (0,30)
ylim = (0,20)

# 1 millisecond delta t
delta_t = 0.001

fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=xlim, ylim=ylim)
ax.grid()

# in Python 2.7 we have to derive from object to have new-style classes
# in Python 3 this is still valid, but not necessary, as all classes are new-style
class Ball(object):

    def __init__(self, xy, v):
        """
        :param xy: Initial position.
        :param v: Initial velocity.
        """
        self.xy = np.array(xy)
        self.v = np.array(v)

        self.scatter, = ax.plot([], [], 'o', markersize=20)

    def update(self):
        if self.xy[0] <= xlim[0]:
            # hit the left wall, reflect x component
            self.v[0] = cor * np.abs(self.v[0])

        elif self.xy[0] >= xlim[1]:
            self.v[0] = - cor * np.abs(self.v[0])

        if self.xy[1] <= ylim[0]:
            # hit the left wall, reflect y component
            self.v[1] = cor * np.abs(self.v[1])

        elif self.xy[1] >= ylim[1]:
            self.v[1] = - cor * np.abs(self.v[1])

        # delta t is 0.1
        delta_v = delta_t * ag
        self.v += delta_v

        self.xy += self.v

        self.xy[0] = np.clip(self.xy[0], xlim[0], xlim[1])
        self.xy[1] = np.clip(self.xy[1], ylim[0], ylim[1])

        self.scatter.set_data(self.xy)



balls = [Ball((3.0,18.0), (0.2,0.3)), Ball((4.0,17.0), (-0.2,0.1)), Ball((1.0,19.0), (-0.3,0.5))]

def init():
    return []

def animate(t):
    # t is time in seconds
    global xy, v

    for ball in balls:
        ball.update()

    # have to return an iterable
    return [ball.scatter for ball in balls]

# interval in milliseconds
# we're watching in slow motion (delta t is shorter than interval)
ani = animation.FuncAnimation(fig, animate, np.arange(0,100,delta_t), init_func=init, interval=10, blit=True)

plt.show()