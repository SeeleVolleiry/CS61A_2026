# Lab02 Utilities : High-Order Functions, Lambda Expressions

UPPERCASE_SHIFT = 65
LOWERCASE_SHIFT = 97
ALPHA_SHIFT = 26

def letter_to_num(letter):
    """Converts all letters to numbers 0-51, with lowercase letters mapped to
    0-25 and uppercase letters mapped to 26-51
    >>> letter_to_num('a')
    0
    >>> letter_to_num('z')
    25
    >>> letter_to_num('A')
    26
    >>> letter_to_num('Z')
    51
    """
    if letter.isupper():
        return ord(letter)-UPPERCASE_SHIFT + ALPHA_SHIFT
    return ord(letter)-LOWERCASE_SHIFT

def num_to_letter(num):
    """Coverts a number 0-51 to a letter
    >>> num_to_letter(0)
    'a'
    >>> num_to_letter(25)
    'z'
    >>> num_to_letter(26)
    'A'
    >>> num_to_letter(51)
    'Z'
    """
    try:
        num = int(num)
    except ValueError:
        return ' '
    num = num % 52
    if num > 25:
        return chr(num - ALPHA_SHIFT + UPPERCASE_SHIFT)
    return chr(num + LOWERCASE_SHIFT)

def mirror_letter(letter):
    """ Returns the letter in the same position on the other
    side of the alphabet.

    >>> mirror_letter('a')
    'z'
    >>> mirror_letter('z')
    'a'
    >>> mirror_letter('B')
    'Y'
    >>> mirror_letter('C')
    'X'
    """
    if letter.isupper():
        return chr(155 - ord(letter))
    return chr(219 - ord(letter))


def looper(f, delimiter=''):
    """Returns a function that applies function f to every element of an iterable."""
    return lambda iterable: delimiter.join([str(f(i)) for i in iterable])


# Q4: Composite Identity Function
def composite_identity(f, g):
    """
    Return a function with one parameter x that returns True if f(g(x)) is
    equal to g(f(x)). You can assume the result of g(x) is a valid input for f
    and vice versa.

    >>> add_one = lambda x: x + 1        # adds one to x
    >>> square = lambda x: x**2          # squares x [returns x^2]
    >>> b1 = composite_identity(square, add_one)
    >>> b1(0)                            # (0 + 1) ** 2 == 0 ** 2 + 1
    True
    >>> b1(4)                            # (4 + 1) ** 2 != 4 ** 2 + 1
    False
    """
    def is_identity(x):
        if f(g(x)) == g(f(x)):
            return True
        return False
    return is_identity


def sum_digits(y):
    """Return the sum of the digits of non-negative integer y."""
    total = 0
    while y > 0:
        total, y = total + y % 10, y // 10
    return total

def is_prime(n):
    """Return whether positive integer n is prime."""
    if n == 1:
        return False
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True

# Q5: Cound Cond-> 从count_fives()和count_primes两个函数中抽象出一个高阶函数,见lab02.md文件
def count_cond(condition):
    """Returns a function with one parameter N that counts all the numbers from
    1 to n that satisfy the two-argument predicate function Condition, where
    the first argument for condition is n and the second argument is the
    number from 1 to n.

    >>> count_fives = count_cond(lambda n, i: sum_digits(n * i) == 5)
    >>> count_fives(10)   # 50 (10 * 5)
    1
    >>> count_fives(50)   # 50 (50 * 1), 500 (50 * 10), 1400 (50 * 28), 2300 (50 * 46)
    4

    >>> is_i_prime = lambda n, i: is_prime(i) # need to pass 2-argument function into count_cond
    >>> count_primes = count_cond(is_i_prime)
    >>> count_primes(2)    # 2
    1
    >>> count_primes(3)    # 2, 3
    2
    >>> count_primes(4)    # 2, 3
    2
    >>> count_primes(5)    # 2, 3, 5
    3
    >>> count_primes(20)   # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    def is_condition(n):
        i = 1
        count = 0
        while i <= n:
            if condition(n, i) == True:
                count += 1
            i += 1
        return count
    return is_condition


from operator import add, sub

def caesar_generator(num, op):
    """Returns a one-argument Caesar cipher function. The function should "rotate" a
    letter by an integer amount 'num' using an operation 'op' (either add or
    sub).

    You may use the provided `letter_to_num` and `num_to_letter` functions,
    which will map all lowercase letters a-z to 0-25 and all uppercase letters
    A-Z to 26-51.

    >>> letter_to_num('a')
    0
    >>> letter_to_num('c')
    2
    >>> num_to_letter(3)
    'd'

    >>> caesar2 = caesar_generator(2, add)
    >>> caesar2('a')
    'c'
    >>> brutus3 = caesar_generator(3, sub)
    >>> brutus3('d')
    'a'
    """
    # 拿到num -> op(letter_to_num(ch), num) -> num_to_letter(op)
    # 所以，lambda表达式将字母转换为数字，并应用op(),返回一个字符
    return lambda ch: num_to_letter( op(letter_to_num(ch), num) )


def is_palindrome(n):
    """
    Fill in the blanks '_____' to check if a number
    is a palindrome.

    >>> is_palindrome(12321)
    True
    >>> is_palindrome(42)
    False
    >>> is_palindrome(2015)
    False
    >>> is_palindrome(55)
    True
    """
    x, y = n, 0
    f = lambda: y * 10 + x % 10
    while x > 0:
        x, y = x // 10, f()
    return y == n

# Q2 of lab02
def cake():
    print('beets')
    def pie():
        print('sweets')
        return 'cake'
    return pie
chocolate = cake()
more_chocolate, more_cake = chocolate(), cake
def snake(x, y):
    if cake == more_cake:
        return chocolate
    else:
        return x + y