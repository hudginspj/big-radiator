# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 11:47:35 2018

@author: pjhud
"""
from math import *
import simcore
import matplotlib.pyplot as plt
import numpy

#while sim.radii[0] > 0: 

def quick_plot(ys):
    plt.plot(range(len(ys)), ys)
    plt.show()

def experiment(mass_flux, initial_velocity, ring_mass, starting_radius, step_time):
    sim = simcore.Sim((mass_flux*2), initial_velocity, ring_mass, starting_radius, step_time) # Double mass flux for symetry trick
    masses = []
    for i in range(100):
        for j in range(100):
            sim.step()
        masses.append(ring_mass * sim.n_rings)
        print(sim.steps, 'max radius', max(sim.radii), sim.n_rings, sim.rings_added)
    radius = max(sim.radii)
    mass = ring_mass * sim.n_rings
    print('radius', radius, 'mass', mass)
    #quick_plot(sim.radii)
    quick_plot(masses)

def test_initial(sim):
    if sim.n_rings > 35:
         return "too_many_rings"
    return None
def test_average(sim):
    if sim.n_rings > 35:
        return "too_many_rings"
    if sim.n_rings < 8:
        return "not_enough_rings"
    if sim.radii[0] > sim.starting_radius * 0.8:
        return "not_reaching_center"
    return None

def print_status(sim):
    #print(sim.steps, 'min radius', sim.radii[0], sim.n_rings, sim.rings_added)
    print(sim.steps, end=' ', flush=True)

def failable_experiment(mass_flux, initial_velocity, ring_mass, starting_radius, step_time):
    sim = simcore.Sim((mass_flux*2), initial_velocity, ring_mass, starting_radius, step_time) # Double mass flux for symetry trick
    masses = []
    # Initial phase
    for i in range(20):
        for j in range(100):
            sim.step()
            if test_initial(sim):
                return test_initial(sim)
        print_status(sim)
        masses.append(ring_mass * sim.n_rings)   ##### TODO remove for initial
    # Average phase
    for i in range(50):
        for j in range(100):
            sim.step()
        if test_average(sim):
            return test_average(sim)  
        masses.append(ring_mass * sim.n_rings)
        print_status(sim)
    #radius = max(sim.radii)
    mass = ring_mass * sim.n_rings
    print('mass', mass, 'avg mass', numpy.mean(masses))
    #quick_plot(sim.radii)
    quick_plot(masses)   
    return "success" 

def recursive_experiment(mass_flux, initial_velocity, ring_mass, starting_radius, step_time):
    outcome = failable_experiment(mass_flux, initial_velocity, ring_mass, starting_radius, step_time)
    print("!"*25, 'OUTCOME', outcome)
    if outcome == "not_enough_rings":
        recursive_experiment(mass_flux, initial_velocity, ring_mass/2, starting_radius, step_time)

if __name__ == "__main__":
    pass
    #experiment(1e23, 1e5, ring_mass=1e30, starting_radius=1e10, step_time=1e5)
    #experiment(2e20, 0, ring_mass=2e27, starting_radius=1.5e11, step_time=1e5) #Drop, water, 1au
    #print(failable_experiment(2e20, 0, ring_mass=2e27, starting_radius=1.5e11, step_time=1e5))
    recursive_experiment(2e20, 0, ring_mass=8e27, starting_radius=1.5e11, step_time=1e5)
    
    
