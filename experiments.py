# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 11:47:35 2018

@author: pjhud
"""
from math import *
import simcore
import matplotlib.pyplot as plt

#while sim.radii[0] > 0: 

def experiment(mass_flux, initial_velocity, ring_mass=1e30, starting_radius=1e10, step_time=1e5):
    sim = simcore.Sim(mass_flux, initial_velocity, ring_mass, starting_radius, step_time)
    while sim.step():
        for i in range(100):
            sim.step()
        print('max radius', max(sim.radii), sim.n_rings, sim.rings_added)
    radius = max(sim.radii)
    mass = ring_mass * sim.n_rings
    print('radius', radius, 'mass', mass)
    plt.plot(range(len(sim.radii)), sim.radii)
    plt.show()

    




if __name__ == "__main__":
    pass
    experiment(1e23, 1e5, ring_mass=1e30, starting_radius=1e10, step_time=1e5)
    
    
