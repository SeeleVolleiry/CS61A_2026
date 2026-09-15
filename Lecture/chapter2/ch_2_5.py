'''OOP：Object-Oriented Programming 面向对象编程
*** Object-oriented programming (OOP) is a method for organizing programs 
*** that brings together many of the ideas introduced in this chapter.
'''

'''1. Objects and Classes: 对象与类（模板与实例）
*** A class serves as a template for all objects whose type is that class. Every object is an instance of some particular class.
***
*** 创建对象/实例化/instantiate
*** The act of creating a new object instance is known as instantiating the class.
*** The syntax in Python for instantiating a class is identical to the syntax of calling a function.
*** 
*** 属性/attribute：
*** An attribute of an object is a name-value pair associated with the object, which is accessible via dot notation.
*** The attributes specific to a particular object, as opposed to all objects of a class, are called instance attributes.
***  In the broader programming community, instance attributes may also be called fields, properties, or instance variables.
*** 
*** 方法/method：
*** Functions that operate on the object or perform object-specific computations are called methods.
*** Methods are invoked on a particular object.
'''

'''2. Defining the Classes and Methods
*** class statement:
*** class <name>:
***     <suite>
***
*** Methods: 跟定义函数类似
*** Object methods are also defined by a def statement in the suite of a class statement.
*** Each method definition includes a special first parameter self, which is bound to the object on which the method is invoked.
*** To invoke these methods, we again use dot notation.
***
*** Naming Conventions:
*** Class names are conventionally written using the CapWords convention (also called CamelCase).
*** Method names follow the standard convention of naming functions using lowercased words separated by underscores.
'''
class Account:
    # The argument, self, is bound to the newly created Account object.
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
    def deposit(self, amount): # method definition
        self.balance = self.balance + amount
        return self.balance
    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self.balance

# instantiate the Account class.
a = Account('Kirk') # This "call" to the Account class creates a new object that is an instance of Account
                    # then calls the constructor function __init__ with two arguments: 
                    # the newly created object and the string 'Kirk'.

a.balance # 0
a.holder # 'Kirk'

b = Account('Spock')
b.balance = 200
[acc.balance for acc in (a, b)] # [0, 200]

# Identity: 身份、标识、恒等/一致性， is / is not operators。
boolean_1 = a is a # True
boolean_2 = a is not b # True
# As usual, binding an object to a new name using assignment does not create a new object.
# New objects that have user-defined classes are only created when a class is instantiated with call expression syntax.
c = a
boolean_3 = c is a # True

# dot notation to invoke methods
b.deposit(100)
b.withdraw(90)
b.withdraw(90)
b.holder

type(Account.deposit) # <class 'function'>
type(b.deposit) # <class 'method'>

Account.deposit(b, 1001)  # The deposit function takes 2 arguments: 1011
b.deposit(1000)           # The deposit method takes 1 argument: 2011

'''Message passing and Dot expression
*** message passing
*** The central idea in message passing was that data values should have behavior by responding to 
***  messages that are relevant to the abstract type they represent.
*** The dot syntax allows us to use the message name directly.
***
*** Dot Expression
*** A dot expression consists of an expression, a dot, and a name:
***     <expression>.<name>
*** A dot expression evaluates to the value of the attribute with the given <name>, 
***  for the object that is the value of the <expression>.
'''

'''Class Attributes
*** Class attributes are created by assignment statements in the suite of a class statement, outside of any method definition.
*** In the broader developer community, class attributes may also be called class variables or static variables.
*** This attribute can still be accessed from any instance of the class.
***
*** instance attributes are found before class attributes.
'''
class account:
    interest = 0.02 # A class attribute
    def __init__(self, account_holder) -> None:
        self.balance = 0
        self.holder = account_holder
    # Additional methods would be defined here

spock_account = account('Spock')
kirk_account = account('Kirk')
spock_account.interest # 0.02
kirk_account.interest # 0.02

account.interest = 0.04
spock_account.interest # 0.04
kirk_account.interest # 0.04

'''Inheritance: 继承
*** Base class(parent class) and subclass(child class):
***  Similar classes differ in their amount of specialization.
***  Two classes may have similar attributes, but one represents a special case of the other.(例如支票账户和普通/通用账户)
*** A subclass inherits the attributes of its base class, but may override certain attributes, including certain methods.
***  With inheritance, we only specify what is different between the subclass and the base class.
***  Anything that we leave unspecified in the subclass is automatically assumed to behave just as it would for the base class.
***
*** Using Inheritance:
*** We specify inheritance by placing an expression that evaluates to the base class in parentheses after the class name.
***
*** Object Interfaces:
*** An object interface is a collection of attributes and conditions on those attributes.
***
*** Multiple Inheritance:
*** Python supports the concept of a subclass inheriting attributes from multiple base classes,
***  a language feature called multiple inheritance.
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

class CheckingAccount(Account):
    '''A bank account that charges for withdrawals.'''
    withdraw_charge = 1
    interest = 0.01
    def withdraw(self, amount):
        # Calling ancestors
        return Account.withdraw(self, amount + self.withdraw_charge)

checking = CheckingAccount('Sam')
checking.deposit(10) # 10
checking.withdraw(5) # 4
checking.interest # 0.01

class SavingAccount(Account):
    deposit_charge = 2
    def deposit(self, amount):
        return Account.deposit(self, amount - self.deposit_charge)

# Multiple Inheritance
# Ambiguous reference: Python resolves names from left to right, then upwards.
# In below example: AsSeenOnTVAccount, CheckingAccount, SavingsAccount, Account, object
class AsSeenOnTVAccount(CheckingAccount, SavingAccount):
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 1 # A free dollar!

such_a_deal = AsSeenOnTVAccount("John")
such_a_deal.balance # 1
such_a_deal.deposit(20) # $2 fee from SavingsAccount.deposit: 19
such_a_deal.withdraw(5) # $1 fee from CheckingAccount.withdraw: 13

'''The Roles of Objects
The Python object system is designed to make data abstraction and message passing both convenient and flexible.
Object-oriented programming is particularly well-suited to programs that model systems that have separate but interacting parts.
'''
