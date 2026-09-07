'''Implicit Sequences: 隐式序列
**** A sequence can be represented without each element being stored explicitly in the memory of the computer.
**** We can construct an object that provides access to all of the elements of some sequential dataset without
**** computing the value of each element in advance. Instead, we compute elements on demand.
'''

'''Lazy Computation
*** Computing values on demand, rather than retrieving them from an existing representation, is an example of lazy computation.
*** Lazy computation describes any program that delays the computation of a value until that value is needed.
'''
# range() is an example.
r = range(10000, 100000000)
r[45006230] # 45016230

'''Iterator: 迭代器
*** An iterator is an object that provides sequential access to values, one by one.
***
*** The iterator abstraction has two components: 
***     a mechanism for retrieving the next element in the sequence being processed;
***     a mechanism for signaling that the end of the sequence has been reached and no further elements remain.
***
*** An iterator can be obtained by calling the built-in iter() function.
*** The contents of the iterator can be accessed by calling the built-in next() function.
***
*** While not as flexible as accessing arbitrary elements of a sequence (called random access),
*** sequential access to sequential data is often sufficient for data processing applications.
***
*** Built-in Iterators: for lazy computation extensively
***     Several built-in functions(map、filter、zip、reverse) take as arguments iterable values and return iterators.
'''
primes = [2, 3, 5, 7]
type(primes) # <class 'list'>
iterator = iter(primes)
type(iterator) # <class 'list_iterator'>
next(iterator) # 2
next(iterator) # 3
next(iterator) # 5
# The way that Python signals that there are no more values available is 
# to raise a StopIteration exception when next is called.
next(iterator) # 7
next(iterator) # StopIteration
try:
    next(iterator)
except StopIteration:
    print("No more values") # No more values

# built-in 
def double_and_print(x):
    print("***", x, '=>', 2*x, "***")
    return 2*x
s = range(3, 7)
doubled = map(double_and_print, s)
next(doubled) # *** 3 => 6 ***
              # 6


'''Iterables: 可迭代性
*** Iterable Value: Any value that can produce iterators is called an iterable value.
*** Even unordered collections must define an ordering over their contents when they produce iterators.
'''

'''For Statements: operate on iterators.
*** Objects are iterable (an interface) if they have an __iter__ method that returns an iterator.
*** Iterable objects can be the value of the <expression> int the header of a statement.
***
*** The execution of For Statement:
***     First, Python evaluates the header <expression>, which must yield an iterable value.
***     Then, the __iter__ method is invoked on that value.
***     Until a StopIteration exception is raised, Python repeatedly invokes the __next__ method on that iterator 
***      and binds the result to the <name> in the for statement. Then, it executes the <suite>.
'''
counts = [1, 2, 3]
for item in counts:
    print(item)
# implement for statement in terms of while, try and assignment statements.
iterms = counts.__iter__()
try:
    while True:
        item = iterms.__next__()
        print(item)
except StopIteration:
    pass

'''Generators and Yield Statements: 生成器和Yield语句
*** A generator is an iterator returned by a special class of function called a generator function.
*** Generator functions are distinguished from regular functions in that they use yield statement to return elements of a series.
'''
def letters_generator():
    '''
    Even though we never explicitly defined __iter__ or __next__ methods, 
    the yield statement indicates that we are defining a generator function. 
    
    When called, a generator function doesn't return a particular yielded value, 
    but instead a generator (which is a type of iterator) that itself can return the yielded values.
    
    A generator object has __iter__ and __next__ methods, and each call to __next__ continues execution of the generator function 
    from wherever it left off previously until another yield statement is executed.
    
    The first time __next__ is called, the program executes statements from the body of the letters_generator function 
    until it encounters the yield statement. Then, it pauses and returns the value of current. 
    yield statements do not destroy the newly created environment, they preserve it for later.
    
    When __next__ is called again, execution resumes where it left off. 
    The values of current and of any other bound names in the scope of letters_generator are preserved across subsequent calls to __next__.
    '''
    current = 'a'
    while current <= 'd':
        yield current
        current = chr(ord(current) + 1)

for letter in letters_generator():
    print(letter)
# a
# b
# c
# d

# We can walk through the generator by manually calling ____next__()
letters = letters_generator()
type(letters) # class 'genrator'
letters.__next__() # 'a'
letters.__next__() # 'b'
letters.__next__() # 'c'
letters.__next__() # 'd'
letters.__next__() # StopIteration