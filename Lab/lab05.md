# Lab05：Mutability, Iterators, Generators.

# MUtability
## Q1: WWPD: List-Mutation

Important: For all WWPD questions, type Function if you believe the answer is <function...>, Error if it errors, and Nothing if nothing is displayed.

Use Ok to test your knowledge with the following "What Would Python Display?" questions:

    python3 ok -q list-mutation -u

```python
>>> s = [6, 7, 8]
>>> print(s.append(6))
None

>>> s
[6, 7, 8, 6]

>>> s.insert(0, 9)
>>> s
[9, 6, 7, 8, 6]

>>> x = s.pop(1)
>>> s
[9, 7, 8, 6]

>>> s.remove(x)
>>> s
[9, 7, 8]

>>> a, b = s, s[:]
>>> a is s
True

>>> b == s
True

>>> b is s
False

>>> a.pop()
8

>>> a + b
[9, 7, 9, 7, 8]

>>> s = [3]
>>> s.extend([4, 5])
>>> s
[3, 4, 5]

>>> a
[9, 7]

>>> s.extend([s.append(9), s.append(10)])
>>> s
[3, 4, 5, 9, 10, None, None]
```

## Q2: Insert Items

Write a function that takes in a list s, a value before, and a value after.
It modifies s in place by inserting after just after each value equal to before in s.
It returns s.

Important: 
    
    No new lists should be created.
    插入新的元素后，列表的长度会发生变化，需要遍历的索引序列也会发生变化。

Note: If the values passed into before and after are equal, make sure you're not creating an infinitely long list while iterating through it. If you find that your code is taking more than a few seconds to run, the function may be in an infinite loop of inserting new values.

## Q3: Group By

补全函数代码，是函数能够按照处理后的值分组，返回一个字典。

Write a function that takes in a list s and a function fn, and returns a dictionary that groups the elements of s based on the result of applying fn.

    The dictionary should have one key for each unique result of applying fn to elements of s.
    The value for each key should be a list of all elements in s that, when passed to fn, produce that key (what it evaluates to).

In other words, for each element e in s, determine fn(e) and add e to the list corresponding to fn(e) in the dictionary.

# Iteraotors

## Q4: WWPD： Iterators

Important: Enter StopIteration if a StopIteration exception occurs, Error if you believe a different error occurs, and Iterator if the output is an iterator object.

Important: Python's built-in function map, filter, and zip return iterators, not lists.

Use Ok to test your knowledge with the following "What Would Python Display?" questions:

    python3 ok -q iterators-wwpd -u

```python
>>> s = [1, 2, 3, 4]
>>> t = iter(s)
>>> next(s)
Error
>>> next(t)
1
>>> next(t)
2
>>> next(iter(s))
1
>>> next(iter(s))
1
>>> u = t
>>> next(u)
3
>>> next(t)
4


>>> r = range(6)
>>> r_iter = iter(r)
>>> next(r_iter)
0

>>> [x + 1 for x in r]
[1, 2, 3, 4, 5, 6]

>>> [x + 1 for x in r_iter]
[2, 3, 4, 5, 6]

>>> next(r_iter)
StopIteration


>>> map_iter = map(lambda x : x + 10, range(5))
>>> next(map_iter)
10

>>> next(map_iter)
11

>>> list(map_iter) # list() 函数的设计目的，就是“榨干”一个可迭代对象，把它现在能吐出来的东西全部装进一个列表。
[12, 13, 14]

>>> for e in filter(lambda x : x % 4 == 0, range(1000, 1008)):
...     print(e)
1000
1004

>>> [x + y for x, y in zip([1, 2, 3], [4, 5, 6])]
[5, 7, 9]
```

## Q5: Count Occurrences

简单的遍历，判断是否相等。满足条件计数加一。

Implement count_occurrences, which takes an iterator t, an integer n, and a value x. It returns the number of elements in the first n elements of t that are equal to x.

You can assume that t has at least n elements.

    Important: You should call next on t exactly n times. If you need to iterate through more than n elements, think about how you can optimize your solution.

# Generators

We can create our own custom iterators by writing a generator function, which returns a special type of iterator called a generator. Generator functions have yield statements within the body of the function instead of return statements. Calling a generator function will return a generator object and will not execute the body of the function.

For example, let's consider the following generator function:
```python
def countdown(n):
    print("Beginning countdown!")
    while n >= 0:
        yield n
        n -= 1
    print("Blastoff!")
```
Calling countdown(k) will return a generator object that counts down from k to 0. Since generators are iterators, we can call iter on the resulting object, which will simply return the same object. Note that the body is not executed at this point; nothing is printed and no numbers are outputted.

    >>> c = countdown(5)
    >>> c
    <generator object countdown ...>
    >>> c is iter(c)
    True

So how is the counting done? Again, since generators are iterators, we call next on them to get the next element! The first time next is called, execution begins at the first line of the function body and continues until the yield statement is reached. The result of evaluating the expression in the yield statement is returned. The following interactive session continues from the one above.

    >>> next(c)
    Beginning countdown!
    5

Unlike functions we've seen before in this course, generator functions can remember their state. On any consecutive calls to next, execution picks up from the line after the yield statement that was previously executed. Like the first call to next, execution will continue until the next yield statement is reached. Note that because of this, Beginning countdown! doesn't get printed again.

    >>> next(c)
    4
    >>> next(c)
    3

The next 3 calls to next will continue to yield consecutive descending integers until 0. On the following call, a StopIteration error will be raised because there are no more values to yield (i.e. the end of the function body was reached before hitting a yield statement).

    >>> next(c)
    2
    >>> next(c)
    1
    >>> next(c)
    0
    >>> next(c)
    Blastoff!
    StopIteration

Separate calls to countdown will create distinct generator objects with their own state. Usually, generators shouldn't restart. If you'd like to reset the sequence, create another generator object by calling the generator function again.

    >>> c1, c2 = countdown(5), countdown(5)
    >>> c1 is c2
    False
    >>> next(c1)
    5
    >>> next(c2)
    5

Here is a summary of the above:

    A generator function has a yield statement and returns a generator object.
    
    Calling the iter function on a generator object returns the same object without modifying its current state.
    
    The body of a generator function is not evaluated until next is called on a resulting generator object. Calling the next function on a generator object computes and returns the next object in its sequence. If the sequence is exhausted, StopIteration is raised.
    
    A generator "remembers" its state for the next next call. Therefore,
        
        the first next call works like this:
            1.Enter the function and run until the line with yield.
            2.Return the value in the yield statement, but remember the state of the function for future next calls.
        And subsequent next calls work like this:
            1.Re-enter the function, start at the line after the yield statement that was previously executed, and run until the next yield statement.
            2.Return the value in the yield statement, but remember the state of the function for future next calls.
    
    Calling a generator function returns a brand new generator object (like calling iter on an iterable object).
    
    A generator should not restart unless it's defined that way. To start over from the first element in a generator, just call the generator function again to create a new generator.

Another useful tool for generators is the yield from statement. yield from will yield all values from an iterator or iterable.

    >>> def gen_list(lst):
    ...     yield from lst
    ...
    >>> g = gen_list([1, 2, 3, 4])
    >>> next(g)
    1
    >>> next(g)
    2
    >>> next(g)
    3
    >>> next(g)
    4
    >>> next(g)
    StopIteration

## Q6:

全排列生成器:要求循环/递归+生成器函数
因为只有一个函数且不能实现知道参入参数的长度，所以不能写循环来应对不同深度的情况 ——> 递归。
    递归函数的作用，题目已经要求的很清楚了：生成给定参数所有元素的全排列列表。
    ——>递推关系：序列s的全排列等于每个元素单独作为起点+剩下的元素形成的新序列的排列。每个元素作为起点则需要用到一层循环;起点与剩下元素的全排列组合，要用到一层循环；提取剩余元素组成序列，需要用到列表推导。
    ——>基准条件：不断递归调用，序列长度越来越小。当长度等于1时，全排列为元素本身。

Given a sequence of unique elements, a permutation of the sequence is a list containing the elements of the sequence in some arbitrary order. For example, [1, 2, 3], [2, 1, 3], [1, 3, 2], and [3, 2, 1] are some of the permutations of the sequence [1, 2, 3].

Implement perms, a generator function that takes in a sequence seq and returns a generator that yields all permutations of seq. For this question, assume that seq will not be empty.

Permutations may be yielded in any order.

Hint: Remember, it's possible to loop over generator objects because generators are iterators!

## Q7: Repeated (Optional)

思路其实跟看成一个列表相类似。

只是：
    因为，iterator会耗尽，所以需要一个变量存储当前值，跟迭代器中的值相比对。
    因为，迭代器会产生StopIteration，所以在耗尽前且满足条件时要及时结束并返回值。这需要一个变量记录连续相等的数目，一个判断语句来打破、return。