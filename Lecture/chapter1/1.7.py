'''Recursive Functions
A function is called recursive if the body of the function calls the function itself,
either directly or indirectly. 
'''
from doctest import *

def sum_digits(n):
    '''return the sum of digits of positive integer n.
    
    >>> sum_digits(9)
    9
    >>> sum_digits(18117)
    18
    >>> sum_digits(9437184)
    36
    >>> sum_digits(11408855402054064613470328848384)
    126
    '''
    if n < 10:
        return n
    else :
        all_but_last, last = n // 10, n % 10
        return sum_digits(all_but_last) + last

'''The anatomy of Recursive Functions:剖析递归函数
    Base Case: A common pattern can be found in the body of many recursive functions.
     The body begins with a base case, a conditional statement that defines the behavior
      of the function for the inputs that are simplest to process.
    Recursive calls: simplify the original problem. Recursive functions express computation
      by simplifying problems incrementally.
    
    Mutual Recursion:互递归，互递归能合并成一个递归函数。
     When a recursive procedure is divided among two functions that call each other, 
        the functions are said to be mutually recursive.
     Mutually recursive functions can be turned into a single recursive function by
        breaking the abstraction boundary between the two functions. 
'''
def fact_iter(n): # iteration version
    total, k = 1, 1
    while k <= n:
        total, k = total * k, k + 1
    return total
def fact(n): # recursive version
    if n == 1:
        return 1
    else :
        return n * fact(n - 1)

def is_even(n):
    if n == 0:
        return True
    else :
        return is_odd(n - 1)
def is_odd(n):
    if n == 0:
        return False
    else :
        return is_even(n - 1)

def isEven(n):
    if n == 0:
        return True
    else :
        if n-1 == 0:
            return False
        else:
            return isEven(n - 2)

result = is_even(4)

def cascade_version1(n):
    '''
    >>> cascade(2013)
    2013
    201
    20
    2
    20
    201
    2013
    '''
    if n < 10:
        print(n)
    else :
        print(n)
        cascade_version1(n // 10)
        print(n)
def cascade_version2(n):
    '''
    >>> cascade(2013)
    2013
    201
    20
    2
    20
    201
    2013
    '''
    if n < 10:
        print(n)
    else :
        print(n)
        cascade_version2(n // 10)
        print(n)

# a pebbles game
def play_alice(n):
    if n == 0:
        print("Bob wins!")
    else :
        play_bob(n -1)
def play_bob(n):
    if n == 0:
        print("Alice wins!")
    elif n % 2 == 0:
        play_alice(n - 2)
    else:
        play_alice(n - 1)
play_alice(20)

'''Tree Recursion:树形递归 a function calls itself more than once.
    each call branches into multiple smaller calls,
    each of which branches into yet smaller calls,
    just as the branches of a tree become smaller
'''
def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n - 2) + fib(n - 1)
result1 = fib(6)

# Example:Partitions
'''
The number of partitions of a positive integer n, using parts up to size m,
is the number of ways in which n can be expressed as the sum of positive integer
parts up to m in increasing order.
For example, the number of partitions of 6 using parts up to 4 is 9.
'''
def count_partitions(n, m):
    '''
    >>> count_partitions(6, 4)
    9
    >>> count_partitions(5, 5)
    7
    >>> count_partitions(10, 10)
    42
    >>> count_partitions(15, 15)
    176
    >>> count_partitions(20, 20)
    627
    '''
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else :
        return count_partitions(n-m, m) + count_partitions(n, m-1)