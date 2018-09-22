# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 11:47:35 2018

@author: pjhud
"""
from math import *

time = 0.0
def step():
    global time
    time += 1.0
    points = {}
    n = 10
    for i in range(n):
        theta = 2 * pi * i / n
        x = time * sin(theta)
        y = time * cos(theta)
        z = 0
        points[i]={'x': x, 'y': y, 'z':z, 'age': time}
    #for p in points:
    #    print(p, ':', points[p])
    return points

if __name__ == "__main__":
    print(step())
