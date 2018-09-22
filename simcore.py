# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 11:47:35 2018

@author: pjhud
"""
from math import *

#!!!!!!!!!! Point 1 is acting on point 2
G = 6.673e-11
n_points_in_ring = 1000
ring_mass = 1e24

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
        theta = 2 * pi * i / n_points_in_ring
        point_mass = ring_mass / n_points_in_ring
        accel = point_accel(r_ring_1, theta, r_2, point_mass)
        #print(theta, accel)
        total_accel += accel
    return total_accel
    

#for i in range (250, 20250, 500):
#    print(i, ring_accel(10000, i))




time = 0.0
v = 1e5
r = 1e5
step_time = 1e5
def step():
    global time, v, r
    time += 1.0
    a = accel_ring(r, r)
    v_new = v + a * step_time
    r_new = r + v * step_time + 0.5 * a * step_time * step_time
    v = v_new
    r = r_new
    

if __name__ == "__main__":
    pass
    #step()
    #print(step())
    
