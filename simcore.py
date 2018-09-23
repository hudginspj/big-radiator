# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 11:47:35 2018

@author: pjhud
"""
from math import *
import ringaccels as accelfuncs
#import sphereaccels as accelfuncs

class Sim:
    def __init__(self, mass_flux, initial_velocity, ring_mass=1e30, starting_radius=1e10, step_time=1e5):
        self.mass_flux = mass_flux
        self.initial_velocity = initial_velocity
        self.ring_mass=ring_mass
        self.starting_radius = starting_radius
        self.step_time = step_time
        self.radii = []
        self.velocities = []
        self.n_rings = 0
        self.rings_added = 0
        self.t = 0
        self.steps = 0
        self.add_ring()
        
    def add_ring(self):
        self.radii.append(self.starting_radius)
        self.velocities.append(self.initial_velocity)
        self.n_rings += 1
        self.rings_added += 1
        
    def step(self):
        stable = True
        self.t += self.step_time
        self.steps += 1
        
        if self.mass_flux * self.t > self.ring_mass * self.rings_added:
            
            #print(self.mass_flux * self.t, ring_mass * self.n_rings)
            self.add_ring()
        
        new_radii = []
        new_velocities = []
        accels = []
        for i in range(self.n_rings): # accelerating ring
            a = 0.0
            for j in range(self.n_rings):  #force rings
                a += accelfuncs.layer_accel(self.radii[j], self.radii[i], self.ring_mass)
            accels.append(a)
            v = self.velocities[i]
            r = self.radii[i]
            new_r = r + v * self.step_time + 0.5 * a * self.step_time * self.step_time
            new_v = v + a * self.step_time
            if new_r < 0 or (new_v > 0 and v < 0):
                #print("done", new_r, new_v, v)
                self.n_rings -= 1
                #exit(0)
            else:
                new_radii.append(new_r)
                new_velocities.append(new_v)
        for i in range(1, self.n_rings-1):   ############## Stabilization
            if new_radii[i] - new_radii[i+1] < new_radii[i-1] - new_radii[i]:
                stable = False
                #print("fliping!")
                new_radii[i] = (new_radii[i+1] + new_radii[i-1]) / 2
        #     #### if new_velocities[i] > new_velocities[i+1]:
        #     #####     #print("fixed velocity")
        #     #####     new_velocities[i] = (new_velocities[i] + new_velocities[i+1])/2
        #     ####     new_velocities[i+1] = (new_velocities[i] + new_velocities[i+1])/2
        #print(self.radii, new_radii)
        #print("radii", new_radii, 'velocities', new_velocities)#, accels)
        self.radii = new_radii
        self.velocities = new_velocities
        return stable 



if __name__ == "__main__":
    sim = Sim(1e23, 1e5)
    while sim.radii[0] > 0: 
        for i in range(100):
            sim.step()
        #print('velocities', sim.velocities)
        #print("radii", sim.radii)
        print('max radius', max(sim.radii), sim.n_rings, sim.rings_added, sim.radii[0])
        #input("press enter")

    
