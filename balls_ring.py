# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 17:37:28 2018
"""
# when we're in pylab mode, the next two imports are not necessary
# we do it here for correctness sake, iow your code will also run without pylab mode

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

import matplotlib.animation as animation
import math
import ringinterpret as interpret

# bounds of the room

# xlim = (-1e13,1e13)
# ylim = (-1e13,1e13)
xlim = (-interpret.max_radius,interpret.max_radius)
ylim = (-interpret.max_radius,interpret.max_radius)

fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=xlim, ylim=ylim)
ax.grid()
ax.set_facecolor('xkcd:black')

all_scatters = None

def animate(t):
    global all_scatters
    # t is count of iterations
    if all_scatters:
        for scatter in all_scatters:
            scatter.set_visible(False)

    scatters = []
    points = interpret.step()
    for p in points:
        x = points[p]['x']
        y = points[p]['y']
        scatter = ax.plot([], [], 'o', markersize=5)[0]
        scatter.set_data([x, y])
        #scatter.set_visible(False)
        scatters.append(scatter)
    
    all_scatters = scatters
    return scatters

#interval in milliseconds
ani = animation.FuncAnimation(fig, animate, interval=300, blit=True)
#ani.save("xtest1.html")

figManager = plt.get_current_fig_manager()
figManager.window.showMaximized()

plt.show()

#print(matplotlib.rcParams['savefig.frameon'])
