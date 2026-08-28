# What Would Python Display?

Important: For all WWPD questions, type Function if you believe the answer is <function...>, Error if it errors, and Nothing if nothing is displayed.

## Q1 WWPD: The Truth Will Prevail

### Principles (of Short Circuiting): 

*不知道就 “Python3 -i” terminal命令， 一个个的输入*

and: evalutes from left to right up to: The first false value.
or: evalutes from left to right up to: The first true value.

Short-circuiting happens when the operator reaches an operand that allows them to make a conclusion about the expression. For example, and will short-circuit as soon as it reaches the first false value because it then knows that not all the values are true.

If and and or do not short-circuit, they just return the last value; another way to remember this is that and and or always return the last thing they evaluate, whether they short circuit or not. Keep in mind that and and or don't always return booleans when using values other than True and False.

### Answer of Q1

True and 13
13

False or 0
0

not 10
False

not None
True

True and 1 / 0
Error

True or 1 / 0
True

-1 and 1 > 0
True

-1 or 5
-1

(1 + 1) and 1
1

print(3) or ""
(line1)? 3
(line2)? ""

```python
'''
>>>0 or f(1)
"positive"
>>>f(0) or f(-1)
"zero"
>>>f(0) and f(-1)
""
'''
def f(x):
    if x == 0:
        return "zero"
     elif x > 0:
         return "positive"
     else:
         return ""
```
## Q2 WWPD: Higher-Order Functions

```python
def cake():
    print('beets')
    def pie():
        print('sweets')
        return 'cake'
    return pie
'''
>>> chocolate = cake()
beets
>>> chocolate
Function
>>> chocolate()
(line1) sweets
(line2) 'cake'
>>> more_chocolate, more_cake = chocolate(), cake
sweets
>>> more_chocolate
'cake'
'''

def snake(x, y):
    if cake == more_cake:
        return chocolate
    else:
        return x + y
'''
>>> snake(10, 20)
Function
>>> snake(10, 20)()
sweets
'cake'
>>> cake = 'cake'
>>> snake(10, 20)
30
'''
```

## Q3: WWPD: Lambda

Q: Which of the following statements describes a difference between a def statement and a lambda expression?
Choose the number of the correct choice:
0) A def statement can only have one line in its body.
1) A lambda expression cannot have more than two parameters.
2) A lambda expression does not automatically bind the function that it returns to a name.
3) A lambda expression cannot return another function.
? 2

Q: How many formal parameters does the following lambda expression have?
lambda a, b: c + d
Choose the number of the correct choice:
0) two
1) one
2) Not enough information
3) three
? 0

Q: When is the return expression of a lambda expression executed?
Choose the number of the correct choice:
0) When you pass the lambda expression into another function.
1) When the lambda expression is evaluated.
2) When you assign the lambda expression to a name.
3) When the function returned by the lambda expression is called.
? 3


lambda x: x  # A lambda expression with one parameter x
Function

a = lambda x: x  # Assigning the lambda function to the name a
a(5)
5

(lambda: 3)()  # Using a lambda expression as an operator in a call expression.
3

b = lambda x, y: lambda: x + y  # Lambdas can return other lambdas!
c = b(8, 4)
c
Function

c()
12

d = lambda f: f(4)  # They can have functions as arguments as well.
def square(x):
    return x * x
d(square)
16

higher_order_lambda = lambda f: lambda x: f(x)
g = lambda x: x * x
higher_order_lambda(2)(g)  # Which argument belongs to which function call?
Error

higher_order_lambda(g)(2)
4

call_thrice = lambda f: lambda x: f(f(f(x)))
call_thrice(lambda y: y + 1)(0)
3

print_lambda = lambda z: print(z)  # When is the return expression of a lambda expression executed?
print_lambda
Function

one_thousand = print_lambda(1000)
1000

one_thousand # What did the call to print_lambda return?
Nothing

## Q5: Count Cond

从count_fives()和count_primes两个函数中抽象出一个高阶函数,见lab02.md文件
直接观察两个函数的代码，发现出来了if语句的条件的条件判断不同，其余都相同。所以，条件判断是调用传入的函数参数的地方。
这个过程和电子书1.6节思路一致。
```python
def count_fives(n):
    """Return the number of values i from 1 to n (including n)
    where sum_digits(n * i) is 5.

    >>> count_fives(10)  # Among 10, 20, 30, ..., 100, only 50 (10 * 5) has digit sum 5
    1
    >>> count_fives(50)  # 50 (50 * 1), 500 (50 * 10), 1400 (50 * 28), 2300 (50 * 46)
    4
    """
    i = 1
    count = 0
    while i <= n:
        if sum_digits(n * i) == 5:
            count += 1
        i += 1
    return count

def count_primes(n):
    """Return the number of prime numbers up to and including n.

    >>> count_primes(6)   # 2, 3, 5
    3
    >>> count_primes(13)  # 2, 3, 5, 7, 11, 13
    6
    """
    i = 1
    count = 0
    while i <= n:
        if is_prime(i):
            count += 1
        i += 1
    return count
```

## Q6: String Transformer/ 凯撒密码函数

Using a lambda expression, complete the caesar_generator() function. Your function should only contain a return statement.

拿到num -> op(letter_to_num(ch), num) -> num_to_letter(op)。所以，lambda表达式将字母转换为数字，并应用op(),返回一个字符
lambda ch: num_to_letter( op(letter_to_num(ch), num) )
```python
# caesar_generator(num, op)这一高阶函数内部定义的函数，等价于lambda表达式。
def func(character):
    num_caesar_generator = op(letter_to_num(character), num)
    return num_to_letter(num_caesar_generator)
```

## Q7: Palindrome/回文 (optional)

A number is considered a palindrome if it reads the same forwards and backwards. Fill in the blanks '_' of is_palindrome() function to help determine if a number is a palindrome.

代码思路：
return 返回的是“y==n”的真假，而函数的作用是判断数字是否回文。这就是说y就是倒序后的数字n。
关于数字倒序、提取每位上的数字，一般会用到 //（整除）和 %（取模）运算。
循环条件为x > 0,说明x一直在进行整除运算，去掉末尾的数字，即x：从原数 n 开始，每次砍掉最后一位（x // 10）。

y = f(), f()中没有参数，所以lambda表达式也没有参数要求，只有return。
y记录的是x一个个末尾被去掉的数字。十进制下，本次循环的y 等于 上一个y乘10 加上 本次x的末尾数。
因此，从 0 开始，每次把 x 砍下的末位数字拼接到 y 的末尾（y * 10 + 末位数字）。