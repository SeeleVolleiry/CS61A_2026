'''Mutable Data: 可变数据 -> Modular
*** Object Metaphor: 对象隐喻
*** Sequence Object
*** Dictionaries
'''

# Object Metaphor

# Objects combine data values with behavior. In Python, all values are objects.

# Objects represent information, but also behave like the things that they represent.

# Objects are both information and processes, bundled together 
# to represent the properties, interactions, and behaviors of complex things.

# Object behavior is implemented in Python through specialized object syntax and associated terminology
from datetime import date
tues = date(2014, 5, 13)
print(date(2014, 5, 19) - tues) # 6 days, 0:00:00

# Objects have attributes, which are named values that are part of the object. 
# In Python, like many other programming languages, we use dot notation to designated an attribute of an object.
# <expression>.<name>
tues.year # 2014

# Objects also have methods, which are function-valued attributes. 方法是值为函数的属性
tues.strftime("%A, %B, %D")
"1234".isnumeric() # True
"rOBERT dE nIRO".swapcase() # "Robert De Niro"
"eyes".upper().endswith("YES") # True

# Lists are mutable. Mutable objects are used to represent values that change over time.
# With mutable data, methods called on one name can affect another name at the same time.
chinese = ['coin', 'string', 'myriad']
suits = chinese
suits.pop()
suits.remove('string')
suits.append('cup')
suits.extend(['sword', 'club'])
suits[2] = 'spade'
suits[0:2] = ['heart', 'diamond'] # finally, suits and chinese are also same.

suits = ['heart', 'diamond', 'spade', 'club']
nest = list(suits)
nest[0] = suits
suits.insert(2, 'Joker')
joke = nest[0].pop(2) # Not same as above example
# Python includes two comparison operators, called is and is not, 
# that test whether two expressions in fact evaluate to the identical object.
suits is nest[0] # True
suits is ['heart', 'diamond', 'spade', 'club'] # False check for identity.
suits == ['heart', 'diamond', 'spade', 'club'] # True check for equality of contents.

from unicodedata import lookup

[lookup("WHITE" + s.upper() + "SUIT") for s in suits] # ['♡', '♢', '♤', '♧']

# Tuples:  immutable
# it is possible to change the value of a mutable element contained within a tuple.
code = ("up", "up", "down", "down") + ("left", "right") * 2
len(code) # 8
code[3] # 'down'
code.count("down") # 2
code.index("left") # 4

'''Dictionary: 字典 key-value pairs
*** Dictionaries are Python's built-in data type for storing and manipulating correspondence relationships.
*** Dictionaries are unordered collections of key-value pairs.
***
*** A key of a dictionary cannot be or contain a mutable value,
*** and there can be at most one value for a given key.
***
*** Dictionary Comprehension
'''
numerals = {'I':1.0, 'V':5, 'X':10}
numerals['X'] # 10 element selection
numerals['I'] = 1 # modify / change
numerals['L'] = 50 # add
sum(numerals.values()) # 66
dict([(3,9), (4,16), (5,25)]) # {3: 9, 4: 6, 5: 25}
numerals.get('A', 0) # 0
numerals.get('V', 0) # 5

{x: x*x for x in range(3,6)} # {3: 9, 4: 16, 5: 25}

'''Local State
*** nonlocal: non-local assignment is a powerful tool for creating modular programs.
*** In particular, non-local assignment has given us the ability to maintain some state that is local to a function, 
*** but evolves over successive calls to that function. 
'''
# nonlocal
def make_withdraw(balance):
    """Return a withdraw function that draws down balance with each call.
    The nonlocal statement changes all of the remaining assignment statements in the definition of withdraw.
    After executing nonlocal balance, any assignment statement with balance on the left-hand side of = 
    will not bind balance in the first frame of the current environment. 
    Instead, it will find the first frame in which balance was already defined and re-bind the name in that frame.
    If balance has not previously been bound to a value, then the nonlocal statement will give an error.
    """
    def withdraw(amount):
        nonlocal balance                 # Declare the name "balance" nonlocal
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount       # Re-bind the existing balance name
        return balance
    return withdraw

wd = make_withdraw(20)
wd(5)
wd(3)
# The benefits of non-local assignment
# each instance of withdraw maintains its own balance state, but that state is inaccessible to any other function in the program.
wd = make_withdraw(20)
wd2 = make_withdraw(7)
wd2(6)
wd(8)
# The cost of Non-local assignment
# In this case, calling the function named by wd2 did change the value of the function named by wd,
# because both names refer to the same function.
wd = make_withdraw(12)
wd2 = wd
wd2(1)
wd(1)

'''Implementing Lists and Dictionary: 列表和字典的实现
*** Python 语言并不让我们直接访问列表的实现细节，而只提供了语言内置的可以变更数据的方法。
*** 为了理解如何使用具有局部状态的函数来表示可变列表，我们现在将开发一个可变链表的实现。

*** 我们可以在 dispatch 函数体中添加额外的 elif 子句，每个子句检查一条消息（例如，'extend' ）并直接对内容应用适当的更改。
*** 将对数据值的所有操作的逻辑封装在一个响应不同消息的函数中，是一种称为消息传递的能力。
*** 使用消息传递的程序定义了调度函数，每个函数都可能具有局部状态，并通过将“消息”作为第一个参数传递给这些函数来组织计算。消息是对应于特定行为的字符串。
'''

import ch_2_3

def mutable_link():
    """返回一个可变链表的函数
    In this case, we use a list of key-value pairs to store the contents of the dictionary.
    Each pair is a two-element list.
    
    函数代码见2_3.py.若是想要作为模块导入，需要变更文件名，Python模块必须以字母或者下划线开头。
    """
    contents = 'empty'
    def dispatch(message, value=None):
        nonlocal contents
        if message == 'len':
            return ch_2_3.len_link(contents)
        elif message == 'getitem':
            return ch_2_3.getitem_link(contents, value)
        elif message == 'push_first':
            contents = ch_2_3.link(value, contents)
        elif message == 'pop_first':
            f = ch_2_3.first(contents)
            contents = ch_2_3.rest(contents)
            return f
        elif message == 'str':
            return ch_2_3.join_link(contents, ", ")
    return dispatch

def dictionary():
    """返回一个字典的函数实现"""
    records = []
    def getitem(key):
        matches = [r for r in records if r[0] == key]
        if len(matches) == 1:
            key, value = matches[0]
            return value
    def setitem(key, value):
        nonlocal records
        non_matches = [r for r in records if r[0] != key]
        records = non_matches + [[key, value]]
    def dispatch(message, key=None, value=None):
        if message == 'getitem':
            return getitem(key)
        elif message == 'setitem':
            setitem(key, value)
    return dispatch

'''Dispatch Functions
*** Dispatch function is a general method for implementing a message passing interface for abstract data.
***
*** Dispatch dictionaries:
****    Instead of using conditionals to implement dispatching, we can use dictionaries with string keys
'''

def account(initial_balance):
    def deposit(amount):
        dispatch["balance"] += amount
        return dispatch["balance"]
    def withdraw(amount):
        if amount > dispatch["balance"]:
            return "Insufficient Funds"
        dispatch["balance"] -= amount
        return dispatch["balance"]
    dispatch = {
        "deposit": deposit,
        "withdraw": withdraw,
        "balance": initial_balance        
    }
    return dispatch

def withdraw(account, amount):
    return account["withdraw"](amount)
def deposit(account, amount):
    return account["deposit"](amount)
def check_balance(account):
    return account["balance"]

a = account(20)
deposit(a, 5)
withdraw(a, 17)
check_balance(a)

'''Propagating Constraints: 约束传递
*** declarative programming:声明式编程
'''
# Example: temperature computation-- Celsius & Fahrenheit
from operator import add, mul, sub, truediv

def convert(c, f):
    '''Connect c to f with constraints to convert from Celsius to Fahrenheit'''
    u, v, w, x, y = [connector() for _ in range(5)]
    multiplier(c, w, u)
    multiplier(v, x, u)
    adder(v, y, f)
    constant(w, 9)
    constant(x,5)
    constant(y, 32)

def adder(a, b, c):
    '''The constraint that a + b = c'''
    return make_ternary_constraint(a, b, c, add, sub, sub)

def make_ternary_constraint(a, b, c, ab, ca, cb):
    '''The constraint that ab(a,b) = c, ca(c,a) = b, cb(c, b) = a'''
    def new_value():
        av, bv, cv = [connector["has_val"]() for connector in (a, b, c)]
        if av and bv:
            c["set_val"](constraint, ab(a["val"], b["val"]))
        elif av and cv:
            b["set_val"](constraint, ca(c["val"], a["val"]))
        elif bv and cv:
            a["set_val"](constraint, cb(c["val"], b["val"]))
    def forget_value():
        for connector in (a, b, c):
            connector["forget"](constraint)
    constraint = {"new_val": new_value, "forget": forget_value}
    for connector in (a, b, c):
        connector["connect"](constraint)
    return constraint
# multipier() is similar to adder()
def multiplier(a, b, c):
    '''The constraint that a * b = c'''
    return make_ternary_constraint(a, b, c, mul, truediv, truediv)

def constant(connector, value):
    '''The constraint that connector = value'''
    constraint = []
    connector["set_val"](constraint, value)
    return constraint

def connector(name=None):
    '''A connector between constraints'''
    informant = None
    constraints = []
    def set_value(source, value):
        nonlocal informant
        val = connector["val"]
        if val is None:
            informant, connector["val"] = source, value
            if name is not None:
                print(name, '=', value)
            inform_all_except(source, "new_val", constraints)
        else:
            if val != None:
                print("Contradiction detected:", val, "vs", value)
    def forget_value(source):
        nonlocal informant
        if informant == source:
            informant, connector["val"] = None, None
            if name is not None:
                print(name, "is forgotten")
            inform_all_except(source, "foget", constraints)
    connector = {
        "val": None,
        "set_val": set_value,
        "forget": forget_value,
        "has_val": lambda: connector["val"] is not None,
        "connect": lambda source: constraints.append(source)
    }
    return connector

def inform_all_except(source, message, constraints):
    '''Inform all constraints of the message except source'''
    for c in constraints:
        if c != source:
            c[message]()

celsius = connector("Celsius")
fahrenheit = connector("Fahrenheit")