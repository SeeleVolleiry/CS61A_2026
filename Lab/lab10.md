# Lab10: Interpreters, Tail Calls

## Quasiquotation

The normal quote ' and the quasiquote ` are both valid ways to quote an expression.
However, the quasiquoted expression can be unquoted with the "unquote" , (represented by a comma).
When a term in a quasiquoted expression is unquoted, the unquoted term is evaluated, instead of being taken as literal text.
This mechanism is somewhat akin to using f-strings in Python, where expressions inside {} are evaluated and inserted into the string.

```scheme
scm> (define a 5)
a
scm> (define b 3)
b
scm> `(* a b)  ; Quasiquoted expression
(* a b)
scm> `(* a ,b)  ; Unquoted b, which evaluates to 3
(* a 3)
scm> `(* ,(+ a b) b)  ; Unquoted (+ a b), which evaluates to 8
(* 8 b)
```

## Q1: WWSD: Quasiquote

```scheme
scm> '(1 x 3)
? (1 x 3)
-- OK! --

scm> (define x 2)
? x
-- OK! --

scm> `(1 x 3)
? (1 x 3)
-- OK! --

scm> `(1 ,x 3)
? (1 2 3)
-- OK! --

scm> `(1 x ,3)
? (1 x 3)
-- OK! --

scm> `(1 (,x) 3)
? (1 (2) 3)
-- OK! --

scm> `(1 ,(+ x 2) 3)
? (1 4 3)
-- OK! --

scm> (define y 3)
? y      
-- OK! --

scm> `(x ,(* y x) y)
? (x 6  y)
-- OK! --

scm> `(1 ,(cons x (list y 4)) 5)
? (1 (2 3 4)  5)
-- OK! --
```

## Q2: Using Link

Answer the following questions about a Link instance representing the Calculator expression (+ (- 2 4) 6 8).
```
---------------------------------------------------------------------
Q: Find the Python expression that returns a `Link` representing the given expression: (+ (- 2 4) 6 8)
Choose the number of the correct choice:
0) Link(+, Link(Link(-, Link(2, Link(4))), Link(6, Link(8))))
1) Link('+', Link('-', Link(2, Link(4, Link(6, Link(8))))))
2) Link('+', Link(Link('-', Link(2, Link(4))), Link(6, Link(8))))
3) Link('+', Link(Link(-, Link(2, Link(4))), Link(6, Link(8))))
4) None of these
? 2
-- OK! --
---------------------------------------------------------------------
Q: What is the operator of the previous part's call expression?
Choose the number of the correct choice:
0) (
1) 6
2) 2
3) -
4) None of these
5) +
? 5
-- OK! --
---------------------------------------------------------------------
Q: If the `Link` you constructed in the previous part was bound to the name `p`,
how would you retrieve the operator?
Choose the number of the correct choice:
0) p
1) p.first
2) p.first.rest
3) p.rest.first
4) p.rest
? 1
-- OK! --
---------------------------------------------------------------------
Q: If the `Link` you constructed was bound to the name `p`, 
how would you retrieve a list containing all of the operands?
Choose the number of the correct choice:
0) p
1) p.rest.first
2) p.first.rest
3) p.first
4) p.rest
? 4
-- OK! --
---------------------------------------------------------------------
Q: How would you retrieve only the first operand?
Choose the number of the correct choice:
0) p.first.rest
1) p.rest.first
2) p.rest
3) p
4) p.first
? 1
-- OK! --
---------------------------------------------------------------------
Q: What is the first operand of the call expression (+ (- 2 4) 6 8) prior to evaluation?
Choose the number of the correct choice:
0) Link(2, Link(4))
1) 4
2) Link('-', Link(2, Link(4)))
3) 2
4) '-'
5) -2
6) '+'
? 2
-- OK! --
```

## Q3: New Procedure

Add the // operation to Calculator, a floor-division procedure.

Hint: You will need to modify both the calc_eval and floor_div methods for this question!

## Q4: New Form

Add and expressions to our Calculator interpreter as well as introduce the Scheme boolean values #t and #f, represented as Python True and False.

We cannot evaluate and expressions the same way we evaluate call expressions. Since and is a special form that short circuits on the first false argument, we need to add special logic so that we don't always evaluate all of the sub-expressions.

Important: To check whether some val is a false value in Scheme, use val is scheme_f rather than val == scheme_f because in Python 0 == False but 0 is not False (crazy, right!).

and的算法：短路原则+返回最后一个值或者返回True、False
    当前表达式：为空？返回True；不为空，进行下一步
    计算当前表达式的第一个值：是 scheme_f？ 是就返回False；不是，计算当前表达式的rest的first的值，并判断是否为scheme_f。
    一直重复第二步，直到计算到最后一个值仍未真，则返回该值。

## Q5: Repeat

补全`lab10.scm`

`Macro`：宏
A macro is a code transformation that is created using `define-macro` and applied using a call expression.
A macro call is evaluated by:

    Binding the formal parameters of the macro to the unevaluated operand expressions of the macro call.
    Evaluating the body of the macro, which returns an expression.
    Evaluating the expression returned by the macro in the frame of the original macro call.

```scheme
scm> (define-macro (twice expr) (list 'begin expr expr))
twice
scm> (twice (+ 2 2))  ; evaluates (begin (+ 2 2) (+ 2 2))
4
scm> (twice (print (+ 2 2)))  ; evaluates (begin (print (+ 2 2)) (print (+ 2 2)))
4
4
```

Hint:

    The repeated-call procedure takes a zero-argument procedure, so (lambda () ___) must appear in the blank. The body of the lambda is expr, which must be unquoted.

    Call f on no arguments with (f). If n is 1, just call f. If n is greater than 1, first call f and then call (repeated-call (- n 1) f).

## Q6: Concatenate

补全`lab10.scm`

`Tail Calls`