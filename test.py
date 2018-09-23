from experiments import *
#recursive_experiment(2e20, 0, ring_mass=5e10, starting_radius=1.5e11, step_time=1e1)
mass, velocity = experiment_wrapper(2e20, 1.5e11)
print(mass, velocity)