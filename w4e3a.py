#w4e3a

EARTH_MASS = 5.97E24
EARTH_DIAMETER = 12756

def surface_gravity(mass, diameter):
    """
    Computes the surface gravity of a planet, relative to the gravity on Earth.
    Provide the mass in kg and the diameter in m.
    """
    if (mass < 0):
        raise Exception('Mass should be positive')
    if (diameter < 0):
        raise Exception('Diameter should be positive')
    return (mass / EARTH_MASS) * (EARTH_DIAMETER / diameter)**2


def display_favorite(student_name, planet_name, planet_mass, planet_diameter):
    """
    Prints out information about a student
    """
    message = 'My name is '+student_name+', and my favorite planet is '+planet_name
    gravity = surface_gravity(planet_mass, planet_diameter)
    message = message + '. Its gravity is '+str(gravity)+' as much as Earth.'
    print(message)
    if (gravity > 1.0):
        print("That's a lot of gravity")
    if (gravity == 1.0):
        print("That is my home!")



display_favorite("Mindie", "Earth", 5.97E24, 12756)

