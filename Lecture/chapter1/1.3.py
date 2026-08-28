'''
Function definitions consist of a def statement that indicates a <name> 
and a comma-separated list of named <formal parameters>,
then a return statement, called the function body, 
that specifies the <return expression> of the function
'''
from math import add, mul, truediv, floordiv

def square(x):
    return mul(x, x)

def sum_squares(x, y):
    return add(square(x), square(y))

square(-2)
truediv(-5, 4)
floordiv(-5, 4)
result = sum_squares(5, 12)