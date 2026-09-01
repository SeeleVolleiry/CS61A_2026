'''Sequences: an ordered collection of values
***Python includes several native data types that are sequences, the most important of which is the list.
'''

from operator import add

# List
digits = [1, 8,2, 8]
len(digits) # 4
digits[3] # 8

[2, 7] + digits * 2 # [2, 7, 1, 8, 2, 8, 1, 8, 2, 8]
pairs = [[10, 20], [30, 40]]
pairs[1] # [30, 40]
pairs[1][0] # 30

# Sequence Iteration: for statement
def count(s, value):
    # Compute the number of occurences of value in sequence s.
    total = 0
    for elem in s:
        if elem == value:
            total = total + 1
    return total

# This pattern of binding multiple names to multiple values in a fixed-length sequence is called sequence unpacking
pairs = [[1,2], [2,2], [2,3],[2,4]]
same_count = 0
for x, y in pairs:
    if x == y:
        same_count = same_count + 1
print(same_count) # 2

# range: a built-in type of sequence in Pyhton, representing a range of integers.
range(1, 10) # integers in [1, 10): 1, 2, 3, 4, 5, 6, 7, 8, 9
range(4) # range(0, 4)
list(range(5, 8)) # [5, 6, 7]

for _ in range(0, 3): # single unscore is for the name not using in the suite of "for"
    print("Go Bears!")

'''Sequence Processing: 序列处理
*** List Comprehension: 列表推导式——包括对每个元素进行映射、选择子集两种
*** Aggregation:聚合
*** Menbership
*** Slicing
'''
'''List Comprehension Form: [ <map expression> for <name> in <sequence expression> if <filter expression> ]
*** To evaluate a list comprehension, Python evaluates the <sequence expression>, which must return an iterable value.
*** Then, for each element in order, the element value is bound to <name>, the filter expression is evaluated,
*** and if it yields a true value, the map expression is evaluated.
*** The values of the map expression are collected into a list.
'''
odds = [1, 3, 5, 7, 9]

[x + 1 for x in odds] # [2, 4, 6, 8, 10]
[x for x in odds if  25 % x == 0] # [1, 5]

'''Aggregation: aggregate all values in a sequence into a single value.
*** sum min max are examples functions.
'''
# Example of sequence processing
# e.g. compute perfect number
def divisors(n):
    '''
    >>>divisors(4)
    [1, 2]
    >>>divisors(12)
    [1, 2, 3, 4, 6]
    '''
    return [1] + [x for x in range(2, n) if n % x == 0]
[n for n in range(1, 1000) if n == sum(divisors(n))] # compute the perfect number, [6, 28, 496]
# finding the minimum perimeter of a rectangle with integer side lengths, given its area
def width(area, height):
    '''
    >>>area = 80
    >>>width(area, 5)
    16
    '''
    assert area % height == 0, "Invalid pairs of area and height"
    return area // height
def perimeter(width, height): # 周长
    '''
    >>>area = 80
    >>>perimeter(16, 5)
    42
    '''
    return 2 * (width + height)

def minimum_perimeter(area):
    '''
    >>>area = 80
    >>>minimum_perimeter(area)
    36
    '''
    heights =divisors(area)
    perimeters = [perimeter(width(area, h), h) for h in heights]
    return min(perimeters)

# Sequence Processing -> Higher-Order Function
# evaluate an expression for each element in sequence.
def  apply_to_all(map_fn, s):
    return [map_fn(x) for x in s]
# Selecting subset
def keep_if(filter_fn, s):
    return [x for x in s if filter_fn(x)]
# aggregation
def reduce(reduce_fn, s, initial):
    reduced = initial
    for x in s:
        reduced = reduce_fn(reduced, x)
    return reduced

def divisors_of(n):
    divides_n = lambda x : n % x == 0
    return [1] + keep_if(divides_n, range(2,n))
def sum_of_divisors(n):
    return sum(divisors_of(n))
def perfect(n):
    return sum_of_divisors(n) == n

# Membership： two operators -> in and not in 
2 in digits # True
1828 not in digits # True

# Slicing: A slice of a sequence is any contiguous span of the original sequence, designated by a pair of integers.
# In Python, sequence slicing is expressed similarly to element selection, using square brackets.
digits[0:2] # [1,8]
digits[1:] #[8, 2, 8]

'''Strings: Dive Into Python3 -> Chapter4.Strings
*** The native data type for text in Python is called a string, and corresponds to the constructor str().
***
*** String literals can express arbitrary text, surrounded by either single or double quotation marks.
*** String is sequence too.Python does not have a separate character type; any text is a string, 
*** and strings that represent single characters have a length of 1.
***
*** The behavior of strings diverges from other sequence types in Python. 
'''

str1 = 'I am a string!'
str2 = "I have got an apostrophe"
str3 = '您好'
str4 = "Berkeley" + ", CA" # "Berkeley, CA"
str5 = "Shabu" * 2 # "Shabu Shabu"
"here" in "Where's Waldo?" # True

str6 = """The zen of Python # length of "\n" is 1.
claims, Readability counts.
Read more: important this.""" # "The zen of Python\nclaims, Readability counts.\nRead more: important this."

str7 = str(2) + " is an element of " + str(digits) # "2 is an element of [1, 8, 2, 8]"

'''Trees
*** Closure Property: 闭包性
*** The data abstraction for a tree consists of the constructor tree() and the selectors label() and branches(). 
'''
def tree(root_label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [root_label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branches):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def fib_tree(n):
    if n==0 or n==1:
        return tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        return tree(fib_tree(n), [left, right])