# Scheme Interpreter

# Phase 1: The Evaluator

*python3 ok -q eval_apply -u*解锁问题
```python
---------------------------------------------------------------------
Q: What types of expressions are represented as Links?
Choose the number of the correct choice:
0) Only special forms
1) Only call expressions
2) All expressions are represented as Links
3) Call expressions and special forms
? 3
-- OK! --
---------------------------------------------------------------------
Q: What expression in the body of scheme_eval finds the value of a name?
Choose the number of the correct choice:
0) env.lookup(expr)
1) scheme_symbolp(expr)
2) env.find(name)
3) scheme_forms.SPECIAL_FORMS[first](rest, env)
? 0
-- OK! --
---------------------------------------------------------------------
Q: How do we know if a given combination is a special form?
Choose the number of the correct choice:
0) Check if the first element in the list is a symbol
1) Check if the first element in the list is a symbol and that the
   symbol is in the dictionary SPECIAL_FORMS
2) Check if the expression is in the dictionary SPECIAL_FORMS
? 1
-- OK! --
---------------------------------------------------------------------
Q: What is the difference between applying builtins and applying user-defined procedures?
(Choose all that apply)

I.   User-defined procedures open a new frame; builtins do not
II.  Builtins simply execute a predefined Python function; user-defined
     procedures must evaluate additional expressions in the body
III. Builtins have a fixed number of arguments; user-defined procedures do not
---
Choose the number of the correct choice:
0) II only
1) I only
2) I and II
3) III only
4) I, II and III
5) I and III
6) II and III
? 2
-- OK! --
---------------------------------------------------------------------
Q: What exception should be raised for the expression (1)?
Choose the number of the correct choice:
0) SchemeError("unknown identifier: 1")
1) SchemeError("malformed list: (1)")
2) SchemeError("1 is not callable")
3) AssertionError
? 2
-- OK! --
```

## Problem 1: define and lookup methods in Frame class

`Implement the define and lookup methods of the Frame class in scheme_classes.py.`

Each Frame object has the following instance attributes:

    bindings is a dictionary representing the bindings in the frame instance. Each item associates a Scheme symbol (represented as a Python string) to a Scheme value.
    
    parent is the parent Frame instance (parent environment frame). The parent of the Global Frame is None.

To complete these methods:

    define takes a symbol (represented by a Python string) and a value. It binds the symbol to the value in the Frame instance using bindings.

    lookup takes a symbol and returns the value bound to that symbol in the first frame of the environment where it is found. The environment for a Frame instance consists of that frame, its parent frame, and all its ancestor frames, including the Global Frame. When looking up a symbol:

        If the symbol is bound in the current frame, return its value.
        If the symbol is not bound in the current frame and the frame has a parent frame, continue looking up the symbol in the parent frame.
        Keep checking all parent frames until either the symbol is found or there are no more parent frames.
        If the symbol is never found in any frame, raise a SchemeError.

*python3 ok -q 01 -u*
```python
---------------------------------------------------------------------
>>> from scheme import *
>>> global_frame = create_global_frame()
>>> global_frame.define("x", 3)
>>> global_frame.parent is None
? True
-- OK! --

>>> global_frame.lookup("x")
? 3
-- OK! --

>>> global_frame.define("x", 2)
>>> global_frame.lookup("x")
? 2
-- OK! --

>>> global_frame.lookup("foo")
Choose the number of the correct choice:
0) None
1) SchemeError
2) 3
? 1
-- OK! --
---------------------------------------------------------------------
>>> from scheme import *
>>> first_frame = create_global_frame()
>>> first_frame.define("x", 3)
>>> second_frame = Frame(first_frame)
>>> second_frame.parent == first_frame
? True
-- OK! --

>>> second_frame.define("y", False)
>>> second_frame.lookup("x")
? 3
-- OK! --

>>> second_frame.lookup("y")
? False
-- OK! --
```

解题思路：十分简单，按照解锁问题和problem 1描述的方法逻辑来写即可。

## Problem 2：

To be able to call built-in procedures, such as +, you need to complete the BuiltinProcedure case within the scheme_apply function in scheme_eval_apply.py. Built-in procedures are applied by calling a corresponding Python function that implements the procedure.

A BuiltinProcedure has two instance attributes:

    py_func: the Python function that implements the built-in Scheme procedure.

scheme_apply takes the procedure object, a linked list of argument values args, and the current environment env. The args argument is a Scheme list, represented as a Link object or nil, containing the values passed to the procedure. For example, if the Scheme built-in procedure we are trying to use is + and we pass in args as Link(1, Link(2, nil)) to scheme_apply, we would be making the call (+ 1 2).

**Your implementation should do the following**:

    Convert the Scheme list to a Python list of arguments. Hint: args is a Link, which has .first and .rest attributes.
    
    If procedure.need_env is True, then add the current environment env to the end of this list.
    
    Return the result of calling procedure.py_func on all of those arguments. Since you don't know the exact number of arguments, use *args notation: f(1, 2, 3) is equivalent to f(*[1, 2, 3]). Do this part within the try statement provided, after the line that says try:.

解题思路：在上面的斜线后面已经描述的十分清晰了。总共分为三步：

    首先将Scheme list(Link类)转换为Python的list/列表[...,]。用一个循环逐个添加即可搞定。
    其次是根据need_env属性的值，判断是否要将env加到列表的末尾
    最后则是给py_func函数传入Python列表作为参数。这里要利用到 *号加列表这一可变参数等于传入该列表内的所有元素作为参数。

*python3 ok -q 02 -u*
```python
---------------------------------------------------------------------
>>> from scheme import *
>>> env = create_global_frame()
>>> twos = Link(2, Link(2, nil))
>>> plus = BuiltinProcedure(scheme_add) # + procedure
>>> scheme_apply(plus, twos, env) # Type SchemeError if you think this errors
? 4
-- OK! --
---------------------------------------------------------------------
>>> from scheme import *
>>> env = create_global_frame()
>>> plus = BuiltinProcedure(scheme_add) # + procedure
>>> scheme_apply(plus, nil, env) # Remember what (+) evaluates to in scheme
? 0
-- OK! --
---------------------------------------------------------------------
>>> from scheme import *
>>> env = create_global_frame()
>>> twos = Link(2, Link(2, nil))
>>> oddp = BuiltinProcedure(scheme_oddp) # odd? procedure
>>> scheme_apply(oddp, twos, env) # Type SchemeError if you think this errors
? SchemeError
-- OK! --
---------------------------------------------------------------------
>>> from scheme import *
>>> env = create_global_frame()
>>> one = Link(1, nil)
>>> def test_func(arg, env):
...     return arg + (1 if env else 0)
>>> test_procedure = BuiltinProcedure(test_func, True)
>>> scheme_apply(test_procedure, one, env)
? 2
-- OK! --
```

## Problem 3：补全scheme_eval

解题思路：REPl -> Scheme_eval和scheme_apply互相调用。

    first和rest已经写好，但不是上面两个函数可以直接使用的参数形式。例如，第一个参数是四则运算符号的字符表达。这就要计算first和rest的值，也就是使用scheme_eval()。值得注意的是，rest是序列，要对其中每个元素都应用scheme_eval。这就是题目中提到的第一、第二步。
    计算出operator和operands后，就可以将它们和env传入scheme_apply函数，计算出结果，最后return。

Implement the missing part of scheme_eval, which evaluates a call expression. To evaluate a call expression:

    Evaluate the operator (which should evaluate to a Procedure instance – see scheme_classes.py for Procedure definitions).
    Evaluate all of the operands and collect the results (the argument values) in a Scheme list.
    Return the result of calling scheme_apply on this Procedure, these argument values, and the current environment.

You'll have to `recursively call scheme_eval` in the first two steps. Here are some other functions/methods you should use:

    The map_link function returns a new Scheme list constructed by applying a one-argument Python function to every item in a Scheme list.
    The scheme_apply function applies a Scheme procedure to arguments represented as a Scheme list (a Link instance or nil).

*python3 ok -q 03 -u*
```python
>>> from scheme_reader import *
>>> from scheme import *
>>> expr = read_line('(+ 2 2)')
>>> scheme_eval(expr, create_global_frame()) # Type SchemeError if you think this errors
? 4
-- OK! --

>>> scheme_eval(Link('+', Link(2, Link(2, nil))), create_global_frame()) # Type SchemeError if you think this errors
? 4
-- OK! --

>>> expr = read_line('(+ (+ 2 2) (+ 1 3) (* 1 4))')
>>> scheme_eval(expr, create_global_frame()) # Type SchemeError if you think this errors
? 12
-- OK! --

>>> expr = read_line('(yolo)')
>>> scheme_eval(expr, create_global_frame()) # Type SchemeError if you think this errors
? SchemeError
-- OK! --
---------------------------------------------------------------------
scm> (* (+ 3 2) (+ 1 7)) ; Type SchemeError if you think this errors
? 40
-- OK! --

scm> (1 2) ; Type SchemeError if you think this errors
? SchemeError
-- OK! --
```

## Problem 4：the first part of do_define_form

Notice that the type of the first operand can tell us what is being defined:

    If it is a symbol, e.g. a, then the expression is defining a symbol.
    If it is a Scheme list, e.g. (foo x), then the expression is creating a procedure.

The `do_define_form` function in `scheme_forms.py` evaluates (define ...) expressions. There are two missing parts in this function; one for when the first operand is a symbol, and the other for when it is a Scheme list (i.e. Link).

*For this problem, implement just the first part*, which evaluates the second operand to obtain a value and binds the first operand, a symbol, to that value. Then, do_define_form returns the symbol that was bound.

Hint: The define method of a Frame instance creates a binding in that frame.

*python3 ok -q 04 -u*
```python
---------------------------------------------------------------------
Q: What is the structure of the expressions argument to do_define_form?
Choose the number of the correct choice:
0) Link('define', Link(A, Link(B, nil))), where:
       A is the symbol being bound,
       B is an expression whose value should be evaluated and bound to A
1) Link(A, B), where:
       A is the symbol being bound,
       B is an expression whose value should be evaluated and bound to A
2) Link(A, Link(B, nil)), where:
       A is the symbol being bound,
       B is the value that should be bound to A
3) Link(A, B), where:
       A is the symbol being bound,
       B is the value that should be bound to A
4) Link(A, Link(B, nil)), where:
       A is the symbol being bound,
       B is an expression whose value should be evaluated and bound to A
? 4
-- OK! --
---------------------------------------------------------------------
Q: What method of a Frame instance will bind
a value to a symbol in that frame?
Choose the number of the correct choice:
0) define
1) bindings
2) lookup
3) make_child_frame
? 0
-- OK! --
---------------------------------------------------------------------
scm> (define size 2)
? size
-- OK! --

scm> size
? 2
-- OK! --

scm> (define x (+ 7 3))
? x
-- OK! --

scm> x
? 10
-- OK! --
```

解题思路：Problem 4要求先完成函数的第一部分，也就是在对应的frame中实现绑定expression和symbol。
    
    在frame中创建绑定要使用到Frame类的define方法。
    (define x 2)的返回值是 x？所以，可以看出返回值就是symbol。
    根据测试用例 10 而不是(+ 7 3)，这表明expression要计算出最终值。

## Problem 5：do_quote_form

题目要求：在`scheme_forms.py` 里实现`do_quote_form` ，让`(quote ...)` 表达式把操作数不求值地返回。

*python3 ok -q 05 -u*
```python
--------------------------------------------------------------------
Q: What is the structure of the expressions argument to do_quote_form?
Choose the number of the correct choice:
0) [A], where:
       A is the quoted expression
1) Link(A, nil), where:
       A is the quoted expression
2) A, where:
       A is the quoted expression
3) Link('quote', Link(A, nil)), where:
       A is the quoted expression
? 1
-- OK! --
---------------------------------------------------------------------
>>> from scheme import *
>>> global_frame = create_global_frame()
>>> do_quote_form(Link(3, nil), global_frame)
? 3
-- OK! --

>>> do_quote_form(Link('hi', nil), global_frame)
? 'hi'           
-- OK! --

>>> expr = Link(Link('+', Link('x', Link(2))))
>>> do_quote_form(expr, global_frame) # Make sure to use Link notation
? Link('+', Link('x', Link(2)))      
-- OK! --
```

解题思路：

    通过解锁问题，我们知道： expressions的形式是Link(A, nil)。其中，A就是最后的结果，是 quoted expression。
    题目要求返回Link类，A本来就是Link类。我们直接返回A，也即expressions.first就行了。

# Phase 2: Procedures

In Phase 2, you will add the ability to `create and call user-defined procedures`. You will add the following features to the interpreter:

    Lambda procedures, using the (lambda ...) special form
    Named procedures, using the (define (...) ...) special form
    Dynamically scoped mu procedures, using the (mu ...) special form.

## Problem 6：begin special form

Change the eval_all function in scheme_eval_apply.py (which is called from do_begin_form in scheme_forms.py) to *complete the implementation of the begin special form* (spec).

A begin expression is evaluated by evaluating all sub-expressions in order. The value of the begin expression is the value of the final sub-expression.

To complete the implementation of begin, eval_all will take in expressions (a Scheme list of expressions) and env (a Frame representing the current environment), evaluate all the expressions in expressions, and return the value of the last expression in expressions.

*python3 ok -q 06 -u*
```python
---------------------------------------------------------------------
>>> from scheme import *
>>> env = create_global_frame()
>>> eval_all(Link(2, nil), env)
Choose the number of the correct choice:
0) 2
1) SchemeError
? 0
-- OK! --

>>> eval_all(Link(4, Link(5, nil)), env)
Choose the number of the correct choice:
0) SchemeError
1) 5
2) 4
3) (4 5)
? 1
-- OK! --

>>> eval_all(nil, env) # return None (meaning undefined)
---------------------------------------------------------------------
scm> (begin (+ 2 3) (+ 5 6))
? 11
-- OK! --

scm> (begin (define x 3) x)
? 3
-- OK! --
---------------------------------------------------------------------
scm> (begin 30 '(+ 2 2))
Choose the number of the correct choice:
0) 4
1) 30
2) (+ 2 2)
3) '(+ 2 2)
? 2
-- OK! --

scm> (define x 0)
? x
-- OK! --

scm> (begin (define x (+ x 1)) 42 (define y (+ x 1)))
? y
-- OK! --

scm> x
? 1
-- OK! --

scm> y
? 2
-- OK! --
```

解题思路：
    
    题目已经将函数的功能和返回值描述地清晰明确。对每个子表达式求值，返回最后一个表达式的值。
    很容易想到的是，遍历scheme list，对每一个表达式使用schem_eval函数。
    此外，用一个变量记录最新表达式的计算结果，当循环结束后，它就是最后一个计算值，也是函数的返回值。

## User-Defined Procedures

User-defined lambda procedures are represented as `instances of the LambdaProcedure class`. A LambdaProcedure instance has three instance attributes:

    formals: a Scheme list containing the formal parameter names for the arguments of the lambda procedure.
    body: a nested Scheme list of expressions representing the body of the procedure.
    env: the environment in which the procedure was defined.

For example, in (lambda (x y) (+ x y)), formals is Link('x', Link('y', nil)). body is Link(Link('+', Link('x', Link('y', nil))), nil), which is a nested Scheme list where the first element (body.first) is the expression (+ x y) represented as Link('+', Link('x', Link('y', nil))).
body is nested to allow for complex expressions and nested function calls.

## Problem 7：do_lambda_form

Implement the do_lambda_form function (spec) in scheme_forms.py, which creates and returns a LambdaProcedure instance.

In Scheme, the body of a procedure can contain multiple expressions, but must include at least one. The body attribute of a LambdaProcedure instance is a nested Scheme list of these expressions, and the formals attribute is a Link. Like a begin special form, evaluating the body of a procedure executes all expressions in order. A procedure returns the value of its last body expression.

*python3 ok -q 07 -u*
```python
---------------------------------------------------------------------
scm> (lambda (x y) (+ x y)) ; A lambda procedure is displayed exactly as it iswritten
? lambda (x y) (+ x y)
-- Not quite. Try again! --

? (lambda (x y) (+ x y))  
-- OK! --

scm> (lambda (x)) ; type SchemeError if you think this causes an error
? SchemeError
-- OK! --
---------------------------------------------------------------------
>>> from scheme_reader import *
>>> from scheme import *
>>> env = create_global_frame()
>>> lambda_line = read_line("(lambda (a b c) (+ a b c))")
>>> lambda_proc = do_lambda_form(lambda_line.rest, env)
>>> lambda_proc.formals # use single quotes ' around strings in your answer
Choose the number of the correct choice:
0) Link('a', Link('b', Link('c')))
1) Link('+', Link('a', Link('b', Link('c'))))
2) Link(Link('a', Link('b', Link('c'))))
? 0
-- OK! --

>>> lambda_proc.body # the body is a *Scheme list* of expressions! Make sure your answer is a properly nested Link.
Choose the number of the correct choice:
0) Link('+', Link('a', Link('b', Link('c'))))
1) Link('a', Link('b', Link('c')))
2) Link('+', 'a', 'b', 'c')
3) Link(Link('+', Link('a', Link('b', Link('c')))))
? 3
-- OK! --
```

## Problem 8：make_child_frame

`Implement the make_child_frame method of the Frame class (in scheme_classes.py)`, which will be used to create new frames when calling user-defined procedures.
This method takes in two arguments: formals, which is a Scheme list of symbols (ex: Link('x', Link('y', nil))), and vals, which is a Scheme list of values (ex: Link(3, Link(5, nil))). It should return a new child frame with the formal parameters bound to the values.

To do this:

    If the number of argument values does not match with the number of formal parameters, raise a SchemeError.
    Create a new Frame instance that is the child of this frame (called self).
    Bind each formal parameter to its corresponding value in the newly created frame. The first symbol in formals should be bound to the first value in vals, and so on. Remember that formals and vals are Links.
    Return the new frame.

Hint: The define method of a Frame instance creates a binding in that frame.

*python3 ok -q 08 -u*
```python
---------------------------------------------------------------------
>>> from scheme import *
>>> global_frame = create_global_frame()
>>> formals = Link('a', Link('b', Link('c', nil)))
>>> vals = Link(1, Link(2, Link(3, nil)))
>>> frame = global_frame.make_child_frame(formals, vals)
>>> global_frame.lookup('a') # Type SchemeError if you think this errors
? SchemeError
-- OK! --

>>> frame.lookup('a')        # Type SchemeError if you think this errors
? 1
-- OK! --

>>> frame.lookup('b')        # Type SchemeError if you think this errors
? 2
-- OK! --

>>> frame.lookup('c')        # Type SchemeError if you think this errors
? 3
-- OK! --
---------------------------------------------------------------------
>>> from scheme import *
>>> global_frame = create_global_frame()
>>> frame = global_frame.make_child_frame(nil, nil)
>>> frame.parent is global_frame
? True
-- OK! --
```

解题思路：

    显而易见，len_link能求出长度，这也就是for循环的次数。
    利用两个变量，来追踪需要的Link
    每次循环利用提示的define方法，将两个Link中的first绑定到子帧中。
    追踪变量更新为其rest。

## Problem 9：

`Implement the LambdaProcedure case in the scheme_apply function in scheme_eval_apply.py`

This elif block is executed when the procedure being applied is a LambdaProcedure instance.

First create a new Frame instance and bind the procedure's formal parameters to the argument values by calling the make_child_frame method on the appropriate parent frame.

Then, within this new frame, evaluate each of the expressions of the body of the procedure using eval_all.

Hint: Your new frame should be a child of the frame in which the lambda was defined. The env provided as an argument to scheme_apply is instead the frame in which the procedure was called.

See User-Defined Procedures to remind yourself of the attributes of LambdaProcedure.

## Problem 10：do_define_form

We'd like to be able to use the shorthand form of defining named procedures, which is what we've been doing in homeworks and labs.

Modify the do_define_form function in scheme_forms.py so that it correctly handles define (...) ...) expressions (spec).

There are (at least) two ways to solve this problem. One is to construct an expression (define _ (lambda ...)) and call do_define_form on it (omitting the define). The second is to implement it directly:

    Using the given variables signature and expressions, find the defined function's name (symbol), formals, and body.

    Create a LambdaProcedure instance using the formals and body. (You could call do_lambda_form to do this.)
    
    Bind the symbol to this new LambdaProcedure instance.
    
    Return the symbol that was bound.

Doctest Walkthrough: Consider the doctest do_define_form(read_line("((f x) (+ x 2))"), env). This is the Python call that will evaluate (define (f x) (+ x 2)) in Scheme. read_line is a utility function that takes in "((f x) (+ x 2))" and returns its Link representation. Therefore, that Link representation is passed into do_define_form as its expressions parameter.

Hint for Way 2: How can we utilize the Scheme list representation of ((f x) (+ x 2)) (the structure for (define (f x) (* x 2))) to have the same functionality as (define f (lambda (x) (+ x 2))), which we know our Scheme interpreter (and thus our Python code) can already handle? Try writing out the Scheme list representation yourself and consider what components you would need to extract from it in order to be able to replicate the functionality of (define f (lambda (x) (+ x 2))) in Python within do_define_form.

# Phase 3: MU and Logical Forms



## Problem 11：mu special form

The mu special form (spec; invented for this project) evaluates to a dynamically scoped procedure.

Your job:

    Implement do_mu_form in scheme_forms.py to evaluate the mu special form. A mu expression evaluates to a MuProcedure. The MuProcedure class (defined in scheme_classes.py) has been provided for you.

    In addition to implementing do_mu_form, complete the MuProcedure case within the scheme_apply function (in scheme_eval_apply.py) so that when a mu procedure is called, its body is evaluated in the correct environment. When a MuProcedure is called, the parent of the new call frame is the environment in which that call expression was evaluated. As a result, a MuProcedure does not need to store an environment as an instance attribute. Your code here should be VERY similar to what you did for question 9.

## Problem 12：do_and_form & do_or_form

In Scheme, only #f is a false value. All other values (including 0 and nil) are true values.
You can test whether a value is a true or false value using the provided Python functions is_scheme_true and is_scheme_false, defined in scheme_utils.py.

Implement do_and_form and do_or_form so that and and or expressions (spec) are evaluated correctly.

The logical forms and and or are short-circuiting. For and, your interpreter should evaluate each sub-expression from left to right, and if any of these is a false value, return that value. Otherwise, return the value of the last sub-expression. If there are no sub-expressions in an and expression, it evaluates to #t.

For or, evaluate each sub-expression from left to right. If any sub-expression evaluates to a true value, return that value. Otherwise, return the value of the last sub-expression. If there are no sub-expressions in an or expression, it evaluates to #f.

In your code here, you should represent Scheme's #t as Python's True and Scheme's #f as Python's False.
Important: Use the provided Python functions is_scheme_true and is_scheme_false from scheme_utils.py to test boolean values.

*python3 ok -q 12 -u*
```python
---------------------------------------------------------------------
scm> (and)
Choose the number of the correct choice:
0) SchemeError
1) #f
2) #t
? 2
-- OK! --

scm> (and 1 #f)
Choose the number of the correct choice:
0) #f
1) 1
2) #t
? 0
-- OK! --

scm> (and (+ 1 1) 1)
? 1
-- OK! --

scm> (and #f 5)
? #f
-- OK! --

scm> (and 4 5 (+ 3 3))
? 6
-- OK! --

scm> (not (and #t #f 42 (/ 1 0)))
? #t
-- OK! --
---------------------------------------------------------------------
scm> (or)
Choose the number of the correct choice:
0) SchemeError
1) #f
2) #t
? 1
-- OK! --

scm> (or (+ 1 1))
Choose the number of the correct choice:
0) #t
1) 2
2) #f
? 1
-- OK! --

scm> (not (or #f))
? #t
-- OK! --

scm> (define (zero) 0)
? zero
-- OK! --

scm> (or (zero) 3)
? 0
-- OK! --

scm> (or 4 #t (/ 1 0))
? 4
-- OK! --
```

解题思路：and和or这两种特殊形式的算法流程，已在题目中描述的十分清楚。我们只需用一个循环计算每个值，在触发短路原则时退出，没触发时返回既定值。

## Problem 13：do_cond_form

Fill in the missing parts of do_cond_form so that it correctly implements cond (spec), returning the value of the first result sub-expression corresponding to a true predicate, or the value of the result sub-expression corresponding to else.

解题思路：
    
    这道题是要我们补全指定位置缺失的代码。
    通过通读整个函数的代码和观察缺失部分的位置，可以发现缺失部分是有一个predict为真时才执行的代码。
    阅读题目给出的cond这一函数的行为，可以知道：当除了else以外的条件为真时，会执行语句并返回计算结果。如果语句没有可以执行的代码，就返回#t，也就是True。

# Phase 4: Write Some Scheme

`三个问题的代码都在填入questions.scm这一文件中`

If you want to use cond for Problems 13, 14, or 15, you must implement Problem EC1 for your tests to run.

## Problem 14：enumerate procedure

Implement the (enumerate s) procedure, which takes in a list of values s and returns a list of two-element lists, where the first element is the index of the value, and the second element is the value itself. Set the first index to 0.

```scheme
scm> (enumerate '(3 4 5 6))
((0 3) (1 4) (2 5) (3 6))
scm> (enumerate '(c s 6 1 a))
((0 c) (1 s) (2 6) (3 1) (4 a))
scm> (enumerate '())
()
```

解题思路：这是关于Scheme list的问题。涉及到列表，根据经验，我们首先可以考虑递归。

    通过样例，可以看出两个东西。一是基准条件，空列表返回空列表。二是出现了一个索引变量。
    这个索引值，不是传入的参数，而我们要实现enumerate就必须追踪被添加元素的位置/索引值。此时，考虑把enumerate作为高阶函数来写，内部的辅助函数实现具体的递归。

## Problem 15：dictionary list

A dictionary list is a Scheme list of pairs ((key value) (key value) ... (key value)) where each key is a unique symbol.

Implement (get dict key), a scheme procedure that takes a dictionary list dict and a value key that appears as the first element in some pair within dict. The get procedure returns the value paired with key. If key is not the first value in a pair within dict, return #f.

Then, implement (set dict key value), a scheme procedure that takes a dictionary list dict and key and value values. If key is a key in dict, then it returns a new dictionary-list that is the same length as dict but has value as the value paired with key. If key is not a key in dict, then it returns a dictionary list with all of the key-value pairs in dict as well as a new pair at the end containing (key value). Assume that no key appears more than once in dict.

```scheme
scm> (define dict-list '((a 1) (b 2) (c 3)))
dict-list
scm> (get dict-list 'b)
2
scm> (get dict-list 'e)
#f
scm> (set dict-list 'b 4)
((a 1) (b 4) (c 3))
scm> (set dict-list 'x 0)
((a 1) (b 2) (c 3) (x 0))
```

递归

## Problem 16：soulution-code

接收 含空白 的 Scheme 链表`problem` 和一个 Scheme 表达式`solution` ，返回把 五下划线空白`_____` 替换为`solution` 的结果；若有多处空白，每一处都用 同一个`solution` 替换。

Implement solution-code, a scheme procedure that takes in a Scheme list problem that contains a Scheme expression with a blank, as well as a Scheme expression solution. It returns the result of replacing the five-underscore blank _____ with the solution. If there are multiple blanks, they should each be replaced by the same solution expression.

```scheme
scm> (define add-problem '(define (add x y) _____))
add-problem
scm> (define add-sol '(+ x y))
add-sol
scm> (solution-code add-problem add-sol)
(define (add x y) (+ x y))
```