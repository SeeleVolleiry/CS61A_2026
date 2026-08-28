# Control (control statement)

# Compound Statements

# Defining Functions II: Local Assignment
def percent_difference(x, y):
    difference = abs(x-y)
    return 100 * difference / x

result = percent_difference(40, 50)

# Conditional Statement
''' A conditional statement in Python consists of a series of headers and suites: 
    a required if clause, an optional sequence of elif clauses, and finally an optional else clause

    Boolean values: True and False
        comparison operations
        Boolean oprators: and or not
    
    Iteration:迭代
'''

def absolute_value(x):
    '''Compute abs(x)'''
    if x > 0:
        return x
    elif x == 0:
        return 0
    else:
        return -x

result2 = absolute_value(-2)

def fib(n):
    '''Compute the nth fibonacci number, for n >= 2'''
    pred, curr = 0, 1
    k = 2 # which fibnacci number is now?
    while k < n:
        pred, curr = curr, pred + curr
        k = k + 1
    return curr

result3 = fib(8)

# Testing: implementation 测试
# Assertion: assert statement
assert fib(8) == 13, "The 8th Fibnacci number should be 13" #if true, nothing. Othrewise, display the string.

'''
When writing Python in files, rather than directly into the interpreter, 
tests are typically written in the same file or a neighboring file with the suffix _test.py.
'''
def fib_test():
    assert fib(2) == 1, "the 2nd Fibnacci number should be 1"
    assert fib(3) == 1, "the 2nd Fibnacci number should be 1"
    assert fib(50) == 7778742049, "Error at the 50th Fibnacci number"

# Doctests
'''
Python 提供了一种便捷的方法，可以将简单的测试直接放在函数的文档字符串（docstring）中。
文档字符串的第一行应包含函数的简要描述，后跟一个空行，之后可以是对参数和行为的详细描述。
此外，文档字符串还可以包含调用该函数的交互式示例
'''
def sum_naturals(n):
        """Return the sum of the first n natural numbers.

        >>> sum_naturals(10)
        55
        >>> sum_naturals(100)
        5050
        """
        total, k = 0, 1
        while k <= n:
            total, k = total + k, k + 1
        return total

from doctest import testmod, run_docstring_examples
run_docstring_examples(sum_naturals, globals, True)