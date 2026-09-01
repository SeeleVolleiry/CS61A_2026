'''Data Abstraction: 
***The general technique of isolating the parts of a program that deal with how data are represented
***from the parts that deal with how data are manipulated is a powerful design methodology called data abstraction.
***
***Data abstraction isolates how a compound data value is used from the details of how it is constructed.
***
***Abstraction barriers
'''

from operator import getitem
from fractions import gcd

# example of pairs 引入
pair = [10, 20]
x = getitem(pair, 0) # 10
y = getitem(pair, 1) # 20

def rational(n, d):
    g = gcd(n, d)
    return [n/g, d/g]

def numer(x):
    return x(0)

def denom(x):
    return x(1)

def add_rationals(x, y):
    nx, ny = numer(x), numer(y)
    dx, dy = denom(x), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)

def mul_rationals(x, y):
    return rational(numer(x) * numer(y), denom(x) * denom(y))

def print_rational(x):
    print(numer(x), '/', denom(x))

def rationals_are_equal(x, y):
    return numer(x) * denom(y) == numer(y) * denom(x)