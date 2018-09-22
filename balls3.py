# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 17:37:28 2018
"""
# when we're in pylab mode, the next two imports are not necessary
# we do it here for correctness sake, iow your code will also run without pylab mode

import numpy as np
import matplotlib.pyplot as plt

import matplotlib.animation as animation
import math

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

    def __init__(self, y):
        """
        :param xy: Initial position.
        :param v: Initial velocity.
        """
        self.y = y

        self.scatter, = ax.plot([], [], 'o', markersize=3)

    def update(self, x):
        #self.scatter.set_data(self.xy)
        self.scatter.set_data([x, self.y])

#balls = [Ball(3), Ball(7), Ball(11)]

scatters = [ax.plot([], [], 'o', markersize=3) for i in range(3)]

def init():
    return []

def animate(t):
    # t is time in seconds
    #for ball in balls:
    #    ball.update(5*math.sin(t) + 10)
    for scatter in scatters:
        scatter.set_data([])
    # have to return an iterable
    #return [ball.scatter for ball in balls]
    return scatters

# interval in milliseconds
# we're watching in slow motion (delta t is shorter than interval)
ani = animation.FuncAnimation(fig, animate, np.arange(0,100,delta_t), init_func=init, interval=10, blit=True)

plt.show()