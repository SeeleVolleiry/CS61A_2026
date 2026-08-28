# Designing Functions

# Documentation: Docstring、 Commnets
# The first line describes the job of the function in one line.
# The following lines can describe arguments and clarify the behavior of the function
def pressure(v, t, n):
    '''Compute the pressure in pascals of an ideal gas
    Applies the ideal gas law: http://en.wikipedia.org/wiki/Ideal_gas_law

    v -- volume of gas, in cubic meters
    t -- absolute temperature in degress kelvin
    n -- particles of gas
    '''
    k = 1.38e-23 # Boltzmann's constant
    return n * k * t / v

# Default argument values
def pressure_n_mole(v, t, n=6.022e23):
    '''Compute the pressure in pascals of an ideal gas
    Applies the ideal gas law: http://en.wikipedia.org/wiki/Ideal_gas_law

    v -- volume of gas, in cubic meters
    t -- absolute temperature in degress kelvin
    n -- particles of gas (default: one mole)
    '''
    k = 1.38e-23 # Boltzmann's constant
    return n * k * t / v