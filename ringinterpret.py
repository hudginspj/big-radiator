# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 11:47:35 2018

@author: pjhud
"""
from math import *
import simcore
import random

sim = simcore.Sim(1e23, 1e5) #### Default
max_radius = 1e13

#sim = simcore.Sim(2e20, 0, ring_mass=2e27, starting_radius=1.5e11, step_time=1e5)
#max_radius = sim.starting_radius
    
def step():
    for i in range(100):
        sim.step()

    print('max radius', max(sim.radii), sim.n_rings, sim.rings_added)

    points = {}
    for i, r in enumerate(sim.radii[1:]):
        n = 10 #343
        for j in range(n):
            theta = 2 * pi * (j + (0.1 *i))  / n
            #gap = r - sim.radii[i-1]
            #r_adj = r + (gap * j / n)
            #r_adj = r + random.uniform(1.5, 1.9)
            r_adj = r
            x = r_adj * sin(theta)
            y = r_adj * cos(theta)
            z = 0
            points[i*n +j] = {'x': x, 'y': y, 'z':z, 'age': sim.t}
    #for p in points:
    #    print(p, ':', points[p])
    return points

if __name__ == "__main__":
    step()
    print(step())
    
