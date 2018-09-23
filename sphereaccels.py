# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 11:47:35 2018

@author: pjhud
"""
from math import *

#!!!!!!!!!! Point 1 is acting on point 2
G = 6.673e-11
#n_points_in_ring = 100

def layer_accel(r_shell_1, r_2, layer_mass):
    if r_shell_1 > r_2:
        return 0
    else: 
        return G * layer_mass / (r_2 * r_2)

    

