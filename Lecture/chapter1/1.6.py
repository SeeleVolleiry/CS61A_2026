# 高阶函数 High-order Funtions：functions that manipulate other functions.
# 更广泛、笼统的概念： 如从求平方和、自然数和各种具体求和，抽象到“求和”

from math import sqrt

# Functions as Arguments
def sum_naturals1(n):
    '''Compute the natural numbers up to n'''
    total, k = 0, 1
    while k < n:
        total, k = total + k, k + 1
    return total

def sum_cubes1(n):
    '''Compute the sum of the cubes of natural numbers up to n'''
    total, k = 0, 1
    while k <= n:
        total, k = total + k*k*k, k + 1
    return total

def pi_sum1(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + 8 / ((4*k-3)*(4*k-1)), k + 1
    return total

# 以上三个函数，有很大一部分代码是相通的
# expresses the concept of summation itself rather than 
# only functions that compute particular sums.
'''
def <name>(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + <term>(k), k + 1
    return total
'''
def summation(n, term):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

def cube(x):
    return x*x*x
def sum_cubes(n):
    return summation(n, cube)
result1 = sum_cubes(3)

def identity(x):
    return x
def sum_naturals(n):
    return summation(n, identity)
result2 = sum_naturals(10)

def pi_term(x):
    return 8 / ((4*x - 3) * (4*x - 1))
def pi_sum(n):
    return summation(n, pi_term)
result3 = pi_sum(1e6)

# FUnctions as General Methods: 通用方法，更为广泛的算法或者计算步骤之类的
# 同样是函数作为参数的实例、重要作用。
'''
A general method / algorithm for iterative improvemnt
It doesn't specify what problem is being solved.
those details are left to the update and close functions passed in as arguments.
'''
def improve(upgrade, close, guess=1):
    while not close(guess):
        guess = upgrade(guess)
    return guess

# 构建具体的upgrade、 close函数计算黄金分割率
def golden_upgrade(guess): # upgrade
    return 1 / guess + 1

def square_close_to_successor(guess): # close
    return approx_eq(guess * guess, guess + 1)

def approx_eq(x, y, tolerance=1e-15):
    return abs(x-y) < tolerance

phi_apprpx = improve(golden_upgrade, square_close_to_successor)
# test the function
phi = 1/2 + sqrt(5)/2
def improve_test():
    approx_phi = improve(golden_upgrade, square_close_to_successor)
    assert approx_eq(phi, approx_phi), "phi differs from its approximation"

# Defining Functions III: Nested Definitions
'''
以上的函数，使用函数作为参数，固然十分强大，但是也存在两大缺点：
1.命名太多，全局环境容易混乱，必须保持全局唯一
2.收到特定函数签名的限制：利用的函数的函数。即高阶函数，对参数是有要求的。
    比如，improve()的定义中明确了upgrade只能接受一个参数 ——> guess = upgrade(guess)
嵌套函数定义可以解决这两个问题，因为词法作用域及其带来的“闭包”特性。
 sharing names among nested definitions, thus the inner fumction can refer to names in parent environment
 When a user-defined function is called, the frame created has the same parent as that function.
'''
def average(x, y):
    return (x + y) / 2
'''
def sqrt_upgrade(x, a):
    return average(x, a/x)
此函数需要两个参数
'''
def sqrt(a):
    def sqrt_upgrade(x):
        return average(x, x/a)
    def sqrt_close(x, a):
        return approx_eq(x*x, a)
    return improve(sqrt_upgrade, sqrt_close)

# Functions as Return Values
'''
An important feature of lexically scoped programming languages is that
locally defined functions maintain their parent environment when they are returned. 
'''
def square(x):
    return x * x
def successor(x):
    return x + 1
def compose1(f, g):
    def h(x):
        return f(g(x))
    return h
def f(x):
    '''Never called'''
    return -x
square_successor = compose1(square, successor)
result4 = square_successor(12)

'''
Example: Newton's Method
 This extended example shows how function return values and local definitions
 can work together to express general ideas concisely. 
 迭代公式： Xn+1 = Xn - f(Xn) / f'(Xn)
'''
def newton_upgrade(f, df):
    def upgrade(x):
        return x - f(x) / df(x)
    return upgrade
def find_zero(f, df):
    def near_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_upgrade(f, df), near_zero)

def square_root_newton(a):
    def f(x):
        return x * x - a
    def df(x):
        return 2 * x
    return find_zero(f, df)

def power(x, n):
    product, k = 1, 0
    while k < n:
        product, k = product * x, k+1
    return product

def nth_root_of_a(n, a):
    def f(x):
        return power(x, n) - a
    def df(x):
        return n * power(x, n-1)
    return find_zero(f, df)

'''柯里化：currying
柯里化（Currying）是函数式编程中的一个重要概念，它源自之前我们聊过的高阶函数和闭包。
简单来说，柯里化就是把一个接收多个参数的函数，变成一连串只接收一个参数的函数链。
We can use higher-order functions to convert a function that takes multiple arguments into a chain of functions that each take a single argument.
''' 
def curried_pow(x):
    def h(y):
        return pow(x, y)
    return h
curried_pow(2)(3) # 8



'''Lambda Expression
A lambda expression evaluates to a function that has a single return expression as its body. 
Assignment and control statements are not allowed.
'''
def composel(f, g):
    return lambda x: f(g(x))
# a function that    takes x    and returns     f(g(x))
#      lambda           x            :          f(g(x))
f = composel(lambda x: x*x, lambda y: y+1)
result5 = f(12) # 169


'''First-class Function
一个语言把函数当作“一等公民”，那么函数就和整数、字符串、列表这些普通数据一样，拥有同等的“权利”。
简单来说，就是函数不再只是“动作”，也可以被当作“数据”来传递和操作：
可用于赋值、作为参数、作为返回值、被包含在数据结构中。
'''

'''Function Decrators
装饰器（Decorator）是Python中一种非常强大的高级特性，它本质上就是一个高阶函数 / 闭包.
装饰器用于在不修改原函数代码的前提下，为其动态添加额外的功能。
装饰后，除了函数原有的核心功能之外，多了包装纸赋予的额外特性（比如打印日志、计时、权限校验等）

pythontutor.com：可视化代码运行，可复制代码运行从而理解该内容
'''
def trace(fn): # fn -> function
    def wrapped(x): # wrap 包装
        printf( '->', fn, '(', x, ')' )
        return fn(x)
    return wrapped

@trace # 这里本质上是执行了：triple = trace(triple)
def triple(x):
    return x * 3
'''等价的非装饰器写法：
def triple(x):
    return x * 3
triple = trace(triple)
'''