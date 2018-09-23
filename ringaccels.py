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


def layer_accel(r_ring_1, r_2, ring_mass):
    total_accel = 0.0
    for i in range(n_points_in_ring//2):
        theta = 2 * pi * (i + 0.5) / n_points_in_ring
        point_mass = ring_mass / n_points_in_ring
        accel = point_accel(r_ring_1, theta, r_2, point_mass)
        #print(theta, accel)
        total_accel += accel
    return total_accel
    

