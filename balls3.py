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

fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=xlim, ylim=ylim)
ax.grid()



scatters = [ax.plot([], [], 'o', markersize=3)[0] for i in range(6)]

def animate(t):
    # t is count of iterations
    for i, scatter in enumerate(scatters):
        x = 5*i
        y = 5*math.sin(t) + 10
        scatter.set_data([x, y])
    return scatters

#interval in milliseconds
ani = animation.FuncAnimation(fig, animate, interval=1000, blit=True)

plt.show()