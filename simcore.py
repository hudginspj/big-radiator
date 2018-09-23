# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 11:47:35 2018

@author: pjhud
"""
from math import *

#!!!!!!!!!! Point 1 is acting on point 2
G = 6.673e-11
n_points_in_ring = 100


def point_accel(r_1, theta_1, r_2, m):
    x_1 = r_1 * cos(theta_1)
    y_1 = r_1 * sin(theta_1)
    delta_x = x_1 - r_2
    distance = sqrt(delta_x * delta_x + y_1 * y_1)
    accel = G * m * delta_x / (distance * distance * distance)  #See derivation
    #print(theta_1, accel)
    return accel

#for i in range(500):
#    theta = 2 * pi * i / 1000
#    accel = point_accel(10000, theta, 5000, 1e15)
    



def ring_accel(r_ring_1, r_2, ring_mass):
    total_accel = 0.0
    for i in range(n_points_in_ring//2):
        theta = 2 * pi * (i + 0.5) / n_points_in_ring
        point_mass = ring_mass / n_points_in_ring
        accel = point_accel(r_ring_1, theta, r_2, point_mass)
        #print(theta, accel)
        total_accel += accel
    return total_accel
    

#for i in range (250, 20250, 500):
#    print(i, ring_accel(10000, i))


# mass_flux & step time -> ring mass
#starting_radius = 1e10
#step_time = 1e5
#ring_mass = 1e30#####1e29
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
        self.add_ring()
        
    def add_ring(self):
        self.radii.append(self.starting_radius)
        self.velocities.append(self.initial_velocity)
        self.n_rings += 1
        self.rings_added += 1
        
    def step(self):
        stable = True
        self.t += self.step_time
        
        if self.mass_flux * self.t > self.ring_mass * self.rings_added:
            
            #print(self.mass_flux * self.t, ring_mass * self.n_rings)
            self.add_ring()
        
        new_radii = []
        new_velocities = []
        accels = []
        for i in range(self.n_rings): # accelerating ring
            a = 0.0
            for j in range(self.n_rings):  #force rings
                a += ring_accel(self.radii[j], self.radii[i], self.ring_mass)
            accels.append(a)
            v = self.velocities[i]
            r = self.radii[i]
            new_r = r + v * self.step_time + 0.5 * a * self.step_time * self.step_time
            new_v = v + a * self.step_time
            if new_r < 0 or (new_v > 0 and v < 0):
                print("done", new_r, new_v, v)
                self.n_rings -= 1
                #exit(0)
            else:
                new_radii.append(new_r)
                new_velocities.append(new_v)
        for i in range(1, self.n_rings-1):
            if new_radii[i] - new_radii[i+1] < new_radii[i-1] - new_radii[i]:
                stable = False
                #print("fliping!")
                new_radii[i] = (new_radii[i+1] + new_radii[i-1]) / 2
            # if new_velocities[i] > new_velocities[i+1]:
            #     #print("fixed velocity")
            #     new_velocities[i] = (new_velocities[i] + new_velocities[i+1])/2
            #     new_velocities[i+1] = (new_velocities[i] + new_velocities[i+1])/2
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

    
