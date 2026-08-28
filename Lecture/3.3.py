# Exceptions: 异常
# An exception is a object instance with a class that inherits, 
# either directly or indirectly, from the BaseException class.

# 抛出异常：raise statement and assert statement

# 处理异常：try
'''
try:
    <try suite>
exception <exception class> as <name>:
    <except suite>
'''
from math import sqrt

def invert(x):
    result = 1 / x # Raises a ZeroDivsionError of x is 0.
    print("Never printed if x is 0")
    return result

def invert_safe(x):
    try:
        return invert(x)
    except ZeroDivisionError as e:
        return str(e)

class IterImproveError(Exception):
    def __init__(self, last_guess):
        self.last_guess = last_guess

def improve(upgrade, done, guess=1, max_upgrades=1000):
    k = 0
    try:
        while not done(guess) and k < max_upgrades:
            guess = upgrade(guess)
            k = k + 1
            return guess
    except ValueError:
        raise IterImproveError(guess)

def find_zero(f, guess=1):
    def done(x):
        return f(x) == 0
    try:
        return improve(newton_update(f), done, guess)
    except IterImproveError as e:
        return e.last.guess