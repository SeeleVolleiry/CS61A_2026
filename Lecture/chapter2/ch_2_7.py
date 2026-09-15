'''Object Abstraction
*** 泛型函数：generic function
*** A central concept in object abstraction is a generic function, 
    which is a function that can accept values of multiple different types.
*** 实现泛型函数的三种不同技术：
*** shared interfaces, type dispatching, and type coercion.
'''

'''String Conversion
str()、__str__()、repr()、__repr__()

Certain functions should apply to multiple data types.
One way to create such a function is to use a shared attribute name with a different definition in each class.
'''

'''Special Methods
In Python, certain special names are invoked by the Python interpreter in special circumstances.
    e.g. __init__ method, __str__ method, __repr__ method.

Most commonly used Special Methods/Names:
    True and False values: __bool__
        If an object defines the __bool__ method, then Python calls that method to determine its truth value.
    
    Sequence operations: __len__(), __getitem__
        Python uses a sequence's length to determine its truth value, if it does not provide a __bool__ method.
        Empty sequences are false, while non-empty sequences are true.

    Callable objects: __call__
        With this method, we can define a class that behaves like a higher-order function.

    Arithmetic:算术
'''
class Account: # Base Class
    '''A bank account that has a non-negative balance'''
    interrest = 0.2
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
    def deposit(self, amount):
        '''Increase the account balance by amount and return the new balance.'''
        self.balance = self.balance + amount
        return self.balance
    def withdraw(self, amount):
        '''Decrease the account balance by amount and return the new balance.'''
        if amount > self.balance:
            return 'Insuffcient funds'
        self.balance = self.balance - amount
        return self.balance

# add a __bool__ method to Account
# Account.__bool__ = lambda self: self.balance != 0

def make_adder(n):
    def adder(k):
        return n+k
    return adder

class Adder(object):
    def __init__(self, n):
        self.n = n
    def __call__(self, k):
        return self.n + k

'''Multiple Representation: 多重表示
*** There might be more than one useful representation for a data object.
    We might like to design systems that can deal with multiple representations.
    例如，实数的表示就有直角坐标和极坐标两种。

*** Python 有一种简单的计算属性的特性，可以通过零参数函数实时的计算属性。
    @property 修饰符允许函数在没有调用表达式语法（表达式后跟随圆括号）的情况下被调用。
'''
from operator import add, mul
from math import atan2, sin, cos, pi

class Number:
    def __add__(self, other):
        if self.type_tag == other.type_tag:
            return self.add(other)
        elif (self.type_tag, other.type_tag) in self.adders:
            return self.cross_apply(other, self.adders)

    def __mul__(self, other):
        if self.type_tag == other.type_tag:
            return self.mul(other)
        elif (self.type_tag, other.type_tag) in self.multipliers:
            return self.croos_apply(other, self.multipliers)

    def cross_apply(self, other, cross_fns):
        cross_fns = cross_fns[(self.type_tag, other.type_tag)]
        return cross_fns(self, other)

    adders = {("com", "rat"): add_complex_and_rational, 
              ("rat", "com"): add_rational_and_complex}
    multipliers = {("com", "rat"): mul_complex_and_rational,
                   ("rat", "com"): mul_rational_and_complex}

class Complex(Number):
    def add(self, other): # shared interfaces to implement generic functions.
        # ComplexRI constructs a complex number from real and imaginary parts.
        return ComplexRI(self.real + other.real, self.imag + other.imag)
    def mul(self, other): # shared interfaces to implement generic functions.
        magnitude = self.magnitude * other.magnitude
        # ComplexMA constructs a complex number from a magnitude and angle.
        return ComplexMA(magnitude, self.angle + other.angle)

class ComplexRI(Complex):
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
        @property
        def magnitude(self):
            return (self.real**2 + self.imag**2) ** 0.5
        @property
        def angle(self):
            return atan2(self.imag, self.real)
        def __repr__(self):
            return 'ComplexRI({0:g},{1:g})'.format(self.real, self.imag)

class ComplexMA(Complex):
    def __init__(self, magnitude, angle):
        self.magnitude = magnitude
        self.angle = angle
    @property
    def real(self):
        return self.magnitude * cos(self.angle)
    @property
    def imag(self):
        return self.magnitude * sin(self.angle)
    def __repr__(self):
        return 'ComplexMA({0:g}, {1:g}*pi)'.format(self.magnitude, self.angle)

'''Generic Function: 泛型函数
*** Generic functions are methods or functions that apply to arguments of different types.
***
*** Three technologies to implement generic functions:
*** shared interfaces, type dispatching, type coercion.
'''
from fractions import gcd

class Rational(Number):
    def __init__(self, number, denom):
        g = gcd(number, denom)
        self.number =number //g
        self.denom = denom //g
    def __repr__(self):
        return 'Rational({0}, {1})'.format(self.number, self.denom)
    def add(self, other):
        nx, dy = self.number, other.denom
        ny, dx = other.number, self.denom
        return Rational(nx * dy + ny * dx, dx * dy)
    def mul(self, other):
        number = self.number * other.number
        denom = self.denom * other.denom
        return Rational(number, denom)

# Type dispatching. One way to implement cross-type operations is to select behavior 
# based on the types of the arguments to a function or method. 

'''
*** The idea of type dispatching is to write functions that inspect the type of arguments they receive, 
*** then execute code that is appropriate for those types.
'''
# isinstance() takes an object and a class.
# It returns true if the object has a class that either is or inherits from the given class.
c = ComplexRI(1, 1)
isinstance(c, ComplexRI) # True
isinstance(c, Complex) # True
isinstance(c, ComplexMA) # False

def is_real(c):
    '''Return whether c is a real number with no imaginary part'''
    if isinstance(c, ComplexRI):
        return c.imag == 0
    elif isinstance(c, ComplexMA):
        return c.angle % pi == 0

is_real(ComplexRI(1, 1)) # False
is_real(ComplexMA(2, pi)) # True

# Type dispatching is not always performed using isinstance.
# For arithmetic, we will give a type_tag attribute to Rational and Complex instances that has a string value.
# When two values x and y have the same type_tag, then we can combine them directly with x.add(y). 
# If not, we need a cross-type operation.
def add_complex_and_rational(c, r):
    return ComplexRI(c.real + r.number/r.denom, c.imag)

def mul_complex_and_rational(c,r):
    r_magnitude, r_angle = r.number/r.denom, 0
    if r_magnitude < 0:
        r_magnitude, r_angle = -r_magnitude, pi
    return ComplexMA(c.magnitude * r_magnitude, c.angle + r_angle)

# 对称性
def add_rational_and_complex(r, c):
    return add_complex_and_rational(c, r)

def mul_rational_and_complex(r, c):
    return mul_complex_and_rational(c, r)

class Number: # type dispatching version
    def __add__(self, other):
        if self.type_tag == other.type_tag:
            return self.add(other)
        elif (self.type_tag, other.type_tag) in self.adders:
            return self.cross_apply(other, self.adders)

    def __mul__(self, other):
        if self.type_tag == other.type_tag:
            return self.mul(other)
        elif (self.type_tag, other.type_tag) in self.multipliers:
            return self.croos_apply(other, self.multipliers)

    def cross_apply(self, other, cross_fns):
        cross_fns = cross_fns[(self.type_tag, other.type_tag)]
        return cross_fns(self, other)

    adders = {("com", "rat"): add_complex_and_rational, 
              ("rat", "com"): add_rational_and_complex}
    multipliers = {("com", "rat"): mul_complex_and_rational,
                   ("rat", "com"): mul_rational_and_complex}

'''Coercing: 强制（转换）
*** coercion：
    Often the different data types are not completely independent, and there may be ways by which objects of one type 
    may be viewed as being of another type. This process is called coercion. 
***
*** coercion function:
    we can implement this idea by designing coercion functions that transform an object of one type 
    into an equivalent object of another type.
***
*** Advantages and drawbacks of coercion:
    一些更加精于设计的强制转换方案不仅仅只是尝试将一种类型转换到另一种，而是会尝试将两种不同的类型都转换为第三种通用类型。
    另一种强制转换的扩展是迭代强制转换，将一种数据类型通过中间类型转换到另一种类型。
    强制转换函数可能在应用时丢失信息。
***
'''
# 有理数强制转换为复数
def ratinal_to_complex(r):
    return ComplexRI(r.number / r.denom, 0)

class Number: # coercion version
    def __add__(self, other):
        x, y = self.coerce(other)
        return x.add(y)

    def __mul__(self, other):
        x, y = self.coerce(other)
        return x.mul(y)

    def coerce(self, other):
        if self.type_tag == other.type_tag:
            return self, other
        elif (self.type_tag, other.type_tag) in self.coercions:
            return (self.coerce_to(other.type_tag), other)
        elif (other.type_tag, self.type_tag) in self.coercions:
            return (self, other.coerce_to(self.type_tag))

    def coerce_to(self, other_tag):
        coercion_fn = self.coercions[(self.type_tag, other_tag)]
        return coercion_fn(self)

    coercions = [('rat', 'com'): rational_to_complex]
