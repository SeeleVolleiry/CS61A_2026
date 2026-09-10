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
______

>>> next(t)
______

>>> next(t)
______

>>> next(iter(s))
______

>>> next(iter(s))
______

>>> u = t
>>> next(u)
______

>>> next(t)
______
>>> r = range(6)
>>> r_iter = iter(r)
>>> next(r_iter)
______

>>> [x + 1 for x in r]
______

>>> [x + 1 for x in r_iter]
______

>>> next(r_iter)
______
>>> map_iter = map(lambda x : x + 10, range(5))
>>> next(map_iter)
______

>>> next(map_iter)
______

>>> list(map_iter)
______

>>> for e in filter(lambda x : x % 4 == 0, range(1000, 1008)):
...     print(e)
______

>>> [x + y for x, y in zip([1, 2, 3], [4, 5, 6])]
______
```

## Q5:


# Generators

## Q6:


## Q7:(Optional)