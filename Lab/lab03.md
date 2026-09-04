# Lab3: Sequences, Recursion

## Topics:

### Lists and List Comprehension

A list is a data structure that can hold an ordered collection of items. 
These items, known as elements, can be of any data type, including numbers, strings, or even other lists. 

A list comprehension describes the elements in a list and evaluates to a new list containing those elements.

There are two forms:

    [<expression> for <element> in <sequence>]
    [<expression> for <element> in <sequence> if <conditional>]

### For Loops

A for statement executes code for each element of a sequence, such as a list or range. 
Each time the code is executed, the name right after for is bound to a different element of the sequence.

    for <name> in <expression>:
    <suite>

First, expression is evaluated. It must evaluate to a sequence. Then, for each element in the sequence in order,

    name is bound to the element.
    suite is executed.

### Ranges

A range is a data structure that holds integer sequences. 
While ranges and lists are both sequences, a range object is different from a list. 
A range can be converted to a list by calling list()

A range can be created by:

    range(stop) contains 0, 1, ..., stop - 1
    range(start, stop) contains start, start + 1, ..., stop - 1

## Q1: WWPD: Lists & Ranges

Predict what Python will display when you type the following into the interactive interpreter.
```Python
>>> s = [7//3, 5, [4, 0, 1], 2]
>>> s[0]
2

>>> s[2]
[4, 0, 1]

>>> s[-1]
2

>>> len(s)
4

>>> 4 in s
False

>>> 4 in s[2]
True

>>> s[2] + [3 + 2]
[4, 0, 1, 5]

>>> 5 in s[2]
False

>>> s[2] * 2
[4, 0, 1, 4, 0, 1]

>>> list(range(3, 6))
[3, 4, 5]

>>> range(3, 6)
range(3, 6)

>>> r = range(3, 6)
>>> [r[0], r[2]]
[3, 5]

>>> range(4)[-1]
3
```

## Q2: Flatten

Write a function flatten that takes in a list s and returns a new list that is the "flattened" version of s.
You should not modify the original list. And you can check if something is a list by using the built-in type function. 
函数的作用是去掉列表之间的嵌套，“拉平”列表。遍历深度要足够深，否则加入的元素可能是仍旧是列表，比如[2],而不是2。
如果使用循环，如何确定深度？需要几层循环呢？
嵌套列表这一数据结构具有递归的特性
*递归*

“递归函数里，return 要么在递归调用处直接返回（如求阶乘），要么在循环结束后返回（如遍历累加）。”

## Q3: WWPD: List Comprehensions

```python
>>> [2 * x for x in range(4)]
[0, 2, 4, 6]

>>> [y for y in [6, 1, 6, 1] if y > 2]
[6, 6]

>>> [[1] + s for s in [[4], [5, 6]]]
[ [1, 4], [1, 5, 6] ]

>>> [z + 1 for z in range(10) if z % 3 == 0]
[1, 4, 7, 10]
```

## Q4: Close List
补全函数close_list()的代码，该函数返回一个列表，列表中的元素满足—— |s[index] - index| < k

## Q5: Sorting a List (recursion)
补全函数remove_first() sort()
递归函数的基准条件和递归调用

## Q6: Making Onions

补全函数make_onion()，make_onion()是一个高阶函数——接收两个单参数函数，函数返回一个函数。
被返回的内层函数，有三个参数（x, y, limit），x是初始值，y是目标值，limit是调用f、g的次数上限。如果能达到目标值则返回True，否则返回False。

十分简单，代码框架已经给出了，只是填空。

## Q7： Function Repeater(optional)

Define a function make_fn_repeater which takes in a one-argument function f and an integer x. 
It should return another function which takes in one argument, another integer. 
This function returns the result of applying f to x this number of times.

代码填空

## Q8: Ten-Pairs(optional)

Write a function that takes a positive integer n and returns the number of ten-pairs it contains.
A ten-pair is a pair of digits within n that sums to 10.

count_digit()函数使用递归的思路：该函数计算参数digit这一数字在n中出现的次数。
递归函数具有基准条件和递归调用两大核心，目标是把大问题拆分成更小一点问题的。 
涉及到位数一般都要用到 // 及 % 运算。这两种运算刚好可以吧问题逐步化小：整除去掉最后一位，取模提取最后一位。

ten_pairs()函数的目标是找出n中有多少对和为10的整数对。
辅助函数count_digit能够计算数字digit的出现次数，那么对于数n中的 数字digit，找出能与其配对的数字，实际上是在剩余数字中计算 *数字 10-digit出现的次数*。
因为要求必须使用递归，所以要找出如何把问题规模变小，或者说是**大问题的答案与化小的问题的答案之间的函数关系**。
可以先举例观察递归关系。当 n= 4523346时，ten_pairs的数量为*第一位数 4 的对应数字 6 在 523346中出现的次数*与*523346 中的ten_pairs数量之和*。
从例子中，可以很容易看出所需要的关系式： ten_pairs(n) = count_digit(n//10, 10-(n%10)) + ten_pairs(n//10)
最后则是判断基准条件（最小规模的问题，其结果显然），观察n逐渐缩短的过程，当n为两位数时，仍旧可以使用公式。n为一位数，整数对结果显然为0。