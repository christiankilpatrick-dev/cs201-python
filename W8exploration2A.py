#Week 8 Exploration 2A

import os

os.chdir("C:\\CS201")

import csv

def compute_surface_gravity(mass, diameter):
    """"
    Computes the surface gravity relative to Earth.
    (Mass in 10**24 kg, diameter in km)

    """
    return (mass / 5.97) * (12756 / diameter)**2


with open('planetdata.csv') as csv_file:
    csv_reader = csv.reader(csv_file)

    planet_names = next(csv_reader) #first row contains planets
    planet_masses = next(csv_reader) #2nd row contains masses
    planet_diameters = next(csv_reader) #3rd row contains diameters

    for i in range(1, len(planet_names)):
        print(planet_names[i].strip())

        mass = float(planet_masses[i])
        diameter = float(planet_diameters[i])

        print(f'Mass: {mass}E24 kg')
        print(f'Diameter: {diameter} km')

        #here is the formula for computing surface gravity relative to Earth's
        surface_gravity = compute_surface_gravity(mass, diameter)
        print(f'Gravity: {surface_gravity: .2f} of Earth at that diameter')

        print()
