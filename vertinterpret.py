# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 11:47:35 2018

@author: pjhud
"""
from math import *
import simcore

#sim = simcore.Sim(1e23, 1e5)
#####sim = simcore.Sim(1e23, 1e5, ring_mass=1e30, starting_radius=1e10, step_time=1e5)  #default, flower shape
#sim = simcore.Sim(2e20, 5e3, ring_mass=2e27, starting_radius=1e10, step_time=1e5)
sim = simcore.Sim(2e20, 0, ring_mass=2e27, starting_radius=1.5e11, step_time=1e5) #water, 1AU  dropping

    
def step():
    for i in range(100):
        sim.step()

    print('max radius', max(sim.radii), sim.n_rings, sim.rings_added)

    points = {}
    for i, r in enumerate(sim.radii):
        x = i
        y = r
        z = 0
        points[i]={'x': x, 'y': y, 'z':z, 'age': sim.t}
    #for p in points:
    #    print(p, ':', points[p])
    return points

if __name__ == "__main__":
    step()
    print(step())
    
