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
    



def ring_accel(r_ring_1, r_2):
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
starting_radius = 1e10
step_time = 1e5
ring_mass = 1e30#####1e29
class Sim:
    def __init__(self, mass_flux, initial_velocity):
        self.mass_flux = mass_flux
        self.initial_velocity = initial_velocity
        self.radii = []
        self.velocities = []
        self.n_rings = 0
        self.rings_added = 0
        self.t = 0
        self.add_ring()
        
    def add_ring(self):
        self.radii.append(starting_radius)
        self.velocities.append(self.initial_velocity)
        self.n_rings += 1
        self.rings_added += 1
        
    def remove_ring(self, index):
        self.n_rings -= 1
        #self.radii.pop(index)
        #self.velocities.pop(index)
        #print("done")
        raise Exception("done")
        
    def step(self):
        self.t += step_time
        
        if self.mass_flux * self.t > ring_mass * self.n_rings:
            
            #print(self.mass_flux * self.t, ring_mass * self.n_rings)
            self.add_ring()
        
        new_radii = []
        new_velocities = []
        accels = []
        for i in range(self.n_rings): # accelerating ring
            a = 0.0
            for j in range(self.n_rings):  #force rings
                a += ring_accel(self.radii[j], self.radii[i])
            accels.append(a)
            v = self.velocities[i]
            r = self.radii[i]
            new_r = r + v * step_time + 0.5 * a * step_time * step_time
            new_v = v + a * step_time
            if new_r < 0 or (new_v > 0 and v < 0):
                print("done", new_r, new_v, v)
                self.remove_ring(i)
                exit(0)
            else:
                new_radii.append(new_r)
                new_velocities.append(new_v)
        #print(self.radii, new_radii)
        #print("radii", new_radii, 'velocities', new_velocities)#, accels)
        self.radii = new_radii
        self.velocities = new_velocities
        


sim = Sim(1e23, 1e5)
while sim.radii[0] > 0: 
    for i in range(100):
        sim.step()
    print('velocities', sim.velocities)
    print("radii", sim.radii)
    print('max radius', max(sim.radii))
    #input("press enter")




time = 0.0
v = 1e5
r = 1e10
def step():
    global time, v, r
    time += step_time
    a = ring_accel(r, r)
    v_new = v + a * step_time
    r_new = r + v * step_time + 0.5 * a * step_time * step_time
    v = v_new
    r = r_new
    print(v, r, a)
    return r,v
    
#while r > 0:
#    step()


if __name__ == "__main__":
    pass

    
