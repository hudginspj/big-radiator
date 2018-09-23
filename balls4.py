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
import vertinterpret

# bounds of the room
xlim = (0,40)
ylim = (0,1e13)

fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=xlim, ylim=ylim)
ax.grid()



def animate(t):
    # t is count of iterations
    scatters = []
    points = vertinterpret.step()
    for p in points:
        x = points[p]['x']
        y = points[p]['y']
        scatter = ax.plot([], [], 'o', markersize=10)[0]
        scatter.set_data([x, y])
        scatters.append(scatter)
        
    return scatters

#interval in milliseconds
ani = animation.FuncAnimation(fig, animate, interval=300, blit=True)

plt.show()