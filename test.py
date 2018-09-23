import math
from experiments import *

def power(radius, sigma, temp):
    return 2*math.pi*radius**2*sigma*temp**4

def mass_flux(power,c,delta_temp):
    return power/(c * delta_temp)

sigma = 5.67037e-8

#Water
water_c = 4181.3
water_temp = 323
water_delta_temp = 373-273

#Superconducting Lead
lead_c = 297
lead_temp = 6
lead_delta_temp = 9-3

#Beryllium
be_c = 1820
be_temp = 298
be_delta_temp = 373-273

material = "water" #should be either water, lead or be (because I can't spell beryllium)
if material == "water":
    c = water_c
    temp = water_temp
    delta_temp = water_delta_temp
    print()
    print("Material: Water")
    print("---------------")
elif material == "lead":
    c = lead_c
    temp = lead_temp
    delta_temp = lead_delta_temp
    print()
    print("Material: Lead")
    print("--------------")
elif material == "be":
    c = be_c
    temp = be_temp
    delta_temp = be_delta_temp
    print()
    print("Material: Beryllium")
    print("-------------------")

print( "Radius \t\t Power \t\t Mass Flux \t Mass \t\t Velocity" )
radius = 1e11
while radius < 1e20:
    p = power(radius, sigma, temp)
    mf = mass_flux(p, c, delta_temp)
    mass, velocity = experiment_wrapper(mf, radius)
    print("{:.2E} \t {:.2E} \t {:.2E} \t {:.2E} \t {:.2E}".format(radius,p,mf,mass,velocity))
    radius = radius * 10
    

#recursive_experiment(2e20, 0, ring_mass=5e10, starting_radius=1.5e11, step_time=1e1)
#mass, velocity = experiment_wrapper(2e20, 1.5e11)
#print(mass, velocity)